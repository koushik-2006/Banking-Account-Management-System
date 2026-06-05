from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

def create_report():
    doc_path = "BAMS_Project_Report.pdf"
    doc = SimpleDocTemplate(doc_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontSize=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=30
    )
    
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor("#2563EB"),
        spaceBefore=20,
        spaceAfter=12
    )
    
    body_style = styles['Normal']
    body_style.fontSize = 11
    body_style.leading = 14
    
    story = []

    # Title Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Banking Account Management System (BAMS)", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Comprehensive Project Report", styles['Heading2']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Version 1.0 | June 2026", styles['Normal']))
    story.append(Spacer(1, 3*inch))
    story.append(Paragraph("Submitted by: Koushik & Team", styles['Normal']))
    story.append(PageBreak())

    # Table of Contents (Manual)
    story.append(Paragraph("Table of Contents", heading_style))
    story.append(Paragraph("1. Abstract .................................... 3", body_style))
    story.append(Paragraph("2. Project Objectives .......................... 4", body_style))
    story.append(Paragraph("3. System Architecture ........................ 5", body_style))
    story.append(Paragraph("4. Database Schema ............................ 6", body_style))
    story.append(Paragraph("5. Module Description ......................... 7", body_style))
    story.append(Paragraph("6. Technology Stack .......................... 12", body_style))
    story.append(Paragraph("7. Testing & Quality Assurance ............... 13", body_style))
    story.append(Paragraph("8. Deployment & Hosting ...................... 14", body_style))
    story.append(Paragraph("9. Conclusion ................................ 15", body_style))
    story.append(PageBreak())

    # 1. Abstract
    story.append(Paragraph("1. Abstract", heading_style))
    story.append(Paragraph("""
    The Banking Account Management System (BAMS) is a state-of-the-art web application designed to digitize traditional banking operations. 
    The system provides a seamless experience for customers to manage their finances, including transfers, loans, and investments, 
    while offering a powerful administrative interface for bank officials to monitor transactions and manage accounts. 
    Built with modern web technologies, BAMS prioritizes security, responsiveness, and user engagement.
    """, body_style))
    story.append(Spacer(1, 12))

    # 2. Objectives
    story.append(Paragraph("2. Project Objectives", heading_style))
    story.append(Paragraph("The primary objectives of the BAMS project are:", body_style))
    objectives = [
        "To provide a secure and user-friendly digital banking platform.",
        "To implement modular banking operations like Fund Transfer, Loan Application, and Card Management.",
        "To build a robust Admin Panel for centralized monitoring and customer support.",
        "To ensure data integrity through a strictly defined SQL database schema.",
        "To deliver high-performance visual analytics for financial tracking."
    ]
    for obj in objectives:
        story.append(Paragraph(f"• {obj}", body_style))
    story.append(PageBreak())

    # 3. System Architecture
    story.append(Paragraph("3. System Architecture", heading_style))
    story.append(Paragraph("""
    BAMS follows a standard 3-tier architecture:
    1. Presentation Layer: Built using HTML5, Vanilla CSS3, and JavaScript (ES6).
    2. Business Logic Layer: Implemented with Spring Boot 3 framework for RESTful APIs.
    3. Data Layer: Utilizes JPA/Hibernate for object-relational mapping with a relational database.
    """, body_style))
    
    # 4. Database Schema
    story.append(Paragraph("4. Database Schema", heading_style))
    story.append(Paragraph("The core database entities include:", body_style))
    
    db_data = [
        ["Table Name", "Description"],
        ["Users", "Stores authentication and personal profile data"],
        ["Accounts", "Manages balances and account status"],
        ["Transactions", "Logs all financial movements (Audit Trail)"],
        ["Loans", "Tracks application, tenure, and repayment status"],
        ["Cards", "Virtual card settings, limits, and blocking status"],
        ["Deposits", "Investment details for Fixed Deposits"]
    ]
    
    t = Table(db_data, colWidths=[1.5*inch, 4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2563EB")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(t)
    story.append(PageBreak())

    # 5. Modules
    story.append(Paragraph("5. Module Description", heading_style))
    story.append(Paragraph("5.1 Customer Modules", styles['Heading3']))
    story.append(Paragraph("• Dashboard: Real-time asset overview and spending analytics.", body_style))
    story.append(Paragraph("• Transfer: NEFT, RTGS, and IMPS support with OTP security.", body_style))
    story.append(Paragraph("• Cards: 3D flip animation for virtual cards with limit management.", body_style))
    story.append(Paragraph("• Loans: Application hub with integrated EMI calculator.", body_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.2 Admin Modules", styles['Heading3']))
    story.append(Paragraph("• Admin Dashboard: System-wide KPI tracking (Users, Revenue).", body_style))
    story.append(Paragraph("• Account Management: Activate, deactivate, and search customers.", body_style))
    story.append(Paragraph("• Global Audit: Real-time monitoring of all financial activity.", body_style))

    # 9. Conclusion
    story.append(PageBreak())
    story.append(Paragraph("9. Conclusion", heading_style))
    story.append(Paragraph("""
    BAMS successfully fulfills the requirement for a modern digital banking solution. 
    By integrating advanced UI features with a secure backend architecture, the project provides a 
    comprehensive template for educational and commercial banking systems.
    """, body_style))

    doc.build(story)
    print(f"Generated: {doc_path}")

if __name__ == "__main__":
    create_report()
