import re

content = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Dashboard | Easy pAy</title>
    <link rel="stylesheet" href="css/variables.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="js/api.js"></script>
</head>

<body class="dashboard-body">
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <a href="index.html" class="logo-container" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
  <div style="width:38px;height:38px;border-radius:9px;background:#C9A84C;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
    <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <rect x="2" y="14" width="4" height="6" rx="1" fill="#0A0A0A"/>
      <rect x="9" y="9" width="4" height="11" rx="1" fill="#0A0A0A"/>
      <rect x="16" y="4" width="4" height="16" rx="1" fill="#0A0A0A"/>
      <rect x="2" y="13" width="18" height="1.5" rx="0.5" fill="#0A0A0A" opacity="0.4"/>
    </svg>
  </div>
  <span style="font-size:21px;font-weight:700;font-family:'Georgia',serif;letter-spacing:0.5px;color:#C9A84C;line-height:1;">Easy <span style="color:#FFD700;">pAy</span></span>
</a>
        </div>
        <nav class="sidebar-nav">
            <a href="dashboard.html" class="sidebar-link active"><span class="icon">📊</span> Dashboard</a>
            <a href="account.html" class="sidebar-link"><span class="icon">💳</span> Account Overview</a>
            <a href="transactions.html" class="sidebar-link"><span class="icon">💸</span> Transactions</a>
            <a href="transfer.html" class="sidebar-link"><span class="icon">🔄</span> Transfer Money</a>
            <a href="loans.html" class="sidebar-link"><span class="icon">🏦</span> Loans</a>
            <a href="cards.html" class="sidebar-link"><span class="icon">🃏</span> My Cards</a>
            <a href="my-applications.html" class="sidebar-link"><span class="icon">📄</span> My Applications</a>
            <hr class="sidebar-divider">
            <a href="profile.html" class="sidebar-link"><span class="icon">👤</span> Profile</a>
            <a href="notifications.html" class="sidebar-link"><span class="icon">🔔</span> Notifications <span
                    class="badge" id="notifBadge">3</span></a>
            <a href="#" onclick="logout(); return false;" class="sidebar-link logout-link"><span class="icon">🚪</span> Logout</a>
        </nav>
    </aside>

    <!-- Main Content -->
    <main class="dashboard-main">
        <!-- Top Navbar -->
        <header class="dashboard-topbar">
            <div class="topbar-left">
                <button class="menu-toggle" id="menuToggle">☰</button>
                <h1 class="welcome-text">Welcome back, <span class="user-welcome-name"></span></h1>
            </div>
            <div class="topbar-right">
                <div class="topbar-info">"""

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find where `<div class="topbar-info">` is in the broken text
idx = text.find('<div class="topbar-info">')
if idx != -1:
    new_text = content + text[idx + len('<div class="topbar-info">'):]
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed!")
else:
    print("Not found")

