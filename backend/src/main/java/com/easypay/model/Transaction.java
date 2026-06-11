package com.easypay.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name="transactions")
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="transaction_ref", unique=true, nullable=false)
    private String transactionRef;

    @Column(name="from_account")
    private String fromAccount;

    @Column(name="to_account")
    private String toAccount;

    @Column(nullable=false)
    private BigDecimal amount;

    @Column(name="transaction_type", nullable=false)
    private String transactionType;

    private String description;
    private String status;

    @Column(name="created_at", insertable = false, updatable = false)
    private LocalDateTime createdAt;
}
