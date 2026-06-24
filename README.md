# 🏛️ Statutory Clause Engine: India DPDP Act 2023

A deterministic Python-based compliance engine that translates rigid legal clauses from India's Digital Personal Data Protection (DPDP) Act 2023 into strict, executable programmatic logic. 

## 💼 Why This Matters to Clients
Ambiguous legal text creates operational bottlenecks. This prototype demonstrates how corporate legal compliance and data governance can be automated. It instantly flags financial liabilities and mandatory workflows based on business variables (user age, breach status, etc.), reducing human error and assessment times.

---

## 🚀 Key Features Evaluated
* **Section 9 (Child Data):** Automatically triggers strict compliance pathways, parental consent workflows, and bars behavioral tracking if the user is a minor.
* **Section 8 (Breach Notification):** Evaluates active data breaches and calculates statutory reporting obligations to the Data Protection Board.
* **Financial Risk Modeling:** Computes worst-case financial liabilities (up to ₹250 Crore) based on the specific compliance failures detected.

---

## 🛠️ How to Run the Prototype

### Prerequisites
Make sure you have Python installed on your system. 

### Execution Steps
1. **Clone or Download the script:**
   Download the `dpdp_engine.py` file to your machine.

2. **Open your Terminal / Command Prompt** and navigate to the folder where the file is saved:
```bash
   cd Path/To/Your/Folder

Run the engine:

Bash
   python dpdp_engine.py
(Note: Use python3 dpdp_engine.py if you are on a Mac).

Interact with the CLI: Answer the prompts to generate a real-time compliance posture report.

📋 Sample Terminal Output
Plaintext
==================================================
📊 COMPLIANCE & LIABILITY REPORT
==================================================

--- CHILD DATA ASSESSMENT ---
❌ STRICT COMPLIANCE REQUIRED: Data Principal is a minor.
   - Action 1: Obtain verifiable parental consent.
   - Action 2: Disable all behavioral monitoring.
   - Liability Risk: Up to ₹200 Crore for non-compliance.
⚖️ Disclaimer
This software is a prototype designed to demonstrate programmatic logic mapping for legal frameworks. It does not constitute formal legal advice.
