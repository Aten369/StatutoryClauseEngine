# dpdp_engine.py

def evaluate_child_data_compliance(user_age):
    """Evaluates compliance requirements based on the user's age."""
    compliance_report = []
    
    if user_age < 18:
        compliance_report.append("❌ STRICT COMPLIANCE REQUIRED: Data Principal is a minor.")
        compliance_report.append("   - Action 1: Obtain verifiable parental consent.")
        compliance_report.append("   - Action 2: Disable all behavioral monitoring and targeted advertising.")
        compliance_report.append("   - Liability Risk: Up to ₹200 Crore for non-compliance.")
    else:
        compliance_report.append("✅ Standard consent mechanisms apply (Data Principal is 18+).")
        
    return "\n".join(compliance_report)

def evaluate_breach_protocol(breach_occurred, reported_to_board):
    """Evaluates obligations and liabilities in the event of a data breach."""
    compliance_report = []
    
    if breach_occurred:
        compliance_report.append("🚨 BREACH PROTOCOL TRIGGERED")
        if not reported_to_board:
            compliance_report.append("❌ URGENT: You must notify the Data Protection Board and affected users immediately.")
            compliance_report.append("   - Liability Risk (Failure to notify): Up to ₹200 Crore.")
            compliance_report.append("   - Liability Risk (Failure to prevent): Up to ₹250 Crore.")
        else:
            compliance_report.append("✅ Board notified. Ensure affected Data Principals are also informed.")
            compliance_report.append("   - Note: You may still face fines up to ₹250 Crore for failure to prevent the breach.")
    else:
        compliance_report.append("✅ No active breach. Maintain reasonable security safeguards to avoid ₹250 Crore penalties.")
        
    return "\n".join(compliance_report)
