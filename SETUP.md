# Easy pAy — How to Run

## Step 1: Setup Database
Open VS Code Terminal → run:
mysql -u root -p < database/bams_schema.sql

## Step 2: Update Password
Open backend/src/main/resources/application.properties
Change: spring.datasource.password=YOUR_MYSQL_ROOT_PASSWORD
To your actual MySQL root password.

## Step 3: Run Spring Boot
cd backend
mvn spring-boot:run
Wait until you see: "Started EasyPayApplication on port 8080"

## Step 4: Run Frontend
Open VS Code → Right-click frontend/index.html → Open with Live Server
Frontend runs at: http://127.0.0.1:5501/frontend/index.html
Backend API at:   http://localhost:8080/api

## Step 5: Verify in MySQL (VS Code MySQL Extension)
Right-click users table → Open Table → See all registered users
Or run: SELECT account_number, full_name, email, balance, account_status FROM users;

## Test Login
Account Number: EP2026TEST01
Password: test123
