package com.bams.banking.models;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Collection;
import java.util.List;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "users")
public class User implements UserDetails {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true)
    private String accountNumber;
    
    private String fullName;
    
    @Column(unique = true)
    private String email;
    
    private String phone;
    
    @Column(name = "password_hash")
    private String passwordHash;
    
    private String address;
    private String gender;
    
    private LocalDate dateOfBirth;
    
    @Enumerated(EnumType.STRING)
    private AccountType accountType;
    
    @Enumerated(EnumType.STRING)
    private AccountStatus accountStatus;
    
    @Enumerated(EnumType.STRING)
    private KycStatus kycStatus;
    
    private BigDecimal balance;
    
    private LocalDateTime createdAt;

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of(new SimpleGrantedAuthority("ROLE_USER"));
    }

    @Override
    public String getPassword() {
        return passwordHash;
    }

    @Override
    public String getUsername() {
        return accountNumber;
    }

    @Override
    public boolean isAccountNonExpired() { return true; }

    @Override
    public boolean isAccountNonLocked() { return accountStatus != AccountStatus.Suspended && accountStatus != AccountStatus.Closed; }

    @Override
    public boolean isCredentialsNonExpired() { return true; }

    @Override
    public boolean isEnabled() { return true; }
}
