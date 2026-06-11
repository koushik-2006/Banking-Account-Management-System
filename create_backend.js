const fs = require('fs');
const path = require('path');

const baseDir = 'backend/src/main/java/com/easypay';

function ensureDir(dir) {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
}

// 1. application.properties
const appProps = `spring.application.name=EasyPay-Backend

# MySQL Connection
spring.datasource.url=jdbc:mysql://localhost:3306/bams_db?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
spring.datasource.username=root
spring.datasource.password=YOUR_MYSQL_ROOT_PASSWORD
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# JPA / Hibernate
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect

# Server
server.port=8080

# JWT
jwt.secret=EasyPay_JWT_Secret_Key_2026_256bit_secure
jwt.expiration=86400000

# CORS - allow frontend
spring.web.cors.allowed-origins=http://127.0.0.1:5501,http://localhost:5501

# Logging
logging.level.org.springframework.security=DEBUG
logging.level.com.easypay=DEBUG
`;
fs.writeFileSync('backend/src/main/resources/application.properties', appProps);

// 2. Main class
ensureDir(baseDir);
const mainClass = `package com.easypay;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class EasyPayApplication {
    public static void main(String[] args) {
        SpringApplication.run(EasyPayApplication.class, args);
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'EasyPayApplication.java'), mainClass);

// Models
ensureDir(path.join(baseDir, 'model'));
const userModel = `package com.easypay.model;

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
`;
fs.writeFileSync(path.join(baseDir, 'model', 'User.java'), userModel);

const txModel = `package com.easypay.model;

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
`;
fs.writeFileSync(path.join(baseDir, 'model', 'Transaction.java'), txModel);

const loanModel = `package com.easypay.model;

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
`;
fs.writeFileSync(path.join(baseDir, 'model', 'LoanApplication.java'), loanModel);

const fdModel = `package com.easypay.model;

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
`;
fs.writeFileSync(path.join(baseDir, 'model', 'FixedDeposit.java'), fdModel);

const cardModel = `package com.easypay.model;

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
`;
fs.writeFileSync(path.join(baseDir, 'model', 'CardApplication.java'), cardModel);

// Repositories
ensureDir(path.join(baseDir, 'repository'));
const userRepo = `package com.easypay.repository;

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
`;
fs.writeFileSync(path.join(baseDir, 'repository', 'UserRepository.java'), userRepo);

const txRepo = `package com.easypay.repository;

import com.easypay.model.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface TransactionRepository extends JpaRepository<Transaction, Long> {
    List<Transaction> findByFromAccountOrToAccountOrderByCreatedAtDesc(String fromAccount, String toAccount);
    List<Transaction> findTop10ByFromAccountOrToAccountOrderByCreatedAtDesc(String fromAccount, String toAccount);
}
`;
fs.writeFileSync(path.join(baseDir, 'repository', 'TransactionRepository.java'), txRepo);

const loanRepo = `package com.easypay.repository;

import com.easypay.model.LoanApplication;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LoanApplicationRepository extends JpaRepository<LoanApplication, Long> {
    List<LoanApplication> findByUserAccount(String userAccount);
    List<LoanApplication> findByStatus(String status);
}
`;
fs.writeFileSync(path.join(baseDir, 'repository', 'LoanApplicationRepository.java'), loanRepo);

const fdRepo = `package com.easypay.repository;

import com.easypay.model.FixedDeposit;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface FixedDepositRepository extends JpaRepository<FixedDeposit, Long> {
    List<FixedDeposit> findByUserAccount(String userAccount);
}
`;
fs.writeFileSync(path.join(baseDir, 'repository', 'FixedDepositRepository.java'), fdRepo);

const cardRepo = `package com.easypay.repository;

