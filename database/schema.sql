-- CORE BANKING TABLES

-- Transactions Table
CREATE TABLE transactions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50) UNIQUE NOT NULL,
    from_account VARCHAR(20) NOT NULL,
    to_account VARCHAR(20) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    type ENUM('TRANSFER', 'DEPOSIT', 'WITHDRAWAL', 'BILL_PAY') NOT NULL,
    mode ENUM('NEFT', 'RTGS', 'IMPS', 'INTERNAL') NOT NULL,
    status ENUM('SUCCESS', 'PENDING', 'FAILED') DEFAULT 'SUCCESS',
    remarks VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Beneficiaries Table
CREATE TABLE beneficiaries (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    name VARCHAR(100) NOT NULL,
    account_number VARCHAR(20) NOT NULL,
    ifsc_code VARCHAR(15) NOT NULL,
    bank_name VARCHAR(100),
    nick_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Loans Table
CREATE TABLE loans (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    loan_type ENUM('HOME', 'PERSONAL', 'CAR', 'EDUCATION') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    tenure_years INT NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    status ENUM('APPLIED', 'UNDER_REVIEW', 'APPROVED', 'ACTIVE', 'CLOSED') DEFAULT 'APPLIED',
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Cards Table
CREATE TABLE cards (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    card_number VARCHAR(19) UNIQUE NOT NULL,
    card_type ENUM('DEBIT', 'CREDIT') NOT NULL,
    expiry_date VARCHAR(5) NOT NULL,
    cvv VARCHAR(3) NOT NULL,
    is_blocked BOOLEAN DEFAULT FALSE,
    online_limit DECIMAL(15, 2) DEFAULT 5000,
    intl_limit DECIMAL(15, 2) DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Fixed Deposits Table
CREATE TABLE fixed_deposits (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    tenure_years INT NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    maturity_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
