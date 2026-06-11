package com.easypay.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name="card_applications")
public class CardApplication {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="card_ref", unique=true, nullable=false)
    private String cardRef;

    @Column(name="user_account", nullable=false)
    private String userAccount;

    @Column(name="card_type", nullable=false)
    private String cardType;

    @Column(name="credit_limit")
    private BigDecimal creditLimit;

    @Column(name="masked_number")
    private String maskedNumber;

    @Column(name="expiry_date")
    private String expiryDate;

    @Column(name="monthly_income")
    private BigDecimal monthlyIncome;

    @Column(name="employment_type")
    private String employmentType;

    @Column(name="billing_address")
    private String billingAddress;

    private String status;

    @Column(name="applied_at", insertable = false, updatable = false)
    private LocalDateTime appliedAt;
}
