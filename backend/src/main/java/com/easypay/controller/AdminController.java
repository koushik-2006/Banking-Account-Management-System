package com.easypay.controller;

import com.easypay.dto.ApiResponse;
import com.easypay.model.CardApplication;
import com.easypay.model.LoanApplication;
import com.easypay.model.User;
import com.easypay.repository.CardApplicationRepository;
import com.easypay.repository.FixedDepositRepository;
import com.easypay.repository.LoanApplicationRepository;
import com.easypay.repository.TransactionRepository;
import com.easypay.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/admin")
@CrossOrigin(origins = {"http://127.0.0.1:5501", "http://localhost:5501"})
public class AdminController {

    @Autowired private UserRepository userRepository;
    @Autowired private TransactionRepository transactionRepository;
    @Autowired private LoanApplicationRepository loanApplicationRepository;
    @Autowired private FixedDepositRepository fixedDepositRepository;
    @Autowired private CardApplicationRepository cardApplicationRepository;

    @GetMapping("/users")
    public ApiResponse getUsers() {
        return new ApiResponse(true, "Success", userRepository.findAllByOrderByCreatedAtDesc());
    }

    @GetMapping("/loans")
    public ApiResponse getLoans() {
        return new ApiResponse(true, "Success", loanApplicationRepository.findAll());
    }

    @GetMapping("/fds")
    public ApiResponse getFds() {
        return new ApiResponse(true, "Success", fixedDepositRepository.findAll());
    }

    @GetMapping("/cards")
    public ApiResponse getCards() {
        return new ApiResponse(true, "Success", cardApplicationRepository.findAll());
    }

    @PatchMapping("/loans/{id}/decision")
    public ApiResponse updateLoan(@PathVariable Long id, @RequestBody Map<String, String> payload) {
        LoanApplication loan = loanApplicationRepository.findById(id).orElseThrow();
        loan.setStatus(payload.get("decision"));
        loanApplicationRepository.save(loan);
        return new ApiResponse(true, "Updated", loan);
    }

    @PatchMapping("/cards/{id}/decision")
    public ApiResponse updateCard(@PathVariable Long id, @RequestBody Map<String, String> payload) {
        CardApplication card = cardApplicationRepository.findById(id).orElseThrow();
        card.setStatus(payload.get("decision"));
        cardApplicationRepository.save(card);
        return new ApiResponse(true, "Updated", card);
    }

    @PatchMapping("/users/{id}/status")
    public ApiResponse updateUserStatus(@PathVariable Long id, @RequestBody Map<String, String> payload) {
        User user = userRepository.findById(id).orElseThrow();
        user.setAccountStatus(payload.get("status"));
        userRepository.save(user);
        return new ApiResponse(true, "Updated", user);
    }

    @GetMapping("/stats")
    public ApiResponse getStats() {
        Map<String, Object> stats = new HashMap<>();
        stats.put("totalUsers", userRepository.count());
        stats.put("activeUsers", userRepository.findAll().stream().filter(u -> "Active".equals(u.getAccountStatus())).count());
        stats.put("pendingLoans", loanApplicationRepository.findByStatus("Applied").size());
        stats.put("totalTransactions", transactionRepository.count());
        return new ApiResponse(true, "Success", stats);
    }
}
