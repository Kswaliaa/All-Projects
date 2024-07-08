

# Bank Loan Portfolio Assessment
---

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Data Source](#data-source)
- [Methodology](#methodology)
- [Key Insights and Findings](#key-insights-and-findings)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Future Work](#future-work)
- [Principal Visualizations](#principal-visualizations)
- [Data Visualization Interfaces](#data-visualization-interfaces)
- [Terminologies Used in Data](#terminologies-used-in-data)
- [Getting Started](#getting-started)
- [Contribution](#contribution)
- [Conclusion](#conclusion)
- [MIT License](#mit-license)

## Project Overview

This project undertakes a comprehensive analysis of bank loan data, leveraging SQL for robust data querying and manipulation. The analysis is complemented by advanced visualization and further exploration using Power BI, Excel, and Tableau. The primary objective is to extract actionable insights concerning loan applications, funding, repayments, and borrower demographics. The analysis spans various dimensions, including temporal (monthly trends, loan terms), geographical (state-level analysis), and categorical aspects (loan purposes, home ownership).

---

## Objectives

- Provide a comprehensive assessment of the bank's loan portfolio performance, identifying strengths and areas for improvement.
- Discover trends and patterns in loan applications, approval rates, and repayment statuses to optimize lending strategies.
- Evaluate financial health indicators such as Total Funded Amount, Average Interest Rate, and Loan Status to gauge portfolio stability and profitability.
- Support strategic decision-making for enhancing the bank's credit and loan offerings, ensuring alignment with market demands and customer needs.

---


## Methodology

Our approach to analyzing the bank loan data involved a multi-step, systematic process designed to ensure thorough data examination and insightful visualization. Below, we outline each stage of our methodology:

### Data Ingestion and Database Creation:

- **Objective**: Establish a robust foundation for data storage and retrieval.
- **Process**: A relational database was created in Microsoft SQL Server to store comprehensive loan data, ensuring data integrity and accessibility.

### Data Analysis and SQL Queries:

- **Objective**: Extract meaningful insights and key performance indicators (KPIs).
- **Process**: SQL queries were meticulously developed to retrieve essential KPIs, including total and monthly loan applications, funded amounts, and average interest rates. This step facilitated the identification of critical trends and performance metrics.

### Data Processing in Excel:

- **Objective**: Perform initial data cleaning and preliminary analysis.
- **Process**: The dataset underwent further cleaning and processing in Excel, which included data validation and the generation of preliminary insights. This step ensured the accuracy and reliability of the data before more advanced analysis.

### Categorization of Loans:

- **Objective**: Classify loans based on repayment performance.
- **Process**: Loans were categorized into 'Good' or 'Bad' based on their repayment status. This classification provided a clear distinction between performing and non-performing loans, which is crucial for risk assessment and management.

### Temporal and Categorical Analysis:

- **Objective**: Examine the data across various dimensions and time frames.
- **Process**: Detailed analysis was conducted based on multiple factors, including issue month, state, loan term, employee length, loan purpose, and home ownership status. This multifaceted analysis enabled a comprehensive understanding of the factors influencing loan performance.

### Visualization:

- **Objective**: Transform data into actionable visual insights.
- **Process**: The results from the SQL queries were visualized using Power BI, Excel, and Tableau. These visualizations were designed to ensure data consistency and to provide a clear, graphical representation of the findings. This step was critical for communicating insights effectively to stakeholders.

---


## Key Insights and Findings

- **Total Loan Applications**: Detailed breakdown of total loan applications, including distinctions between Month-To-Date (MTD) and Previous Month-To-Date (PMTD) applications, providing insights into monthly application trends.

- **Total Funded Amount vs. Amounts Received**: Analysis of the bank's liquidity and loan performance, comparing total funded amounts with actual amounts received, highlighting discrepancies and potential financial adjustments.

- **Average Interest Rate and DTI (Debt-to-Income Ratio)**: Examination of borrower financial health through average interest rates and DTI ratios, aiding in assessing borrowers' ability to manage debt obligations.

- **Loan Categorization**: Segmentation of loans into 'Good' and 'Bad' categories based on repayment status, offering a comprehensive view of the loan portfolio's risk profile and potential credit losses.

- **Detailed Breakdowns by Various Factors**: In-depth analysis by loan status, purpose, state, term, and other factors to identify underlying patterns and trends influencing loan performance and customer behavior.

---


## Tools and Technologies Used

- **SQL Management Server**: Used for database management, querying, and data analysis. SQL queries were crucial in extracting key metrics and insights from the loan dataset.
  
- **Excel**: Utilized for data cleaning, processing, and conducting preliminary analyses. Excel provided a platform for validating data integrity and performing initial calculations.

- **Power BI**: Employed for data visualization and dashboard creation. Power BI enabled the creation of interactive dashboards that visualize loan portfolio performance and trends.

- **Tableau**: Utilized for advanced data visualization and building interactive dashboards. Tableau's capabilities were leveraged to explore complex data relationships and provide deeper insights into loan analytics.

---

## Future Work

- **Predictive Modeling**: Implement machine learning models to forecast loan defaults based on historical data patterns and borrower characteristics.
  
- **Demographic Analysis**: Conduct detailed demographic studies to better understand customer segments and tailor loan products to specific market needs.
  
- **Impact of Loan Terms**: Perform deeper analyses on loan repayment rates based on different loan terms (e.g., short-term vs. long-term loans) to optimize loan structures and minimize default risks.

---


## Terminologies Used in Data

| **Field**               | **Purpose**                                                                                                                                          | **Use for Banks**                                                                                                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Loan ID**             | A unique identifier assigned to each loan application or account.                                                                                     | Efficiently manage and track loans throughout their lifecycle, organize loan records, monitor repayments, and address customer inquiries. |
| **Address State**       | Indicates the borrower's location.                                                                                                                   | Identify regional trends in loan demand, adjust marketing strategies, and manage risk portfolios based on geographic regions.            |
| **Employee Length**     | Provides insights into the borrower's employment stability.                                                                                           | Assess a borrower's ability to repay, as stable employment often translates to a lower default risk.                                     |
| **Employee Title**      | Specifies the borrower's occupation or job title.                                                                                                     | Verify income sources, assess the borrower's financial capacity, and tailor loan offers to different professions.                        |
| **Grade**               | Represents a risk classification assigned to the loan based on creditworthiness.                                                                      | Price loans and manage risk, with higher-grade loans typically receiving lower interest rates.                                           |
| **Sub Grade**           | Refines the risk assessment within a grade, providing additional risk differentiation.                                                                | Offer a finer level of risk assessment, helping banks tailor interest rates and lending terms to match borrower risk profiles.           |
| **Home Ownership**      | Indicates the borrower's housing status.                                                                                                              | Assess collateral availability and borrower stability, as homeowners may have lower default rates.                                       |
| **Issue Date**          | Marks the loan's origination date.                                                                                                                    | Track loan aging, calculate interest accruals, and manage loan portfolios.                                                               |
| **Last Credit Pull Date** | Records when the borrower's credit report was last accessed.                                                                                         | Track credit history updates, assess credit risk, and make informed lending decisions.                                                  |
| **Last Payment Date**   | Marks the most recent loan payment received.                                                                                                          | Assess payment behavior, calculate delinquency, and project future payments.                                                             |
| **Loan Status**         | Indicates the current state of the loan (e.g., fully paid, current, default).                                                                         | Monitor loan health, categorize loans for risk analysis, and determine provisioning requirements.                                        |
| **Next Payment Date**   | Estimates the date of the next loan payment.                                                                                                          | Assist in cash flow forecasting, liquidity planning, and revenue projection from loan portfolios.                                        |
| **Purpose**             | Specifies the reason for the loan (e.g., debt consolidation, education).                                                                              | Segment and customize loan offerings, aligning loan terms with borrower needs.                                                           |
| **Term**                | Defines the duration of the loan in months.                                                                                                           | Structure loan agreements, calculate interest payments, and manage loan maturities.                                                      |
| **Verification Status** | Indicates whether the borrower's financial information has been verified.                                                                             | Gauge data reliability, verify income, and evaluate loan application credibility.                                                        |
| **Annual Income**       | Reflects the borrower's total yearly earnings.                                                                                                        | Determine loan eligibility, calculate debt-to-income ratios, and evaluate creditworthiness.                                              |
| **DTI (Debt-to-Income Ratio)** | Measures the borrower's debt burden relative to income.                                                                                     | Assess a borrower's ability to handle loan payments and make responsible lending decisions.                                              |
| **Instalment**          | The fixed monthly payment amount for loan repayment, including principal and interest.                                                                | Structure loan terms, calculate amortization schedules, and assess payment affordability.                                                |
| **Interest Rate**       | Represents the annual cost of borrowing expressed as a percentage.                                                                                    | Price loans, manage profit margins, and attract investors.                                                                               |
| **Loan Amount**         | The total borrowed sum, defining the principal amount.                                                                                                | Determine loan size and manage financial exposure.                                                                                       |


---

## Getting Started

### Prerequisites

- **SQL Management Server**: To manage and query the database.
- **Excel**: For data processing and analysis.
- **Power BI Desktop**: For creating and viewing dashboards.
- **Tableau Desktop**: For advanced data visualization and interactive dashboards.



## Conclusion

This project has provided valuable insights into the bank's loan portfolio, highlighting trends in loan applications, funding, repayment statuses, and borrower demographics. Through rigorous data analysis using SQL, Excel, Power BI, and Tableau, actionable insights have been uncovered that can inform strategic decision-making within the organization.

The visualizations and findings presented in the Power BI and Tableau dashboards offer a clear understanding of the loan portfolio's performance and risk profiles. Moving forward, these insights will guide in optimizing loan offerings, improving financial health assessments, and enhancing customer satisfaction.

Thank you for exploring the bank loan analysis project. We look forward to continuing to leverage data-driven approaches to drive business forward.

