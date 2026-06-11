package com.easypay.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name="loan_applications")
public class LoanApplication {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="loan_ref", unique=true, nullable=false)
    private String loanRef;

    @Column(name="user_account", nullable=false)
    private String userAccount;

    @Column(name="loan_type", nullable=false)
    private String loanType;

    @Column(nullable=false)
    private BigDecimal amount;

    @Column(name="tenure_months", nullable=false)
    private Integer tenureMonths;

    @Column(name="interest_rate", nullable=false)
    private BigDecimal interestRate;

    @Column(name="monthly_emi")
    private BigDecimal monthlyEmi;

    private String purpose;

    @Column(name="employer_name")
    private String employerName;

    @Column(name="monthly_income")
    private BigDecimal monthlyIncome;

    private String status;

    @Column(name="applied_at", insertable = false, updatable = false)
    private LocalDateTime appliedAt;
}
