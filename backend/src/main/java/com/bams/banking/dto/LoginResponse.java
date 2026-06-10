package com.bams.banking.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class LoginResponse {
    private boolean success;
    private String message;
    private String accountNumber;
    private String fullName;
    private String email;
    private String accountType;
    private String accountStatus;
    private BigDecimal balance;
    private String token;
}