import com.easypay.model.CardApplication;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CardApplicationRepository extends JpaRepository<CardApplication, Long> {
    List<CardApplication> findByUserAccount(String userAccount);
}
`;
fs.writeFileSync(path.join(baseDir, 'repository', 'CardApplicationRepository.java'), cardRepo);

// DTOs
ensureDir(path.join(baseDir, 'dto'));
const registerReq = `package com.easypay.dto;

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
`;
fs.writeFileSync(path.join(baseDir, 'dto', 'RegisterRequest.java'), registerReq);

const loginReq = `package com.easypay.dto;

import lombok.Data;

@Data
public class LoginRequest {
    private String accountNumber;
    private String password;
}
`;
fs.writeFileSync(path.join(baseDir, 'dto', 'LoginRequest.java'), loginReq);

const apiRes = `package com.easypay.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ApiResponse {
    private boolean success;
    private String message;
    private Object data;
}
`;
fs.writeFileSync(path.join(baseDir, 'dto', 'ApiResponse.java'), apiRes);

// Security
ensureDir(path.join(baseDir, 'security'));
const jwtUtil = `package com.easypay.security;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.security.Key;
import java.util.Date;
import java.util.function.Function;

@Component
public class JwtUtil {
    @Value("\${jwt.secret}")
    private String secret;

    @Value("\${jwt.expiration}")
    private long expiration;

    private Key getSigningKey() {
        return Keys.hmacShaKeyFor(secret.getBytes());
    }

    public String generateToken(String accountNumber) {
        return Jwts.builder()
                .setSubject(accountNumber)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + expiration))
                .signWith(getSigningKey(), SignatureAlgorithm.HS256)
                .compact();
    }

    public String extractAccountNumber(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    public <T> T extractClaim(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }

    private Claims extractAllClaims(String token) {
        return Jwts.parserBuilder()
                .setSigningKey(getSigningKey())
                .build()
                .parseClaimsJws(token)
                .getBody();
    }

    public boolean validateToken(String token) {
        try {
            extractAllClaims(token);
            return !isTokenExpired(token);
        } catch (Exception e) {
            return false;
        }
    }

    private boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }

    private Date extractExpiration(String token) {
        return extractClaim(token, Claims::getExpiration);
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'security', 'JwtUtil.java'), jwtUtil);

const jwtFilter = `package com.easypay.security;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.ArrayList;

@Component
public class JwtFilter extends OncePerRequestFilter {

    @Autowired
    private JwtUtil jwtUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        final String authHeader = request.getHeader("Authorization");
        String accountNumber = null;
        String jwt = null;

        if (authHeader != null && authHeader.startsWith("Bearer ")) {
            jwt = authHeader.substring(7);
            accountNumber = jwtUtil.extractAccountNumber(jwt);
        }

        if (accountNumber != null && SecurityContextHolder.getContext().getAuthentication() == null) {
            if (jwtUtil.validateToken(jwt)) {
                UsernamePasswordAuthenticationToken authToken = new UsernamePasswordAuthenticationToken(
                        accountNumber, null, new ArrayList<>()
                );
                authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }
        filterChain.doFilter(request, response);
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'security', 'JwtFilter.java'), jwtFilter);

const securityConfig = `package com.easypay.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.web.cors.CorsConfiguration;

