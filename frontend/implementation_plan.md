# Global App Update: Logo, Forms, Admin Portal, & Link Audit

This comprehensive plan covers four major sets of updates across the Banking Account Management System frontend to ensure a seamless, robust user experience.

## User Review Required

> [!IMPORTANT]
> Please review this final, combined implementation plan containing all 3 sets of requirements you requested.
> Once you provide approval, I will proceed to execution.

## Open Questions

None. The specifications are detailed and unambiguous.

## Proposed Changes

---

### 1. Global Logo Fix
I will use an automated script to replace the existing `<a href="index.html" class="logo-container">...</a>` tag in all HTML files.
- The replacement will be the provided inline SVG, avoiding any "broken image" links.
- `href` will dynamically point to `index.html` or `../index.html` depending on the file's subdirectory depth (e.g., `admin/`).

---

### 2. Global Link Audit & Connection Pass

I will execute a comprehensive sweep of all navigation structures across the entire frontend to ensure no broken or empty (`#`) links exist.

#### [MODIFY] Footer (All HTML Files)
- Update all standard footer links ensuring they resolve correctly based on file depth:
  - **Quick Links**: Home (`index.html`), Services (`services.html`), About (`about.html`), Contact (`contact.html`)
  - **Support**: FAQ (`faq.html`), Privacy Policy (`policies.html`), Terms & Conditions (`policies.html`), Branch Locator (`contact.html`)
- **Admin Access**: Append a hidden link to the footer for easy administrative access:
  `<a href="admin/login.html" style="font-size:11px;color:#555;opacity:0.4;">Admin</a>`

#### [MODIFY] [services.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/services.html)
- Update all "Apply Now" buttons to point to the new forms: `apply-savings.html`, `apply-current.html`, `apply-fd.html`, `apply-personal-loan.html`, `apply-home-loan.html`, `apply-credit-card.html`.
- Update all "Learn More" links to point to their specific informational pages (e.g., `savings-account.html`).

#### [MODIFY] [index.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/index.html)
- Update Hero "Get Started" to scroll to `#services`.
- Update Hero "Learn More" to route to `services.html`.
- Implement a JavaScript `setInterval` counting animation on page load for the Stats section numbers.

#### [MODIFY] [dashboard.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/dashboard.html) (and portal pages)
- Ensure all sidebar items link flawlessly: Dashboard, Account Overview, Transactions, Fund Transfer, Loans, Cards, Fixed Deposits, Profile, Notifications.
- The Logout link will clear `bams_user` from `localStorage` and redirect to `index.html`.

---

### 3. Application Forms (New Files)

I will create 6 new HTML files for multi-step application processes. All forms will include the BAMS navbar, footer, a gold progress bar, validation, and local storage hooks. 
- **Breadcrumbs:** Each `apply-*.html` file will include a breadcrumb at the top (e.g., Home → Services → [Current Service Name]).

#### [NEW] [apply-savings.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/apply-savings.html)
- 3 Steps: Preferences, Nominee Details, Review & Submit. Saves to `localStorage`.

#### [NEW] [apply-current.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/apply-current.html)
- 3 Steps: Business Details, Overdraft Facility, Documents Checklist. Saves to `localStorage`.

#### [NEW] [apply-fd.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/apply-fd.html)
- 2 Steps: Configuration (with real-time maturity calculator), Review & Submit. Pushes to `bams_fd_apps`.

#### [NEW] [apply-personal-loan.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/apply-personal-loan.html)
- 4 Steps: Loan Details (with live EMI calculator), Employment, Documents, Review & Submit. Pushes to `bams_loan_apps`.

#### [NEW] [apply-home-loan.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/apply-home-loan.html)
- 4 Steps: Property Details, Co-applicant, Documents, Review & Submit. Pushes to `bams_loan_apps`.

#### [NEW] [apply-credit-card.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/apply-credit-card.html)
- 3 Steps: Card Selection, Employment & Income, Review & Submit. Pushes to `bams_card_apps`.

---

### 4. Admin Portal (New Files)

I will create an Admin Portal in the `frontend/admin/` directory relying entirely on `localStorage`.

#### [NEW] [admin/setup.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/admin/setup.html)
- First-time Admin Setup validating the Secret Key. Saves encrypted credentials to `bams_admin`.

#### [NEW] [admin/login.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/admin/login.html)
- Admin Login page setting `bams_admin_session` upon successful authentication.

#### [NEW] [admin/dashboard.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/admin/dashboard.html)
- Admin Dashboard showing 4 metric cards (Total Users, Pending Loans/FDs/Cards) and a Recent Activity table combining data from all queues.

#### [NEW] [admin/customers.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/admin/customers.html)
- Customer list view with real-time search, CSV export, and row-level actions (Approve, Reject).

#### [NEW] [admin/applications.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/admin/applications.html)
- Application management featuring a tabbed interface (Loans, FDs, Cards) with Approve/Reject capability and a "Clear All" button.

#### [MODIFY] [register.html](file:///c:/Users/koush/OneDrive/Desktop/Banking-Account-Management-System/frontend/register.html)
- Update logic to save newly registered users with a status of 'Pending' and a 'createdAt' timestamp so they populate in the Admin Portal.

## Verification Plan
1. Script an automated check confirming the SVG logo and the footer links were accurately replaced globally.
2. Manually test navigation routes, ensuring no dead ends or broken paths exist.
3. Verify the `index.html` counting animation functions upon page load.
4. Interact with the multi-step forms, verifying input validation and logic flow.
5. Instantiate an admin account, then manipulate and test data queues across `customers.html` and `applications.html` to confirm proper synchronization.
