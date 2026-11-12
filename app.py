
import streamlit as st

st.set_page_config(
    page_title="Bizcash FICA Training",
    page_icon="🏦",
    layout="wide"
)

# -------------------------
# BIZCASH TRAINING PLATFORM
# -------------------------

st.title("🏦 Bizcash FICA & RMCP Training Platform")
st.caption("Employee Compliance Training | 2026")

st.sidebar.title("Training Menu")

section = st.sidebar.radio(
    "Select a section",
    [
        "Home",
        "FICA Fundamentals",
        "Customer Due Diligence",
        "Risk Management",
        "Bizcash Products",
        "Bizcash SCF Training",
        "Transaction Monitoring",
        "Targeted Financial Sanctions",
        "Knowledge Assessment",
        "Training Information"
    ]
)

# -------------------------
# HOME
# -------------------------

if section == "Home":

    st.header("Welcome to Bizcash Compliance Training")

    st.write("""
    Welcome to the Bizcash digital employee training platform.

    This platform is designed to help employees understand their
    responsibilities under the Financial Intelligence Centre Act (FICA),
    the  and Compliance Plan (RMCP), and applicable
    AML/CFT/CPF requirements.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Training Modules", "8")
    col2.metric("Assessment", "Available")
    col3.metric("Training Year", "2026")

    st.subheader("Your Training Objectives")

    st.markdown("""
    - Understand FICA obligations and employee responsibilities.
    - Identify and verify customers and beneficial owners.
    - Understand customer and transaction risk.
    - Recognise suspicious activities and red flags.
    - Understand Targeted Financial Sanctions (TFS).
    - Apply Bizcash and Bizcash SCF RMCP procedures.
    """)

    st.info("Please complete the training modules and knowledge assessment.")

# -------------------------
# FICA FUNDAMENTALS
# -------------------------

elif section == "FICA Fundamentals":

    st.header("Module 1: FICA Fundamentals")

    st.write("""
    The Financial Intelligence Centre Act (FICA) establishes measures
    aimed at combating money laundering, terrorist financing and
    proliferation financing.
    """)

    st.subheader("Why is FICA important?")

    st.markdown("""
    FICA assists businesses to:

    - Prevent money laundering.
    - Prevent terrorist financing.
    - Identify customers and beneficial owners.
    - Identify and manage financial crime risks.
    - Detect and report suspicious transactions.
    - Comply with regulatory obligations.
    """)

    st.subheader("Employee Responsibilities")

    st.warning("""
    Employees must follow the approved RMCP, complete required customer
    verification, identify unusual activities and escalate concerns to
    the Compliance Officer.
    """)

# -------------------------
# CUSTOMER DUE DILIGENCE
# -------------------------

elif section == "Customer Due Diligence":

    st.header("Module 2: Customer Due Diligence (CDD)")

    st.write("""
    Customer Due Diligence involves identifying and verifying customers,
    understanding their business activities and establishing the
    beneficial ownership structure.
    """)

    st.subheader("Important KYC Information")

    st.markdown("""
    - Customer identification and verification.
    - Nature and purpose of the business relationship.
    - Source of funds and source of wealth, where applicable.
    - Directors and authorised representatives.
    - Shareholding structure.
    - Ultimate Beneficial Owners (UBOs).
    - Politically Exposed Persons (PEPs).
    - Sanctions and adverse-media screening.
    - Customer risk classification.
    """)

    st.subheader("Beneficial Ownership")

    st.info("""
    Beneficial owners must be natural persons identified through the
    applicable ownership and control assessment.

    The ownership structure must be understood, including indirect
    ownership and dilution through intermediate entities.
    """)

    st.subheader("Enhanced Due Diligence")

    st.write("""
    Higher-risk customers may require additional information,
    supporting documents, further verification and more frequent
    monitoring in accordance with the RMCP.
    """)
    st.subheader("Practical KYC Requirements")

    st.markdown("""
    Employees must ensure that the following information is obtained
    and verified, where applicable:

    **Company and Close Corporation**
    - Current CIPC documents.
    - Identification documents of directors.
    - Proof of residential address for relevant individuals.
    - Company nature and purpose of the business relationship.
    - Shareholding structure and independent shareholding confirmation.
    - Ultimate Beneficial Owner (UBO) declaration.
    - Source of funds and source of wealth, where required.
    - Details of authorised representatives.

    **Trusts**
    - Original trust deed and any amendments.
    - Letters of Authority.
    - Details of trustees, founders and beneficiaries.
    - Identification and verification of relevant natural persons.
    - Understanding of the trust's ownership and control structure.

    **Beneficial Ownership**
    - UBOs must be natural persons.
    - Apply the applicable ownership and control assessment.
    - Use the dilution method to assess indirect ownership.
    - Consider the applicable 5% ownership threshold under PCC 59.
    - Identify individuals exercising effective control, where applicable.

    **Screening Requirements**
    - PEP and RCA screening.
    - Targeted Financial Sanctions (TFS) screening.
    - Adverse-media screening.
    - Investigate potential matches and escalate concerns.

    **Important**
    Incomplete or outdated KYC information must be followed up.
    Higher-risk customers may require additional information and
    Enhanced Due Diligence (EDD), in accordance with the RMCP.
    """)

    st.info("""
    Employees must not mark a customer as KYC compliant simply
    because documents have been received. The information must
    be reviewed, verified and assessed against the applicable
    FICA requirements and RMCP.
    """)


# -------------------------
# 
# -------------------------

elif section == "Risk Management":

    st.header("Module 3: Risk Management")

    st.write("""
    Bizcash applies a risk-based approach when onboarding customers
    and monitoring business relationships and transactions.
    """)

    st.subheader("Risk Factors")

    st.markdown("""
    - Product risk.
    - Identity risk.
    - Industry and sector risk.
    - Geographic risk.
    - Source of funds risk.
    - Related-party risk.
    - Screening risk.
    - Onboarding channel risk.
    - Customer behaviour risk.
    """)

    st.subheader("Risk-Based Approach")

    st.success("""
    The level of due diligence and ongoing monitoring must be
    appropriate to the identified risk.
    """)

    st.write("""
    Higher-risk relationships may require Enhanced Due Diligence (EDD),
    Compliance Officer involvement and senior management escalation
    in accordance with the RMCP.
    """)

# -------------------------
# BIZCASH PRODUCTS
# -------------------------

elif section == "Bizcash Products":

    st.header("Module 4: Bizcash Products")

    st.write("""
    Alternative Finance Solutions (Pty) Ltd trading as Bizcash
    provides finance solutions to businesses.
    """)

    products = {
        "Invoice Discounting": "Finance against qualifying invoices.",
        "Business Loans": "Funding provided to qualifying businesses.",
        "Overdraft Facilities": "Facilities allowing businesses access to funding.",
        "Term Loans": "Business finance repayable over an agreed term.",
        "Supply Chain Finance": "Finance arrangements supporting commercial supply chains."
    }

    for product, description in products.items():
        with st.expander(product):
            st.write(description)

    st.warning("""
    Employees must understand the customer's business, the purpose
    of the finance and whether the proposed transaction makes
    commercial sense.
    """)

    st.subheader("Product-Specific FICA Risks and Controls")

    product_controls = {
        "Invoice Discounting": [
            "Verify that the invoice is genuine and relates to an actual commercial transaction.",
            "Check the customer, debtor and beneficiary details.",
            "Look out for duplicate, inflated or altered invoices.",
            "Investigate unusual payment instructions or changes to bank accounts."
        ],
        "Business Loans": [
            "Understand the purpose of the loan and how the funds will be used.",
            "Assess whether the proposed use of funds is consistent with the customer's business.",
            "Consider the source of repayment and source of funds.",
            "Escalate unusual funding requests or unexplained third-party payments."
        ],
        "Overdraft Facilities": [
            "Understand the expected use of the overdraft facility.",
            "Monitor account activity against the customer's normal business operations.",
            "Investigate unusual deposits, withdrawals or third-party transactions.",
            "Escalate activity that is inconsistent with the customer's business profile."
        ],
        "Term Loans": [
            "Understand the purpose and intended use of the finance.",
            "Consider whether the loan amount is reasonable for the stated business purpose.",
            "Assess the source of repayment.",
            "Investigate unexplained changes in repayment arrangements."
        ]
    }

    for product, controls in product_controls.items():
        with st.expander(product):
            for control in controls:
                st.write("- " + control)

    st.info(
        "Employees must apply the relevant RMCP controls and escalate "
        "unusual activity or concerns to the Compliance Officer."
    )

# -------------------------
# BIZCASH SCF
# -------------------------

elif section == "Bizcash SCF Training":

    st.header("Module 5: Bizcash SCF")

    st.write("""
    Bizcash Financial Solutions (Pty) Ltd trading as Bizcash SCF
    provides Supply Chain Finance arrangements.
    """)

    st.subheader("How the SCF arrangement works")

    st.markdown("""
    1. The Buyer submits an invoice, quotation or purchase order.
    2. The Buyer nominates the Beneficiary.
    3. Bizcash verifies the Beneficiary.
    4. The underlying commercial transaction is assessed.
    5. A Transaction Risk Assessment is completed.
    6. Payment is made directly to the verified Beneficiary.
    7. The Buyer repays Bizcash in accordance with the arrangement.
    """)

    st.subheader("Three Risk Components")

    st.markdown("""
    **Buyer Risk:** Risk associated with the Buyer.

    **Beneficiary Risk:** Risk associated with the nominated Beneficiary.

    **Transaction Risk:** Risk associated with the underlying commercial
    transaction and the payment itself.
    """)

    st.error("""
    A high-risk rating in any one of these components results in an
    overall high SCF risk rating and requires Compliance Officer review
    and senior management approval before payment.
    """)

    st.subheader("Underlying Transaction Verification")

    st.markdown("""
    Employees must consider:

    - Authenticity of invoices, quotations and purchase orders.
    - Description, quantity and value of goods or services.
    - Whether the transaction makes commercial sense.
    - Whether the parties normally conduct this type of business.
    - Duplicate or altered supporting documents.
    - Unusual deviations from historical transactions.
    """)
    st.subheader("SCF Transaction Risk Assessment – Practical Process")

    st.markdown("""
    Every SCF transaction must be assessed before payment.
    Employees must consider the Buyer, the nominated Beneficiary
    and the underlying commercial transaction separately.

    **Step 1: Assess Buyer Risk**
    - Review the Buyer's existing KYC information and risk rating.
    - Consider the nature of the Buyer's business and normal trading activities.
    - Identify any unusual behaviour, changes in business activity or concerns.
    - Escalate any adverse findings or unexplained activity.

    **Step 2: Assess Beneficiary Risk**
    - Verify the identity and business details of the nominated Beneficiary.
    - Understand the Beneficiary's relationship with the Buyer.
    - Consider whether the Beneficiary is a related party.
    - Check for relevant PEP, sanctions and adverse-media concerns.
    - Investigate unusual or unexplained changes to Beneficiary details.

    **Step 3: Assess Transaction Risk**
    - Verify the underlying invoice, quotation or purchase order.
    - Confirm that the goods or services are consistent with the parties' businesses.
    - Assess whether the transaction value and commercial purpose make sense.
    - Look for duplicate, altered, inflated or fictitious supporting documents.
    - Identify unusual payment instructions or deviations from previous transactions.

    **Step 4: Determine the Overall SCF Risk Rating**
    - Assess and record the Buyer Risk, Beneficiary Risk and Transaction Risk separately.
    - Consider the findings of all three assessments when determining the overall risk.
    - A high-risk rating in any one component results in an overall high SCF risk rating.

    **Step 5: Escalation and Approval**
    - High-risk SCF transactions must be referred to the Compliance Officer for review.
    - Senior management approval is required before payment.
    - Any concerns must be documented and resolved in accordance with the RMCP.
    - Employees must not proceed with payment before the required review and approval.

    """)

    st.info("""
    Important: Completing the transaction assessment is not simply
    an administrative exercise. Employees must understand the
    commercial transaction, identify potential risks and ensure
    that the required approvals are obtained before payment.
    """)


    st.subheader("SCF Red Flags")

    st.markdown("""
    - Fictitious, duplicated or inflated invoices.
    - Possible collusion between parties.
    - Circular trading.
    - Undisclosed related-party Beneficiaries.
    - Payments to unrelated third parties.
    - New Beneficiaries introduced shortly before financing.
    - Refunds directed to a different bank account.
    - Repayments from unrelated third parties.
    """)

    # ------------------------------
    # SCF PRACTICAL CASE STUDY
    # ------------------------------

    st.subheader("SCF Practical Case Study")

    st.write("""
    **Scenario:**

    An existing Bizcash SCF Buyer requests financing of R450,000
    against an invoice for machinery parts.

    The Buyer has an established relationship with Bizcash, has
    completed KYC and has a low existing customer risk rating.

    During the transaction review, the following is identified:

    - The Beneficiary is being introduced for the first time.
    - The Buyer has not previously conducted business with this Beneficiary.
    - The invoice and purchase order contain matching descriptions and values.
    - The bank account provided for payment differs from the account
      reflected on the original supporting documentation.
    - No satisfactory explanation has been provided for the change.

    **Your task:** Assess the risks and decide whether the transaction
    can proceed.
    """)

    st.info("Complete all four questions and submit your answers.")

    with st.form("scf_case_study_form"):

        q1 = st.radio(
            "Question 1: How would you assess the Buyer's risk?",
            [
                "Low risk – the Buyer has an established relationship and completed KYC.",
                "High risk – every SCF transaction must automatically be high risk.",
                "No assessment is required."
            ],
            index=None
        )

        q2 = st.radio(
            "Question 2: What is the main Beneficiary risk?",
            [
                "There is no risk because the Buyer nominated the Beneficiary.",
                "High risk – the Beneficiary is new and has no established trading relationship with the Buyer.",
                "Low risk – the Beneficiary has supplied an invoice."
            ],
            index=None
        )

        q3 = st.radio(
            "Question 3: What is the main Transaction risk?",
            [
                "There is no risk because the invoice and purchase order match.",
                "High risk – the payment account differs from the original supporting documentation and remains unexplained.",
                "Low risk – the transaction value is R450,000."
            ],
            index=None
        )

        q4 = st.radio(
            "Question 4: What should happen before payment?",
            [
                "Proceed because the Buyer is already KYC compliant.",
                "Proceed and investigate the account change afterwards.",
                "Refer the transaction to the Compliance Officer, investigate the concerns and obtain the required senior management approval before payment."
            ],
            index=None
        )

        submitted = st.form_submit_button("Submit Assessment")

    if submitted:

        answers = [
            q1, q2, q3, q4
        ]

        correct_answers = [
            "Low risk – the Buyer has an established relationship and completed KYC.",
            "High risk – the Beneficiary is new and has no established trading relationship with the Buyer.",
            "High risk – the payment account differs from the original supporting documentation and remains unexplained.",
            "Refer the transaction to the Compliance Officer, investigate the concerns and obtain the required senior management approval before payment."
        ]

        explanations = [
            "The Buyer's existing KYC and established relationship support a low Buyer risk rating, subject to the current assessment.",
            "A newly introduced Beneficiary with no established trading relationship requires further investigation.",
            "The unexplained change in payment account is a significant transaction red flag.",
            "The high-risk findings must be escalated. Payment must not proceed before the required review and approval."
        ]

        if None in answers:
            st.warning("Please answer all four questions before submitting.")

        else:
            score = 0

            st.subheader("Assessment Results")

            for number, answer in enumerate(answers):
                if answer == correct_answers[number]:
                    score += 1
                    st.success(f"Question {number + 1}: Correct")
                else:
                    st.error(f"Question {number + 1}: Incorrect")

                st.write(explanations[number])

            st.write(f"**Your score: {score} / 4**")

            if score == 4:
                st.success("Excellent! You have correctly identified the SCF risks and escalation requirements.")
            elif score >= 2:
                st.warning("Good attempt. Review the explanations and revisit the SCF risk assessment process.")
            else:
                st.error("Further training is required. Please revisit the SCF training module.")

            st.info(
                "Remember: A high-risk rating in any one of the three "
                "SCF risk components results in an overall high SCF risk rating."
            )

# -------------------------
# TRANSACTION MONITORING
# -------------------------

elif section == "Transaction Monitoring":

    st.header("Module 6: Transaction Monitoring")

    st.write("""
    Employees must remain alert to unusual or suspicious customer
    activities and transactions.
    """)

    st.subheader("Examples of Red Flags")

    st.markdown("""
    - Transactions inconsistent with the customer's stated business.
    - Unexplained third-party payments.
    - Unusual changes in transaction volumes.
    - Transactions with no apparent commercial purpose.
    - Unexplained foreign counterparties.
    - Unusual connections to high-risk jurisdictions.
    - Transactions involving unrelated parties.
    """)

    st.warning("""
    Do not ignore unusual activity. Escalate concerns to the
    Compliance Officer in accordance with internal procedures.
    """)

# -------------------------
# TARGETED FINANCIAL SANCTIONS
# -------------------------

elif section == "Targeted Financial Sanctions":

    st.header("Module 7: Targeted Financial Sanctions (TFS)")

    st.write("""
    Employees must understand the importance of screening customers,
    beneficial owners and relevant parties against applicable
    sanctions lists.
    """)

    st.subheader("Employee Responsibilities")

    st.markdown("""
    - Ensure required screening is completed.
    - Review potential screening matches.
    - Escalate possible matches to the Compliance Officer.
    - Do not disregard possible matches without proper review.
    - Follow applicable freezing and reporting procedures.
    """)

    st.error("""
    Potential sanctions matches must be escalated immediately.
    Employees must not proceed with a transaction where a confirmed
    sanctions match requires the transaction to be stopped or assets
    frozen.
    """)

# -------------------------
# KNOWLEDGE ASSESSMENT
# -------------------------

elif section == "Knowledge Assessment":

    st.header("Module 8: Knowledge Assessment")

    st.write("Complete the following questions to test your understanding.")

    questions = [
        {
            "question": "What does CDD stand for?",
            "options": [
                "Customer Due Diligence",
                "Credit Document Details",
                "Customer Data Department"
            ],
            "answer": "Customer Due Diligence"
        },
        {
            "question": "Who must beneficial owners ultimately be?",
            "options": [
                "Companies",
                "Natural persons",
                "Financial institutions"
            ],
            "answer": "Natural persons"
        },
        {
            "question": "What should an employee do when suspicious activity is identified?",
            "options": [
                "Ignore it",
                "Approve the transaction",
                "Escalate it to the Compliance Officer"
            ],
            "answer": "Escalate it to the Compliance Officer"
        },
        {
            "question": "What are the three SCF risk components?",
            "options": [
                "Buyer, Beneficiary and Transaction Risk",
                "Product, Staff and Payment Risk",
                "Customer, Bank and Credit Risk"
            ],
            "answer": "Buyer, Beneficiary and Transaction Risk"
        },
        {
            "question": "What happens if any SCF risk component is high?",
            "options": [
                "Payment proceeds automatically",
                "Compliance Officer review and senior management approval are required before payment",
                "The risk is ignored"
            ],
            "answer": "Compliance Officer review and senior management approval are required before payment"
        },
        {
            "question": "What must an employee do with a potential sanctions match?",
            "options": [
                "Ignore the match",
                "Escalate it for review",
                "Delete the screening result"
            ],
            "answer": "Escalate it for review"
        }
    ]

    with st.form("assessment_form"):

        answers = []

        for i, q in enumerate(questions):
            st.markdown(f"**Question {i + 1}: {q['question']}**")

            answer = st.radio(
                "Select your answer",
                q["options"],
                key=f"question_{i}"
            )

            answers.append(answer)

        submitted = st.form_submit_button("Submit Assessment")

    if submitted:

        score = sum(
            answers[i] == questions[i]["answer"]
            for i in range(len(questions))
        )

        percentage = round((score / len(questions)) * 100)

        st.subheader("Assessment Results")

        st.metric("Your Score", f"{percentage}%")

        if percentage >= 80:
            st.success("Congratulations! You have passed the assessment.")
            st.balloons()
        else:
            st.error("You have not achieved the required 80%. Please review the training.")

        st.write(f"You scored {score} out of {len(questions)}.")

        for i, q in enumerate(questions):
            if answers[i] != q["answer"]:
                st.warning(
                    f"Question {i + 1}: Correct answer: {q['answer']}"
                )

        st.info("""
        Demonstration only: assessment results are not yet stored
        against individual employee profiles.
        """)

# -------------------------
# TRAINING INFORMATION
# -------------------------

elif section == "Training Information":

    st.header("Training Information")

    st.write("""
    The Bizcash RMCP training framework provides for:
    """)

    st.markdown("""
    - Annual FICA, AML, CFT, CPF and RMCP training.
    - Training for new employees before they commence their duties.
    - Training records to be retained for at least five years.
    - A monthly training calendar.
    - Quarterly question-and-answer sessions.
    """)

    st.subheader("Important")

    st.info("""
    This is an initial demonstration. The final platform will include
    employee logins, recorded assessment results, certificates and
    Compliance Officer reporting.
    """)

st.sidebar.divider()
st.sidebar.caption("Bizcash Compliance Training | Internal Demonstration")
