package com.bams.banking.services;

import com.bams.banking.dto.LoginRequest;
import com.bams.banking.dto.LoginResponse;
import com.bams.banking.dto.RegisterRequest;
import com.bams.banking.models.AccountStatus;
import com.bams.banking.models.AccountType;
import com.bams.banking.models.KycStatus;
import com.bams.banking.models.User;
import com.bams.banking.repositories.UserRepository;
import com.bams.banking.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Optional;

@Service
public class AuthService {

    @Autowired
    private UserRepository userRepo;

    @Autowired
    private PasswordEncoder encoder;

    @Autowired
    private JwtUtil jwtUtil;

    public LoginResponse register(RegisterRequest req) {
        if (userRepo.findByEmail(req.getEmail()).isPresent()) {
            return LoginResponse.builder()
                    .success(false)
                    .message("Email already registered")
                    .build();
        }

        String accNo = generateAccountNumber();
        
        User user = User.builder()
                .accountNumber(accNo)
                .fullName(req.getFullName())
                .email(req.getEmail())
                .phone(req.getPhone())
                .passwordHash(encoder.encode(req.getPassword()))
                .gender(req.getGender())
                .dateOfBirth(LocalDate.parse(req.getDateOfBirth()))
                .address(req.getAddress())
                .accountType(AccountType.valueOf(req.getAccountType()))
                .accountStatus(AccountStatus.Pending)
                .kycStatus(KycStatus.Pending)
                .balance(BigDecimal.ZERO)
                .createdAt(LocalDateTime.now())
                .build();
                
        userRepo.save(user);

        return LoginResponse.builder()
                .success(true)
                .message("Account created successfully! Account No: " + accNo)
                .accountNumber(accNo)
                .fullName(req.getFullName())
                .email(req.getEmail())
                .accountType(req.getAccountType())
                .accountStatus("Pending")
                .balance(BigDecimal.ZERO)
                .build();
    }

    public LoginResponse login(LoginRequest req) {
        Optional<User> userOpt = userRepo.findByAccountNumber(req.getAccountNumber());
        
        if (userOpt.isEmpty()) {
            return LoginResponse.builder()
                    .success(false)
                    .message("Account number not found. Please check and try again.")
                    .build();
        }
        
        User user = userOpt.get();
        
        if (!encoder.matches(req.getPassword(), user.getPasswordHash())) {
            return LoginResponse.builder()
                    .success(false)
                    .message("Incorrect password. Please try again.")
                    .build();
        }
        
        if (user.getAccountStatus() == AccountStatus.Suspended) {
            return LoginResponse.builder()
                    .success(false)
                    .message("Your account is suspended. Contact support.")
                    .build();
        }
        
        String token = jwtUtil.generateToken(user.getAccountNumber());
        
        return LoginResponse.builder()
                .success(true)
                .message("Login successful! Welcome, " + user.getFullName())
                .accountNumber(user.getAccountNumber())
                .fullName(user.getFullName())
                .email(user.getEmail())
                .accountType(user.getAccountType().name())
                .accountStatus(user.getAccountStatus().name())
                .balance(user.getBalance())
                .token(token)
                .build();
    }

    private String generateAccountNumber() {
        String acc;
        do {
            acc = "BAMS2026" + String.format("%06d", (int)(Math.random() * 1000000));
        } while (userRepo.findByAccountNumber(acc).isPresent());
        return acc;
    }
}
