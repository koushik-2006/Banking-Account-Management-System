package com.easypay.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name="fixed_deposits")
public class FixedDeposit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="fd_ref", unique=true, nullable=false)
    private String fdRef;

    @Column(name="user_account", nullable=false)
    private String userAccount;

    @Column(nullable=false)
    private BigDecimal principal;

    @Column(name="interest_rate", nullable=false)
    private BigDecimal interestRate;

    @Column(name="tenure_months", nullable=false)
    private Integer tenureMonths;

    @Column(name="maturity_amount")
    private BigDecimal maturityAmount;

    @Column(name="interest_payout")
    private String interestPayout;

    @Column(name="start_date", nullable=false)
    private LocalDate startDate;

    @Column(name="maturity_date", nullable=false)
    private LocalDate maturityDate;

    @Column(name="is_senior_citizen")
    private Boolean isSeniorCitizen;

    private String status;

    @Column(name="created_at", insertable = false, updatable = false)
    private LocalDateTime createdAt;
}
