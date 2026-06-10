package com.bams.banking.controllers;

import com.bams.banking.dto.LoginRequest;
import com.bams.banking.dto.RegisterRequest;
import com.bams.banking.models.User;
import com.bams.banking.repositories.UserRepository;
import com.bams.banking.security.JwtService;
import com.bams.banking.services.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = "*")
public class AuthController {

    @Autowired
    private AuthService authService;

    @Autowired
    private JwtService jwtService; // from the existing project

    @Autowired
    private UserRepository userRepository;

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody RegisterRequest req) {
        return ResponseEntity.ok(authService.register(req));
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest req) {
        return ResponseEntity.ok(authService.login(req));
    }

    @GetMapping("/me")
    public ResponseEntity<?> getMe(@RequestHeader("Authorization") String tokenHeader) {
        try {
            String token = tokenHeader.substring(7); // Remove "Bearer "
            String accountNumber = jwtService.extractUsername(token);
            
            Optional<User> userOpt = userRepository.findByAccountNumber(accountNumber);
            if (userOpt.isPresent()) {
                User user = userOpt.get();
                // Returning a subset of info or the whole entity as JSON (excluding password)
                user.setPasswordHash(null);
                return ResponseEntity.ok(user);
            }
            return ResponseEntity.badRequest().body("{\"success\":false, \"message\":\"User not found\"}");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("{\"success\":false, \"message\":\"Invalid token\"}");
        }
    }
}
