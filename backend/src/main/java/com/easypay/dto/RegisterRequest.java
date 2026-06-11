package com.easypay.dto;

import lombok.Data;
import java.math.BigDecimal;

@Data
public class RegisterRequest {
    private String fullName;
    private String email;
    private String phone;
    private String password;
    private String gender;
    private String dateOfBirth;
    private String address;
    private String accountType;
    private BigDecimal initialDeposit;
}
