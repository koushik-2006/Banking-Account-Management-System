package com.easypay.controller;

import com.easypay.dto.ApiResponse;
import com.easypay.model.CardApplication;
import com.easypay.model.FixedDeposit;
import com.easypay.model.LoanApplication;
import com.easypay.model.Transaction;
import com.easypay.model.User;
import com.easypay.repository.CardApplicationRepository;
import com.easypay.repository.FixedDepositRepository;
import com.easypay.repository.LoanApplicationRepository;
import com.easypay.repository.TransactionRepository;
import com.easypay.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.Map;

@RestController
@RequestMapping("/api/user")
@CrossOrigin(origins = {"http://127.0.0.1:5501", "http://localhost:5501"})
public class UserController {

    @Autowired private UserRepository userRepository;
    @Autowired private TransactionRepository transactionRepository;
    @Autowired private LoanApplicationRepository loanApplicationRepository;
    @Autowired private FixedDepositRepository fixedDepositRepository;
    @Autowired private CardApplicationRepository cardApplicationRepository;

    private String getAccountNumber() {
        return SecurityContextHolder.getContext().getAuthentication().getName();
    }

    @GetMapping("/profile")
    public ApiResponse getProfile() {
        User user = userRepository.findByAccountNumber(getAccountNumber()).orElse(null);
        if (user != null) {
            user.setPasswordHash(null);
            return new ApiResponse(true, "Success", user);
        }
        return new ApiResponse(false, "User not found", null);
    }

    @GetMapping("/transactions")
    public ApiResponse getTransactions() {
        String acc = getAccountNumber();
        return new ApiResponse(true, "Success", transactionRepository.findTop10ByFromAccountOrToAccountOrderByCreatedAtDesc(acc, acc));
    }

    @GetMapping("/balance")
    public ApiResponse getBalance() {
        User user = userRepository.findByAccountNumber(getAccountNumber()).orElse(null);
        if (user != null) {
            return new ApiResponse(true, "Success", Map.of("balance", user.getBalance()));
        }
        return new ApiResponse(false, "User not found", null);
    }

    @PostMapping("/transfer")
    public ApiResponse transfer(@RequestBody Map<String, Object> payload) {
        String toAccount = (String) payload.get("toAccount");
        BigDecimal amount = new BigDecimal(payload.get("amount").toString());
        String desc = (String) payload.get("description");
        
        User from = userRepository.findByAccountNumber(getAccountNumber()).orElseThrow();
        if (from.getBalance().compareTo(amount) < 0) {
            return new ApiResponse(false, "Insufficient balance", null);
        }

        User to = userRepository.findByAccountNumber(toAccount).orElse(null);
        if (to == null) return new ApiResponse(false, "Recipient not found", null);

        from.setBalance(from.getBalance().subtract(amount));
        to.setBalance(to.getBalance().add(amount));

        userRepository.save(from);
        userRepository.save(to);

        Transaction tx = new Transaction();
        tx.setTransactionRef("TX" + System.currentTimeMillis());
        tx.setFromAccount(from.getAccountNumber());
        tx.setToAccount(to.getAccountNumber());
        tx.setAmount(amount);
        tx.setTransactionType("Transfer");
        tx.setDescription(desc);
        tx.setStatus("Success");
        transactionRepository.save(tx);

        return new ApiResponse(true, "Transfer successful", tx);
    }

    @PostMapping("/apply-loan")
    public ApiResponse applyLoan(@RequestBody LoanApplication loan) {
        loan.setUserAccount(getAccountNumber());
        loan.setLoanRef("LN" + System.currentTimeMillis());
        loan.setStatus("Applied");
        loanApplicationRepository.save(loan);
        return new ApiResponse(true, "Loan applied", loan);
    }

    @PostMapping("/apply-fd")
    public ApiResponse applyFd(@RequestBody FixedDeposit fd) {
        fd.setUserAccount(getAccountNumber());
        fd.setFdRef("FD" + System.currentTimeMillis());
        fd.setStatus("Active");
        fixedDepositRepository.save(fd);
        return new ApiResponse(true, "FD applied", fd);
    }

    @PostMapping("/apply-card")
    public ApiResponse applyCard(@RequestBody CardApplication card) {
        card.setUserAccount(getAccountNumber());
        card.setCardRef("CC" + System.currentTimeMillis());
        card.setStatus("Pending");
        cardApplicationRepository.save(card);
        return new ApiResponse(true, "Card applied", card);
    }

    @GetMapping("/loans")
    public ApiResponse getLoans() {
        return new ApiResponse(true, "Success", loanApplicationRepository.findByUserAccount(getAccountNumber()));
    }

    @GetMapping("/fds")
    public ApiResponse getFds() {
        return new ApiResponse(true, "Success", fixedDepositRepository.findByUserAccount(getAccountNumber()));
    }

    @GetMapping("/cards")
    public ApiResponse getCards() {
        return new ApiResponse(true, "Success", cardApplicationRepository.findByUserAccount(getAccountNumber()));
    }
}
