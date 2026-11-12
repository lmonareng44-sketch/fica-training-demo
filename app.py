
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
st.caption("Employee Compliance Training | 2027")

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
        "2027 Monthly Training Programme",
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

    
        "questions": [
                {
                    "question": "What is the primary purpose of FICA?",
                    "options": [
                        "To regulate the pricing of business loans.",
                        "To combat money laundering, terrorist financing and proliferation financing.",
                        "To regulate employee performance."
                    ],
                    "answer": "To combat money laundering, terrorist financing and proliferation financing.",
                    "explanation": "FICA establishes measures to help prevent and combat financial crime."
                },
                {
                    "question": "What is an employee expected to do when identifying a possible FICA concern?",
                    "options": [
                        "Ignore it if the customer is already known.",
                        "Escalate the concern in accordance with the RMCP.",
                        "Wait until the next annual review."
                    ],
                    "answer": "Escalate the concern in accordance with the RMCP.",
                    "explanation": "Employees must identify and escalate concerns rather than ignore unusual activity."
                },
                {
                    "question": "Does an existing customer relationship remove the need to monitor customer activity?",
                    "options": [
                        "Yes, once KYC is complete no further monitoring is needed.",
                        "No, ongoing monitoring remains necessary.",
                        "Yes, provided the customer has a low risk rating."
                    ],
                    "answer": "No, ongoing monitoring remains necessary.",
                    "explanation": "KYC compliance does not remove the obligation to monitor customer behaviour and transactions."
                },
                {
                    "question": "What is the role of the Compliance Officer?",
                    "options": [
                        "To review and oversee compliance matters and applicable reporting obligations.",
                        "To approve every commercial transaction.",
                        "To replace the responsibilities of all employees."
                    ],
                    "answer": "To review and oversee compliance matters and applicable reporting obligations.",
                    "explanation": "The Compliance Officer oversees the organisation's FICA compliance framework and relevant escalation and reporting processes."
                },
                {
                    "question": "An employee notices that a customer's stated business activities do not match the information provided. What should happen?",
                    "options": [
                        "Continue processing because the customer has submitted a KYC form.",
                        "Ignore the discrepancy unless a payment fails.",
                        "Investigate and escalate the concern in accordance with the RMCP."
                    ],
                    "answer": "Investigate and escalate the concern in accordance with the RMCP.",
                    "explanation": "Inconsistencies must be reviewed and escalated where necessary. Employees must not ignore potential risk indicators."
                }
            ]

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