import java.util.Arrays;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Autowired
    private JwtFilter jwtFilter;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .cors(cors -> cors.configurationSource(request -> {
                CorsConfiguration config = new CorsConfiguration();
                config.setAllowedOrigins(Arrays.asList("http://127.0.0.1:5501", "http://localhost:5501"));
                config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"));
                config.setAllowedHeaders(Arrays.asList("*"));
                return config;
            }))
            .csrf(AbstractHttpConfigurer::disable)
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**", "/api/public/**").permitAll()
                .requestMatchers("/api/user/**", "/api/admin/**").authenticated()
                .anyRequest().authenticated()
            )
            .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'security', 'SecurityConfig.java'), securityConfig);

// Service
ensureDir(path.join(baseDir, 'service'));
const authService = `package com.easypay.service;

import com.easypay.dto.ApiResponse;
import com.easypay.dto.LoginRequest;
import com.easypay.dto.RegisterRequest;
import com.easypay.model.User;
import com.easypay.repository.UserRepository;
import com.easypay.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.Random;

@Service
public class AuthService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private JwtUtil jwtUtil;

    public ApiResponse register(RegisterRequest req) {
        if (userRepository.existsByEmail(req.getEmail())) {
            return new ApiResponse(false, "Email already registered", null);
        }

        String accountNumber = generateAccountNumber();

        User user = new User();
        user.setAccountNumber(accountNumber);
        user.setFullName(req.getFullName());
        user.setEmail(req.getEmail());
        user.setPhone(req.getPhone());
        user.setPasswordHash(passwordEncoder.encode(req.getPassword()));
        user.setGender(req.getGender());
        user.setDateOfBirth(LocalDate.parse(req.getDateOfBirth()));
        user.setAddress(req.getAddress());
        user.setAccountType(req.getAccountType());
        user.setBalance(req.getInitialDeposit() != null ? req.getInitialDeposit() : java.math.BigDecimal.ZERO);
        user.setAccountStatus("Pending");
        user.setKycStatus("Pending");
        user.setLoginType("manual");

        userRepository.save(user);

        Map<String, Object> data = new HashMap<>();
        data.put("accountNumber", accountNumber);

        return new ApiResponse(true, "Account created! Your account number is " + accountNumber, data);
    }

    public ApiResponse login(LoginRequest req) {
        Optional<User> userOpt = userRepository.findByAccountNumber(req.getAccountNumber());
        if (userOpt.isEmpty()) {
            return new ApiResponse(false, "Account number not found. Please check and try again.", null);
        }

        User user = userOpt.get();
        if (!passwordEncoder.matches(req.getPassword(), user.getPasswordHash())) {
            return new ApiResponse(false, "Incorrect password. Please try again.", null);
        }

        if ("Suspended".equalsIgnoreCase(user.getAccountStatus())) {
            return new ApiResponse(false, "Account suspended. Contact support.", null);
        }

        String token = jwtUtil.generateToken(user.getAccountNumber());

        Map<String, Object> data = new HashMap<>();
        data.put("token", token);
        data.put("accountNumber", user.getAccountNumber());
        data.put("fullName", user.getFullName());
        data.put("email", user.getEmail());
        data.put("accountType", user.getAccountType());
        data.put("balance", user.getBalance());
        data.put("accountStatus", user.getAccountStatus());

        return new ApiResponse(true, "Login successful", data);
    }

    private String generateAccountNumber() {
        Random random = new Random();
        String acc;
        do {
            acc = "EP2026" + String.format("%06d", random.nextInt(1000000));
        } while (userRepository.existsByAccountNumber(acc));
        return acc;
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'service', 'AuthService.java'), authService);

// Controllers
ensureDir(path.join(baseDir, 'controller'));
const authController = `package com.easypay.controller;

import com.easypay.dto.ApiResponse;
import com.easypay.dto.LoginRequest;
import com.easypay.dto.RegisterRequest;
import com.easypay.service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = {"http://127.0.0.1:5501", "http://localhost:5501"})
public class AuthController {

    @Autowired
    private AuthService authService;

    @PostMapping("/register")
    public ApiResponse register(@RequestBody RegisterRequest req) {
        return authService.register(req);
    }

    @PostMapping("/login")
    public ApiResponse login(@RequestBody LoginRequest req) {
        return authService.login(req);
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'controller', 'AuthController.java'), authController);

const userController = `package com.easypay.controller;

import com.easypay.dto.ApiResponse;
import com.easypay.model.CardApplication;
import com.easypay.model.FixedDeposit;
import com.easypay.model.LoanApplication;
import com.easypay.model.Transaction;
import com.easypay.model.User;
import com.easypay.repository.CardApplicationRepository;
import com.easypay.repository.FixedDepositRepository;
import com.easypay.repository.LoanApplicationRepository;
import com.easypay.repository.TransactionRepository;
import com.easypay.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.Map;

@RestController
@RequestMapping("/api/user")
@CrossOrigin(origins = {"http://127.0.0.1:5501", "http://localhost:5501"})
public class UserController {

    @Autowired private UserRepository userRepository;
    @Autowired private TransactionRepository transactionRepository;
    @Autowired private LoanApplicationRepository loanApplicationRepository;
    @Autowired private FixedDepositRepository fixedDepositRepository;
    @Autowired private CardApplicationRepository cardApplicationRepository;

    private String getAccountNumber() {
        return SecurityContextHolder.getContext().getAuthentication().getName();
    }

    @GetMapping("/profile")
    public ApiResponse getProfile() {
        User user = userRepository.findByAccountNumber(getAccountNumber()).orElse(null);
        if (user != null) {
            user.setPasswordHash(null);
            return new ApiResponse(true, "Success", user);
        }
        return new ApiResponse(false, "User not found", null);
    }

    @GetMapping("/transactions")
    public ApiResponse getTransactions() {
        String acc = getAccountNumber();
        return new ApiResponse(true, "Success", transactionRepository.findTop10ByFromAccountOrToAccountOrderByCreatedAtDesc(acc, acc));
    }

    @GetMapping("/balance")
    public ApiResponse getBalance() {
        User user = userRepository.findByAccountNumber(getAccountNumber()).orElse(null);
        if (user != null) {
            return new ApiResponse(true, "Success", Map.of("balance", user.getBalance()));
        }
        return new ApiResponse(false, "User not found", null);
    }

    @PostMapping("/transfer")
    public ApiResponse transfer(@RequestBody Map<String, Object> payload) {
        String toAccount = (String) payload.get("toAccount");
        BigDecimal amount = new BigDecimal(payload.get("amount").toString());
        String desc = (String) payload.get("description");
        
        User from = userRepository.findByAccountNumber(getAccountNumber()).orElseThrow();
        if (from.getBalance().compareTo(amount) < 0) {
            return new ApiResponse(false, "Insufficient balance", null);
        }

        User to = userRepository.findByAccountNumber(toAccount).orElse(null);
        if (to == null) return new ApiResponse(false, "Recipient not found", null);

        from.setBalance(from.getBalance().subtract(amount));
        to.setBalance(to.getBalance().add(amount));

        userRepository.save(from);
        userRepository.save(to);

        Transaction tx = new Transaction();
        tx.setTransactionRef("TX" + System.currentTimeMillis());
        tx.setFromAccount(from.getAccountNumber());
        tx.setToAccount(to.getAccountNumber());
        tx.setAmount(amount);
        tx.setTransactionType("Transfer");
        tx.setDescription(desc);
        tx.setStatus("Success");
        transactionRepository.save(tx);

        return new ApiResponse(true, "Transfer successful", tx);
    }

    @PostMapping("/apply-loan")
    public ApiResponse applyLoan(@RequestBody LoanApplication loan) {
        loan.setUserAccount(getAccountNumber());
        loan.setLoanRef("LN" + System.currentTimeMillis());
        loan.setStatus("Applied");
        loanApplicationRepository.save(loan);
        return new ApiResponse(true, "Loan applied", loan);
    }

    @PostMapping("/apply-fd")
    public ApiResponse applyFd(@RequestBody FixedDeposit fd) {
        fd.setUserAccount(getAccountNumber());
        fd.setFdRef("FD" + System.currentTimeMillis());
        fd.setStatus("Active");
        fixedDepositRepository.save(fd);
        return new ApiResponse(true, "FD applied", fd);
    }

    @PostMapping("/apply-card")
    public ApiResponse applyCard(@RequestBody CardApplication card) {
        card.setUserAccount(getAccountNumber());
        card.setCardRef("CC" + System.currentTimeMillis());
        card.setStatus("Pending");
        cardApplicationRepository.save(card);
        return new ApiResponse(true, "Card applied", card);
    }

    @GetMapping("/loans")
    public ApiResponse getLoans() {
        return new ApiResponse(true, "Success", loanApplicationRepository.findByUserAccount(getAccountNumber()));
    }

    @GetMapping("/fds")
    public ApiResponse getFds() {
        return new ApiResponse(true, "Success", fixedDepositRepository.findByUserAccount(getAccountNumber()));
    }

    @GetMapping("/cards")
    public ApiResponse getCards() {
        return new ApiResponse(true, "Success", cardApplicationRepository.findByUserAccount(getAccountNumber()));
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'controller', 'UserController.java'), userController);

const adminController = `package com.easypay.controller;

import com.easypay.dto.ApiResponse;
import com.easypay.model.CardApplication;
import com.easypay.model.LoanApplication;
import com.easypay.model.User;
import com.easypay.repository.CardApplicationRepository;
import com.easypay.repository.FixedDepositRepository;
import com.easypay.repository.LoanApplicationRepository;
import com.easypay.repository.TransactionRepository;
import com.easypay.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/admin")
@CrossOrigin(origins = {"http://127.0.0.1:5501", "http://localhost:5501"})
public class AdminController {

    @Autowired private UserRepository userRepository;
    @Autowired private TransactionRepository transactionRepository;
    @Autowired private LoanApplicationRepository loanApplicationRepository;
    @Autowired private FixedDepositRepository fixedDepositRepository;
    @Autowired private CardApplicationRepository cardApplicationRepository;

    @GetMapping("/users")
    public ApiResponse getUsers() {
        return new ApiResponse(true, "Success", userRepository.findAllByOrderByCreatedAtDesc());
    }

    @GetMapping("/loans")
    public ApiResponse getLoans() {
        return new ApiResponse(true, "Success", loanApplicationRepository.findAll());
    }

    @GetMapping("/fds")
    public ApiResponse getFds() {
        return new ApiResponse(true, "Success", fixedDepositRepository.findAll());
    }

    @GetMapping("/cards")
    public ApiResponse getCards() {
        return new ApiResponse(true, "Success", cardApplicationRepository.findAll());
    }

    @PatchMapping("/loans/{id}/decision")
    public ApiResponse updateLoan(@PathVariable Long id, @RequestBody Map<String, String> payload) {
        LoanApplication loan = loanApplicationRepository.findById(id).orElseThrow();
        loan.setStatus(payload.get("decision"));
        loanApplicationRepository.save(loan);
        return new ApiResponse(true, "Updated", loan);
    }

    @PatchMapping("/cards/{id}/decision")
    public ApiResponse updateCard(@PathVariable Long id, @RequestBody Map<String, String> payload) {
        CardApplication card = cardApplicationRepository.findById(id).orElseThrow();
        card.setStatus(payload.get("decision"));
        cardApplicationRepository.save(card);
        return new ApiResponse(true, "Updated", card);
    }

    @PatchMapping("/users/{id}/status")
    public ApiResponse updateUserStatus(@PathVariable Long id, @RequestBody Map<String, String> payload) {
        User user = userRepository.findById(id).orElseThrow();
        user.setAccountStatus(payload.get("status"));
        userRepository.save(user);
        return new ApiResponse(true, "Updated", user);
    }

    @GetMapping("/stats")
    public ApiResponse getStats() {
        Map<String, Object> stats = new HashMap<>();
        stats.put("totalUsers", userRepository.count());
        stats.put("activeUsers", userRepository.findAll().stream().filter(u -> "Active".equals(u.getAccountStatus())).count());
        stats.put("pendingLoans", loanApplicationRepository.findByStatus("Applied").size());
        stats.put("totalTransactions", transactionRepository.count());
        return new ApiResponse(true, "Success", stats);
    }
}
`;
fs.writeFileSync(path.join(baseDir, 'controller', 'AdminController.java'), adminController);

console.log('Backend files generated successfully in com.easypay');
