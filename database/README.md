# BAMS Database Setup

1. Install MySQL 8.0
2. Open MySQL Workbench or terminal
3. Run: `mysql -u root -p < database/bams_schema.sql`
4. Verify: 
   ```sql
   USE bams_db;
   SHOW TABLES;
   ```
