package com.easypay.repository;

import com.easypay.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByAccountNumber(String accountNumber);
    Optional<User> findByEmail(String email);
    boolean existsByEmail(String email);
    boolean existsByAccountNumber(String accountNumber);
    List<User> findAllByOrderByCreatedAtDesc();
}
