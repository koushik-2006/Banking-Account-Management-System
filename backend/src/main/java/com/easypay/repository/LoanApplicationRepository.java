package com.easypay.repository;

import com.easypay.model.LoanApplication;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LoanApplicationRepository extends JpaRepository<LoanApplication, Long> {
    List<LoanApplication> findByUserAccount(String userAccount);
    List<LoanApplication> findByStatus(String status);
}
