package com.easypay.service;

import com.easypay.dto.ApiResponse;
import com.easypay.dto.LoginRequest;
import com.easypay.dto.RegisterRequest;
import com.easypay.model.User;
import com.easypay.repository.UserRepository;
import com.easypay.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.Random;

@Service
public class AuthService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private JwtUtil jwtUtil;

    public ApiResponse register(RegisterRequest req) {
        if (userRepository.existsByEmail(req.getEmail())) {
            return new ApiResponse(false, "Email already registered", null);
        }

        String accountNumber = generateAccountNumber();

        User user = new User();
        user.setAccountNumber(accountNumber);
        user.setFullName(req.getFullName());
        user.setEmail(req.getEmail());
        user.setPhone(req.getPhone());
        user.setPasswordHash(passwordEncoder.encode(req.getPassword()));
        user.setGender(req.getGender());
        user.setDateOfBirth(LocalDate.parse(req.getDateOfBirth()));
        user.setAddress(req.getAddress());
        user.setAccountType(req.getAccountType());
        user.setBalance(req.getInitialDeposit() != null ? req.getInitialDeposit() : java.math.BigDecimal.ZERO);
        user.setAccountStatus("Pending");
        user.setKycStatus("Pending");
        user.setLoginType("manual");

        userRepository.save(user);

        Map<String, Object> data = new HashMap<>();
        data.put("accountNumber", accountNumber);

        return new ApiResponse(true, "Account created! Your account number is " + accountNumber, data);
    }

    public ApiResponse login(LoginRequest req) {
        Optional<User> userOpt = userRepository.findByAccountNumber(req.getAccountNumber());
        if (userOpt.isEmpty()) {
            return new ApiResponse(false, "Account number not found. Please check and try again.", null);
        }

        User user = userOpt.get();
        if (!passwordEncoder.matches(req.getPassword(), user.getPasswordHash())) {
            return new ApiResponse(false, "Incorrect password. Please try again.", null);
        }

        if ("Suspended".equalsIgnoreCase(user.getAccountStatus())) {
            return new ApiResponse(false, "Account suspended. Contact support.", null);
        }

        String token = jwtUtil.generateToken(user.getAccountNumber());

        Map<String, Object> data = new HashMap<>();
        data.put("token", token);
        data.put("accountNumber", user.getAccountNumber());
        data.put("fullName", user.getFullName());
        data.put("email", user.getEmail());
        data.put("accountType", user.getAccountType());
        data.put("balance", user.getBalance());
        data.put("accountStatus", user.getAccountStatus());

        return new ApiResponse(true, "Login successful", data);
    }

    private String generateAccountNumber() {
        Random random = new Random();
        String acc;
        do {
            acc = "EP2026" + String.format("%06d", random.nextInt(1000000));
        } while (userRepository.existsByAccountNumber(acc));
        return acc;
    }
}
