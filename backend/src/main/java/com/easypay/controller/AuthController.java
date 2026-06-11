package com.easypay.controller;

import com.easypay.dto.ApiResponse;
import com.easypay.dto.LoginRequest;
import com.easypay.dto.RegisterRequest;
import com.easypay.service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = {"http://127.0.0.1:5501", "http://localhost:5501"})
public class AuthController {

    @Autowired
    private AuthService authService;

    @PostMapping("/register")
    public ApiResponse register(@RequestBody RegisterRequest req) {
        return authService.register(req);
    }

    @PostMapping("/login")
    public ApiResponse login(@RequestBody LoginRequest req) {
        return authService.login(req);
    }
}
