# Banking Account Management System (BAMS) - Project Report

## 1. Abstract
The Banking Account Management System (BAMS) is a modern, responsive web application designed to streamline personal banking and administrative oversight. Built with a focus on security, user experience, and scalability, BAMS provides a comprehensive suite of tools for both customers (transfers, loans, cards) and administrators (customer management, loan processing, auditing).

## 2. Introduction
BAMS addresses the need for efficient digital banking solutions that combine ease of use with robust administrative control.

## 3. System Architecture
- **Frontend**: Vanilla HTML/CSS/JS (SPA-like navigation with separate pages).
- **Backend**: Spring Boot 3 with JWT Security.
- **Database**: JPA/Hibernate with H2/SQL.

## 4. Database Schema
Refer to `database/schema.sql`.
- `users`: Core authentication and profile data.
- `accounts`: Financial balance and account details.
- `transactions`: Detailed audit trail of all movements.
- `loans`: Application and tracking.
- `cards`: Virtual card management and limits.
- `fixed_deposits`: Investment tracking.

## 5. Module Descriptions
### Customer Portal
- **Dashboard**: Financial overview with Chart.js analytics.
- **Transfers**: IMPS/NEFT/RTGS with OTP simulation.
- **Beneficiaries**: Payee management.
- **Cards**: 3D interactive virtual cards with real-time controls.
- **Loans**: Application and EMI calculator.

### Admin Portal
- **Dashboard**: Global system metrics and flagged activity.
- **Customer Manager**: Profile oversight and account activation/disabling.
- **Loan Processor**: Application queue with credit score simulation.
- **Global Audit**: Real-time transaction feed for fraud monitoring.

## 6. Testing Summary
| Feature | Test Case | Status |
|---------|-----------|--------|
| Login | Valid/Invalid JWT | Pass |
| Transfer | Balance Validation | Pass |
| Loan | Approval Workflow | Pass |
| Admin | Role Protection | Pass |

## 7. Conclusion
BAMS successfully demonstrates a full-stack banking solution with modern UI/UX principles and secure architectural patterns.
