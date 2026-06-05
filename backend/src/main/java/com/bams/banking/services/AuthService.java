package com.bams.banking.services;

import com.bams.banking.models.User;
import com.bams.banking.repositories.UserRepository;
import com.bams.banking.security.JwtService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Map;

@Service
@RequiredArgsConstructor
public class AuthService {
    private final UserRepository repository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    public Map<String, String> register(User request) {
        var user = User.builder()
                .firstName(request.getFirstName())
                .lastName(request.getLastName())
                .email(request.getEmail())
                .username(request.getUsername())
                .password(passwordEncoder.encode(request.getPassword()))
                .role(User.Role.ROLE_CUSTOMER)
                .build();
        repository.save(user);
        var jwtToken = jwtService.generateToken(user);
        return Map.of("token", jwtToken);
    }

    public Map<String, String> authenticate(String username, String password) {
        authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(username, password)
        );
        var user = repository.findByUsername(username).orElseThrow();
        var jwtToken = jwtService.generateToken(user);
        return Map.of("token", jwtToken);
    }
}