elif section == "2027 Monthly Training Programme":

    st.header("2027 Monthly FICA Training Programme")

    st.write("""
    Monthly employee compliance training for Bizcash and Bizcash SCF.
    Each month focuses on a different aspect of FICA, AML/CFT/CPF,
    the RMCP and practical compliance responsibilities.
    """)

    monthly_topics = {
        "January 2027": {
            "topic": "FICA Fundamentals and Employee Responsibilities",
            "focus": [
                "Purpose and objectives of FICA.",
                "Employee responsibilities under the FICA Act and the RMCP.",
                "Accountability of employees for identifying and escalating concerns.",
                "Understanding the roles of the Compliance Officer and senior management."
            ],
            "scenario": "An employee notices that information supplied by a customer does not match the company's known business activities. The employee must raise the concern rather than ignore it.",
            "questions": [
                {
                    "question": "What is the main purpose of FICA?",
                    "options": [
                        "To regulate business profits.",
                        "To combat money laundering, terrorist financing and proliferation financing.",
                        "To regulate employee salaries."
                    ],
                    "answer": "To combat money laundering, terrorist financing and proliferation financing.",
                    "explanation": "FICA helps prevent and combat financial crime."
                },
                {
                    "question": "What must an employee do when they identify suspicious customer activity?",
                    "options": [
                        "Ignore it if the customer is known.",
                        "Report and escalate the concern in accordance with the RMCP.",
                        "Wait until the next annual review."
                    ],
                    "answer": "Report and escalate the concern in accordance with the RMCP.",
                    "explanation": "Employees must identify and escalate concerns rather than ignore unusual activity."
                },
                {
                    "question": "Does an existing customer relationship remove the need for ongoing monitoring?",
                    "options": [
                        "Yes, once KYC is complete, monitoring is no longer required.",
                        "No, ongoing monitoring remains necessary.",
                        "Only high-value customers must be monitored."
                    ],
                    "answer": "No, ongoing monitoring remains necessary.",
                    "explanation": "Customer activity must continue to be monitored throughout the business relationship."
                },
                {
                    "question": "Who is responsible for following the company's RMCP?",
                    "options": [
                        "Only the Compliance Officer.",
                        "Only senior management.",
                        "All employees, according to their responsibilities."
                    ],
                    "answer": "All employees, according to their responsibilities.",
                    "explanation": "FICA compliance is a responsibility shared across the business."
                },
                {
                    "question": "What should an employee do if information supplied by a customer does not match the known nature of the business?",
                    "options": [
                        "Continue processing without raising the issue.",
                        "Raise the concern and escalate it in accordance with the RMCP.",
                        "Automatically reject the customer."
                    ],
                    "answer": "Raise the concern and escalate it in accordance with the RMCP.",
                    "explanation": "Unusual or inconsistent information must be investigated and escalated."
                }
            ]
        },

        "February 2027": {
            "topic": "Customer Due Diligence (CDD)",
            "focus": [
                "Identifying and verifying customers.",
                "Understanding the nature and purpose of the business relationship.",
                "Identifying directors, representatives and authorised persons.",
                "Obtaining and reviewing supporting documentation."
            ],
            "scenario": "A company submits a KYC form but does not provide current CIPC information or identification documents for its directors.",
            "question": "What is the appropriate approach?",
            "options": [
                "Treat the customer as compliant because a KYC form was received.",
                "Identify and obtain the outstanding verification information.",
                "Accept verbal confirmation instead."
            ],
            "answer": "Identify and obtain the outstanding verification information.",
            "explanation": "CDD requires appropriate identification and verification measures."
        },

        "March 2027": {
            "topic": "Ultimate Beneficial Ownership (UBO)",
            "focus": [
                "Understanding direct and indirect ownership.",
                "Applying the look-through and dilution method.",
                "Identifying natural persons who ultimately own or control a customer.",
                "Reviewing trusts, shareholders and complex ownership structures."
            ],
            "scenario": "A company is owned through two intermediate companies. Employees must look through the ownership structure to identify the ultimate natural persons.",
            "question": "Who can ultimately qualify as a beneficial owner?",
            "options": [
                "Only the company listed as the immediate shareholder.",
                "A natural person who ultimately owns or exercises effective control.",
                "Any employee of the customer."
            ],
            "answer": "A natural person who ultimately owns or exercises effective control.",
            "explanation": "UBO identification requires looking through ownership and control structures to the relevant natural persons."
        },

        "April 2027": {
            "topic": "PEPs, Sanctions and Adverse Media",
            "focus": [
                "Understanding domestic and foreign politically exposed persons.",
                "Identifying family members and known close associates where relevant.",
                "Understanding targeted financial sanctions (TFS).",
                "Reviewing adverse media and escalating potential matches."
            ],
            "scenario": "Screening identifies a possible PEP match involving a director. Employees must establish whether the match is genuine and follow the applicable risk-based procedures.",
            "question": "What should happen when a potential sanctions match is identified?",
            "options": [
                "Ignore it if the customer has a low risk rating.",
                "Escalate and investigate the potential match in accordance with the RMCP.",
                "Automatically treat every similar name as a confirmed match."
            ],
            "answer": "Escalate and investigate the potential match in accordance with the RMCP.",
            "explanation": "Potential matches must be investigated and handled in accordance with applicable TFS obligations and the RMCP."
        },

        "May 2027": {
            "topic": "Risk-Based Approach and Enhanced Due Diligence",
            "focus": [
                "Understanding customer risk factors.",
                "Applying customer risk ratings.",
                "Identifying circumstances requiring Enhanced Due Diligence (EDD).",
                "Applying appropriate ongoing monitoring and escalation."
            ],
            "scenario": "A customer operates in a higher-risk sector and has an unusual ownership structure. Additional information may be required before proceeding.",
            "question": "What determines the level of due diligence required?",
            "options": [
                "The identified money laundering and terrorist financing risks.",
                "The customer's preference.",
                "The amount of time available to process the application."
            ],
            "answer": "The identified money laundering and terrorist financing risks.",
            "explanation": "The extent of CDD, EDD and ongoing monitoring must be proportionate to the identified risk."
        },

        "June 2027": {
            "topic": "Source of Funds and Source of Wealth",
            "focus": [
                "Distinguishing source of funds from source of wealth.",
                "Understanding the customer's business income and funding arrangements.",
                "Identifying unexplained third-party funding.",
                "Obtaining supporting information where required by the risk assessment."
            ],
            "scenario": "A business requests finance but the proposed funding arrangement involves payments from an unrelated third party without a reasonable explanation.",
            "question": "What is the appropriate response?",
            "options": [
                "Accept the arrangement without further review.",
                "Investigate the source and purpose of the funds and escalate concerns.",
                "Assume the payment is legitimate because it comes from a bank account."
            ],
            "answer": "Investigate the source and purpose of the funds and escalate concerns.",
            "explanation": "Unexplained third-party funding must be considered and investigated in accordance with the RMCP."
        },

        "July 2027": {
            "topic": "Transaction Monitoring and Suspicious Activity",
            "focus": [
                "Identifying transactions inconsistent with the customer's business.",
                "Recognising unusual deposits, withdrawals and payment patterns.",
                "Identifying unexplained third-party payments.",
                "Escalating suspicious or unusual activity."
            ],
            "scenario": "A customer whose normal business activity involves local trading suddenly receives unexplained payments from unrelated parties.",
            "question": "What should the employee do?",
            "options": [
                "Ignore the activity because the customer is KYC compliant.",
                "Escalate the unusual activity for investigation.",
                "Wait until the customer requests another facility."
            ],
            "answer": "Escalate the unusual activity for investigation.",
            "explanation": "KYC compliance does not remove the requirement for ongoing transaction monitoring."
        },

        "August 2027": {
            "topic": "Bizcash Products and Product-Specific FICA Risks",
            "focus": [
                "Understanding Invoice Discounting, Business Loans and Term Loans.",
                "Understanding overdraft facilities and expected account activity.",
                "Assessing the purpose and intended use of finance.",
                "Identifying unusual payment instructions and third-party transactions."
            ],
            "scenario": "A business requests invoice discounting against an invoice that appears inconsistent with its normal trading activities.",
            "question": "What should employees consider?",
            "options": [
                "Only whether the customer has completed KYC.",
                "Whether the invoice is genuine and the transaction makes commercial sense.",
                "Only whether the finance amount is approved."
            ],
            "answer": "Whether the invoice is genuine and the transaction makes commercial sense.",
            "explanation": "Employees must understand the customer's business and assess the underlying commercial transaction."
        },

        "September 2027": {
            "topic": "Bizcash SCF and Transaction Risk Assessment",
            "focus": [
                "Understanding Buyer Risk, Beneficiary Risk and Transaction Risk.",
                "Verifying the nominated Beneficiary.",
                "Checking invoices, quotations and purchase orders.",
                "Understanding escalation and senior management approval requirements."
            ],
            "scenario": "An existing Buyer nominates a new Beneficiary and requests payment into a bank account different from the account reflected in the original supporting documentation.",
            "question": "What should happen before payment?",
            "options": [
                "Proceed because the Buyer is already KYC compliant.",
                "Investigate the change and obtain the required review and approval.",
                "Proceed and investigate afterwards."
            ],
            "answer": "Investigate the change and obtain the required review and approval.",
            "explanation": "A high-risk finding in any SCF risk component requires Compliance Officer review and senior management approval before payment."
        },

        "October 2027": {
            "topic": "Targeted Financial Sanctions and Proliferation Financing",
            "focus": [
                "Understanding TFS screening obligations.",
                "Recognising potential proliferation financing risks.",
                "Understanding dual-use goods and relevant trade risks.",
                "Escalating potential matches and concerns."
            ],
            "scenario": "A transaction involves goods that may have dual-use applications and a counterparty connected to a higher-risk jurisdiction.",
            "question": "What is the appropriate approach?",
            "options": [
                "Ignore the concern because the transaction is commercial.",
                "Assess the relevant risks, conduct required screening and escalate concerns.",
                "Proceed without additional checks if the invoice is genuine."
            ],
            "answer": "Assess the relevant risks, conduct required screening and escalate concerns.",
            "explanation": "Commercial transactions must still be assessed for relevant sanctions and proliferation financing risks."
        },

        "November 2027": {
            "topic": "FIC Reporting, goAML and Record Keeping",
            "focus": [
                "Understanding internal suspicious activity escalation.",
                "Understanding the Compliance Officer's reporting responsibilities.",
                "Recognising when suspicious and other reportable transactions may arise.",
                "Maintaining records in accordance with the RMCP and applicable requirements."
            ],
            "scenario": "An employee identifies suspicious activity during a customer review and receives additional information supporting the concern.",
            "question": "What should the employee do?",
            "options": [
                "Discuss the suspicion with the customer.",
                "Escalate the concern internally to the Compliance Officer.",
                "Delete the information if the transaction has already taken place."
            ],
            "answer": "Escalate the concern internally to the Compliance Officer.",
            "explanation": "Employees must follow internal escalation procedures. Reporting decisions are handled by the authorised responsible person."
        },

        "December 2027": {
            "topic": "RMCP Review, Compliance Accountability and Annual Refresher",
            "focus": [
                "Reviewing key RMCP requirements.",
                "Understanding employee responsibilities and escalation procedures.",
                "Revisiting customer and transaction risk assessments.",
                "Identifying lessons learned and areas requiring further training."
            ],
            "scenario": "An employee discovers that a customer risk profile has changed since onboarding, but the customer has not yet been reassessed.",
            "question": "What should happen?",
            "options": [
                "Retain the original rating indefinitely.",
                "Review the changed circumstances and update the risk assessment where required.",
                "Wait until the next annual training session."
            ],
            "answer": "Review the changed circumstances and update the risk assessment where required.",
            "explanation": "Customer risk profiles and ongoing monitoring must be reviewed when relevant circumstances change."
        }
    }

    selected_month = st.selectbox(
        "Select monthly training session",
        list(monthly_topics.keys())
    )

    training = monthly_topics[selected_month]

    st.subheader(training["topic"])

    st.markdown("### Monthly Training Focus")
    for item in training["focus"]:
        st.markdown(f"- {item}")

    st.markdown("### Practical Bizcash Scenario")
    st.info(training["scenario"])


        st.markdown("### Monthly Knowledge Assessment")

        answers = {}

        for i, question in enumerate(training["questions"], start=1):
            st.markdown(f"**Question {i}: {question['question']}**")

            answers[i] = st.radio(
                "Select your answer:",
                question["options"],
                index=None,
                key=f"answer_{selected_month}_{i}"
            )

        if st.button("Submit Monthly Assessment", key=f"submit_{selected_month}"):

            if any(answer is None for answer in answers.values()):
                st.warning("Please answer all five questions before submitting.")

            else:
                score = 0

                st.markdown("### Assessment Results")

                for i, question in enumerate(training["questions"], start=1):

                    if answers[i] == question["answer"]:
                        score += 1
                        st.success(f"Question {i}: Correct")
                    else:
                        st.error(f"Question {i}: Incorrect")

                    st.info(question["explanation"])

                st.write(f"**Your score: {score} / 5**")

                if score >= 4:
                    st.success("Congratulations! You have passed this month's assessment.")
                else:
                    st.warning("You have not achieved the required 80%. Please review the training and try again.")


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
