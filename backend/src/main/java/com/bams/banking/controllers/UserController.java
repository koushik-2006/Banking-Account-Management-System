package com.bams.banking.controllers;

import com.bams.banking.models.User;
import com.bams.banking.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/user")
@CrossOrigin(origins = "*")
public class UserController {

    @Autowired
    private UserRepository userRepo;

    @GetMapping("/profile")
    @PreAuthorize("isAuthenticated()")
    public ResponseEntity<?> getUserProfile(@AuthenticationPrincipal org.springframework.security.core.userdetails.UserDetails userDetails) {
        String accountNumber = userDetails.getUsername();
        User user = userRepo.findByAccountNumber(accountNumber).orElseThrow();
        Map<String,Object> res = new HashMap<>();
        res.put("success", true);
        res.put("fullName", user.getFullName());
        res.put("email", user.getEmail());
        res.put("accountNumber", user.getAccountNumber());
        res.put("accountType", user.getAccountType().name());
        res.put("accountStatus", user.getAccountStatus().name());
        res.put("balance", user.getBalance());
        res.put("phone", user.getPhone());
        res.put("kycStatus", user.getKycStatus().name());
        res.put("createdAt", user.getCreatedAt().toString());
        return ResponseEntity.ok(res);
    }
}
