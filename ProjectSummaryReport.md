<div align="center">

# 📑 Project Summary Report: Student Feedback Analyzer

![Problem Statement](https://img.shields.io/badge/Problem_Statement-PS_No._83-blue?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Association](https://img.shields.io/badge/In_Association_With-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Submission](https://img.shields.io/badge/GitHub-Ready-2EA44F?style=for-the-badge&logo=github&logoColor=white)

*Comprehensive technical overview, requirement verification, and GitHub submission documentation.*

</div>

---

## 👨‍💻 Student & Academic Information

| Field | Details |
| :--- | :--- |
| **👤 Student Name** | **Pranav Baghel** |
| **🏫 Section** | `BE-CSE-C-1-26-1-N` |
| **🆔 ERP Number** | `RU-26-00994` |
| **🎓 Program** | B.Tech in Computer Science & Engineering *(in association with **Google**)* |
| **🏛️ University** | Rungta International Skills University *(School of CSE)* |
| **📅 Semester** | First Semester |
| **📌 Project Title** | Student Feedback Analyzer (`PS No. 83`) |

---

## 🎯 1. Executive Summary

The **Student Feedback Analyzer** is a lightweight, console-driven Python application engineered to transform raw student course feedback (`feedback.csv`) into structured, actionable insights. It automates data validation, filters corrupted entries, calculates rating averages and distributions, evaluates overall class sentiment polarity, and extracts the top recurring keywords from student comments.

---

## ⚙️ 2. System Architecture & Data Pipeline

```text
┌───────────────────┐     ┌──────────────────────┐     ┌─────────────────────────┐
│   feedback.csv    │ ──▶ │  Validation Engine   │ ──▶ │  Analytics & NLP Engine │
│  (Raw CSV Data)   │     │ • File Check (os)    │     │ • Mean & Rating Tiers   │
└───────────────────┘     │ • Int Range [1..5]   │     │ • Sentiment Polarity    │
                          │ • Row Warning Logs   │     │ • Regex + Stopwords     │
                          └──────────────────────┘     └────────────┬────────────┘
                                                                    │
                                                                    ▼
                                                       ┌─────────────────────────┐
                                                       │  Formatted CLI Report   │
                                                       │ • Stats & Top 3 Words   │
                                                       └─────────────────────────┘
```

### Core Processing Stages
1. **🛡️ Defensive File Verification:** Uses `os.path.exists()` to verify `feedback.csv` availability prior to execution, preventing unhandled runtime crashes.
2. **🧹 Row-Level Sanitization & Validation:**
   * Skips header lines and empty records cleanly.
   * Safely preserves multi-comma comments while extracting `StudentID` and `Rating`.
   * Enforces strict whole-number validation ($1 \le \text{Rating} \le 5$), logging descriptive row warnings for out-of-bounds or non-numeric entries.
3. **📊 Statistical & Sentiment Modeling:**
   * Computes exact arithmetic mean: $\text{Average} = \frac{\sum \text{Valid Ratings}}{\text{Valid Feedback Count}}$.
   * Categorizes feedback into three sentiment tiers:
     * 🟢 **Positive (`4–5`):** High student satisfaction
     * 🟡 **Neutral (`3`):** Moderate satisfaction
     * 🔴 **Negative (`1–2`):** Areas requiring improvement
4. **🔍 Natural Language Keyword Extraction:**
   * Tokenizes comments using regular expressions (`\b[a-zA-Z]+\b`) normalized to lowercase.
   * Removes common stop words (`and`, `but`, `the`, `is`, `a`, `of`, `too`).
   * Ranks the **Top 3 keywords** via `collections.Counter`, resolving frequency ties alphabetically.

---

## ✅ 3. Bare Minimum Requirements Compliance

| Requirement | Implementation Status | Technical Details |
| :--- | :---: | :--- |
| **Single-File Python 3 Solution** | ✅ Completed | Self-contained console script (`feedback_analyzer.py`). |
| **Missing File Exception Handling** | ✅ Completed | Displays a clear error message if `feedback.csv` is missing. |
| **Strict Rating Validation (`1–5`)** | ✅ Completed | Rejects decimals, strings, and numbers outside `[1, 5]` with row warnings. |
| **Statistical & Sentiment Metrics** | ✅ Completed | Outputs valid count, average, rating breakdown, sentiment %, and top 3 words. |
| **4-Scenario Test Case Verification** | ✅ Completed | Tested across normal, boundary, invalid, and sentiment scenarios. |

---

## 🧪 4. Test Case Verification Matrix

| Test Case | Input Scenario | Expected & Verified Output | Status |
| :--- | :--- | :--- | :---: |
| **TC-01: Normal Input** | Standard `feedback.csv` (6 valid rows) | Valid: `6` \| Avg: `3.83` \| Top 3: `great (3), notes (3), clear (2)` | ✅ Pass |
| **TC-02: Boundary Input** | Single-row dataset (`S1,5,Great`) | Valid: `1` \| Avg: `5.00` \| Positive: `100.00%` \| Top: `great (1)` | ✅ Pass |
| **TC-03: Invalid Input** | Invalid rows (`S7,6,Nice`, `S8,abc,Nice`) | Prints `Warning: Row X skipped...` and ignores corrupted records | ✅ Pass |
| **TC-04: Sentiment Split** | Standard `feedback.csv` (6 valid rows) | Positive: `4 (66.67%)` \| Neutral: `1 (16.67%)` \| Negative: `1 (16.67%)` | ✅ Pass |

---

## 🐙 5. GitHub Repository Structure & Submission Guide

In accordance with **Instruction Step 5** (*Upload code and report to GitHub*), the repository follows clean open-source documentation standards:

```text
📦 Student-Feedback-Analyzer
 ┣ 📜 feedback_analyzer.py   # Primary Python 3 source code
 ┣ 📊 feedback.csv           # Sample dataset for immediate testing
 ┣ 📘 README.md              # Main repository landing page & usage guide
 ┗ 📑 SUMMARY.md             # Executive project report & test matrix
```

### 📋 Pre-Submission Checklist
* [x] **Code Integrity:** Verified zero syntax errors and clean console formatting.
* [x] **Sample Dataset:** Included `feedback.csv` so evaluators can run the script immediately.
* [x] **Complete Documentation:** Added student details (**Pranav Baghel** | `BE-CSE-C-1-26-1-N` | `RU-26-00994`) across both `README.md` and `SUMMARY.md`.
* [x] **Repository Visibility:** Set repository to **Public** and verified all commits are pushed to `main`.

---

## 🚀 6. Key Takeaways & Future Enhancements

* **💡 Key Takeaways:** Demonstrates clean defensive programming, $O(N)$ frequency analysis using hash maps (`Counter`), and modular console reporting.
* **🔮 Future Scope:**
  * **Interactive CLI Menu:** Adding a user-driven menu loop to switch between *Summary*, *Sentiment*, and *Keyword* views dynamically.
  * **Graphical Charts:** Integrating `matplotlib` to generate visual bar charts for rating distributions.
  * **Batch CSV Support:** Allowing instructors to analyze multiple course feedback files simultaneously.

---

<div align="center">
  <sub>Submitted by <b>Pranav Baghel</b> (`RU-26-00994`) • B.Tech CSE (in association with Google) • Rungta International Skills University</sub>
</div>
