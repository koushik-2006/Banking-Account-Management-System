package com.bams.banking.controllers;

import com.bams.banking.models.User;
import com.bams.banking.services.AuthService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {
    private final AuthService service;

    @PostMapping("/register")
    public ResponseEntity<Map<String, String>> register(@RequestBody User request) {
        return ResponseEntity.ok(service.register(request));
    }

    @PostMapping("/login")
    public ResponseEntity<Map<String, String>> authenticate(@RequestBody Map<String, String> request) {
        return ResponseEntity.ok(service.authenticate(request.get("username"), request.get("password")));
    }
}
