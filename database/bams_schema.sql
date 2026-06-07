-- Create and use database
CREATE DATABASE IF NOT EXISTS bams_db;
USE bams_db;

-- Users / Account Holders table
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  account_number VARCHAR(20) UNIQUE NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(15) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  gender ENUM('Male','Female','Other') NOT NULL,
  address TEXT,
  account_type ENUM('Savings','Current') DEFAULT 'Savings',
  account_status ENUM('Pending','Active','Suspended','Closed') DEFAULT 'Pending',
  kyc_status ENUM('Pending','Verified','Rejected') DEFAULT 'Pending',
  balance DECIMAL(15,2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Admins table
CREATE TABLE admins (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('superadmin','admin') DEFAULT 'admin',
  is_first_setup BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  transaction_ref VARCHAR(30) UNIQUE NOT NULL,
  from_account VARCHAR(20),
  to_account VARCHAR(20),
  amount DECIMAL(15,2) NOT NULL,
  transaction_type ENUM('Credit','Debit','Transfer','FD','Loan_EMI') NOT NULL,
  description VARCHAR(255),
  status ENUM('Pending','Success','Failed') DEFAULT 'Success',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (from_account) REFERENCES users(account_number) ON DELETE SET NULL,
  FOREIGN KEY (to_account) REFERENCES users(account_number) ON DELETE SET NULL
);

-- Loan Applications table
CREATE TABLE loan_applications (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  loan_ref VARCHAR(20) UNIQUE NOT NULL,
  user_account VARCHAR(20) NOT NULL,
  loan_type ENUM('Personal','Home','Car','Education') NOT NULL,
  amount DECIMAL(15,2) NOT NULL,
  tenure_months INT NOT NULL,
  interest_rate DECIMAL(5,2) NOT NULL,
  monthly_emi DECIMAL(15,2),
  purpose VARCHAR(255),
  status ENUM('Applied','Under_Review','Approved','Rejected','Active','Closed') DEFAULT 'Applied',
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number)
);

-- Fixed Deposits table
CREATE TABLE fixed_deposits (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  fd_ref VARCHAR(20) UNIQUE NOT NULL,
  user_account VARCHAR(20) NOT NULL,
  principal DECIMAL(15,2) NOT NULL,
  interest_rate DECIMAL(5,2) NOT NULL,
  tenure_days INT NOT NULL,
  maturity_amount DECIMAL(15,2),
  interest_payout ENUM('Monthly','Quarterly','On_Maturity') DEFAULT 'On_Maturity',
  start_date DATE NOT NULL,
  maturity_date DATE NOT NULL,
  status ENUM('Active','Matured','Closed_Prematurely') DEFAULT 'Active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number)
);

-- Cards table
CREATE TABLE cards (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  card_number VARCHAR(20) UNIQUE NOT NULL,
  user_account VARCHAR(20) NOT NULL,
  card_type ENUM('Debit','Credit') NOT NULL,
  card_variant ENUM('Classic','Silver','Platinum') DEFAULT 'Classic',
  cvv_hash VARCHAR(255) NOT NULL,
  expiry_date DATE NOT NULL,
  credit_limit DECIMAL(15,2) DEFAULT 0.00,
  daily_limit DECIMAL(15,2) DEFAULT 50000.00,
  is_active BOOLEAN DEFAULT TRUE,
  is_blocked BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number)
);

-- Beneficiaries table
CREATE TABLE beneficiaries (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  user_account VARCHAR(20) NOT NULL,
  nick_name VARCHAR(50) NOT NULL,
  beneficiary_account VARCHAR(20) NOT NULL,
  bank_name VARCHAR(100) NOT NULL,
  ifsc_code VARCHAR(15) NOT NULL,
  transfer_limit DECIMAL(15,2) DEFAULT 100000.00,
  is_active BOOLEAN DEFAULT TRUE,
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number)
);

-- Account Number Generator stored procedure
DELIMITER //
CREATE PROCEDURE GenerateAccountNumber(OUT acc_no VARCHAR(20))
BEGIN
  SET acc_no = CONCAT('BAMS', YEAR(NOW()), LPAD(FLOOR(RAND() * 100000), 6, '0'));
  WHILE EXISTS (SELECT 1 FROM users WHERE account_number = acc_no) DO
    SET acc_no = CONCAT('BAMS', YEAR(NOW()), LPAD(FLOOR(RAND() * 100000), 6, '0'));
  END WHILE;
END //
DELIMITER ;

-- Insert initial test data
INSERT INTO users (account_number, full_name, email, phone, password_hash, date_of_birth, gender, account_type, account_status, kyc_status, balance)
VALUES ('BAMS2026000001', 'Koushik Sethuraman', 'koushik@example.com', '9876543210', '$2a$10$PLACEHOLDER_BCRYPT_HASH', '2003-01-01', 'Male', 'Savings', 'Active', 'Verified', 50000.00);
