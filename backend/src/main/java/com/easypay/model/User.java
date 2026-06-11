package com.easypay.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name="users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="account_number", unique=true, nullable=false)
    private String accountNumber;

    @Column(name="full_name", nullable=false)
    private String fullName;

    @Column(unique=true, nullable=false)
    private String email;

    @Column(nullable=false)
    private String phone;

    @Column(name="password_hash", nullable=false)
    private String passwordHash;

    @Column(name="date_of_birth")
    private LocalDate dateOfBirth;

    private String gender;
    private String address;

    @Column(name="account_type")
    private String accountType;

    @Column(name="account_status")
    private String accountStatus;

    @Column(name="kyc_status")
    private String kycStatus;

    private BigDecimal balance;

    @Column(name="login_type")
    private String loginType;

    @Column(name="created_at", insertable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name="updated_at", insertable = false, updatable = false)
    private LocalDateTime updatedAt;
}
