# Technical Design Document (TDD)
## Credit Risk Assessment System

---

## 1. System Overview
The system is designed to process historical loan data, build a statistical credit risk model, and evaluate model performance to support credit decision-making.

---

## 2. Architecture Overview
- Data Input: CSV-based historical loan dataset
- Processing Layer: Python scripts for preprocessing and modeling
- Modeling Layer: Logistic Regression
- Validation Layer: Statistical performance metrics
- Output: Risk scores and evaluation metrics

---

## 3. Technology Stack
- Programming Language: Python
- Libraries:
  - Pandas
  - NumPy
  - Scikit-learn
- Development Environment: Jupyter Notebook / Python scripts

---

## 4. Data Preprocessing
- Missing value handling
- Feature selection
- Target variable encoding (loan_status)

---

## 5. Model Design
- Model Type: Logistic Regression
- Reason for Selection:
  - Interpretability
  - Industry acceptance for credit risk
  - Efficiency for binary classification problems

---

## 6. Training Approach
- Dataset split into training and testing sets
- Model trained using maximum likelihood estimation
- Hyperparameters tuned for convergence stability

---

## 7. Assumptions
- Historical data is representative of future behavior
- Input data quality is reliable
- Binary classification is sufficient for risk assessment

---
