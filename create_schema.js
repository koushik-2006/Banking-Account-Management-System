const fs = require('fs');
const path = require('path');

const bamsSchemaSql = `CREATE DATABASE IF NOT EXISTS bams_db;
USE bams_db;

CREATE TABLE users (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  account_number VARCHAR(20) UNIQUE NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(15) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  gender VARCHAR(10),
  address TEXT,
  account_type ENUM('Savings','Current') DEFAULT 'Savings',
  account_status ENUM('Pending','Active','Suspended','Closed') DEFAULT 'Pending',
  kyc_status ENUM('Pending','Verified','Rejected') DEFAULT 'Pending',
  balance DECIMAL(15,2) DEFAULT 0.00,
  login_type VARCHAR(20) DEFAULT 'manual',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE admins (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('superadmin','admin') DEFAULT 'superadmin',
  is_setup_done BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  transaction_ref VARCHAR(30) UNIQUE NOT NULL,
  from_account VARCHAR(20),
  to_account VARCHAR(20),
  amount DECIMAL(15,2) NOT NULL,
  transaction_type ENUM('Credit','Debit','Transfer','FD_Debit','Loan_Credit','EMI_Debit') NOT NULL,
  description VARCHAR(255),
  status ENUM('Pending','Success','Failed') DEFAULT 'Success',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (from_account) REFERENCES users(account_number) ON DELETE SET NULL,
  FOREIGN KEY (to_account) REFERENCES users(account_number) ON DELETE SET NULL
);

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
  employer_name VARCHAR(100),
  monthly_income DECIMAL(15,2),
  status ENUM('Applied','Under_Review','Approved','Rejected','Active','Closed') DEFAULT 'Applied',
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number) ON DELETE CASCADE
);

CREATE TABLE fixed_deposits (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  fd_ref VARCHAR(20) UNIQUE NOT NULL,
  user_account VARCHAR(20) NOT NULL,
  principal DECIMAL(15,2) NOT NULL,
  interest_rate DECIMAL(5,2) NOT NULL,
  tenure_months INT NOT NULL,
  maturity_amount DECIMAL(15,2),
  interest_payout ENUM('Monthly','Quarterly','On_Maturity') DEFAULT 'On_Maturity',
  start_date DATE NOT NULL,
  maturity_date DATE NOT NULL,
  is_senior_citizen BOOLEAN DEFAULT FALSE,
  status ENUM('Active','Matured','Closed_Early') DEFAULT 'Active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number) ON DELETE CASCADE
);

CREATE TABLE card_applications (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  card_ref VARCHAR(20) UNIQUE NOT NULL,
  user_account VARCHAR(20) NOT NULL,
  card_type ENUM('Silver','Gold','Platinum') NOT NULL,
  credit_limit DECIMAL(15,2),
  masked_number VARCHAR(20),
  expiry_date VARCHAR(10),
  monthly_income DECIMAL(15,2),
  employment_type VARCHAR(30),
  billing_address TEXT,
  status ENUM('Pending','Approved','Rejected') DEFAULT 'Pending',
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number) ON DELETE CASCADE
);

CREATE TABLE beneficiaries (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  user_account VARCHAR(20) NOT NULL,
  nick_name VARCHAR(50) NOT NULL,
  beneficiary_account VARCHAR(20) NOT NULL,
  bank_name VARCHAR(100) NOT NULL,
  ifsc_code VARCHAR(15) NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_account) REFERENCES users(account_number) ON DELETE CASCADE
);

INSERT INTO users (account_number, full_name, email, phone, password_hash, gender, account_type, account_status, kyc_status, balance)
VALUES ('EP2026TEST01', 'Test User', 'test@easypay.com', '9876543210', '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LvtLWkJ8iFa', 'Male', 'Savings', 'Active', 'Verified', 50000.00);

-- USEFUL QUERIES:
-- See all users:          SELECT id, account_number, full_name, email, account_type, balance, account_status, created_at FROM users;
-- See all transactions:   SELECT * FROM transactions ORDER BY created_at DESC;
-- See all loans:          SELECT * FROM loan_applications ORDER BY applied_at DESC;
-- See all FDs:            SELECT * FROM fixed_deposits;
-- See all card apps:      SELECT * FROM card_applications;
-- Count total users:      SELECT COUNT(*) as total_users FROM users;
-- Active users only:      SELECT * FROM users WHERE account_status = 'Active';
-- Pending loans:          SELECT * FROM loan_applications WHERE status = 'Applied';
`;

// TASK 1
fs.writeFileSync('database/bams_schema.sql', bamsSchemaSql);
console.log('bams_schema.sql created.');
