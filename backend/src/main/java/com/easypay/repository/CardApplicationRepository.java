package com.easypay.repository;

import com.easypay.model.CardApplication;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CardApplicationRepository extends JpaRepository<CardApplication, Long> {
    List<CardApplication> findByUserAccount(String userAccount);
}
