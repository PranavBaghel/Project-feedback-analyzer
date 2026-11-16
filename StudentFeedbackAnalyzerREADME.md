<div align="center">

# 📊 Student Feedback Analyzer

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Google](https://img.shields.io/badge/Association-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge)

*A smart console-based Python utility to validate, analyze, and extract sentiment & keyword insights from student feedback data.*

</div>

---

## 👨‍💻 Student & Academic Profile

| Attribute | Details |
| :--- | :--- |
| **👤 Student Name** | **Pranav Baghel** |
| **🏫 Section** | `BE-CSE-C-1-26-1-N` |
| **🆔 ERP Number** | `RU-26-00994` |
| **🎓 Program** | B.Tech in Computer Science & Engineering *(in association with **Google**)* |
| **🏛️ University** | Rungta International Skills University *(School of CSE)* |
| **📅 Semester** | First Semester |
| **📌 Problem Statement** | **PS No. 83** — Student Feedback Analyzer |

---

## 🎯 Project Overview

The **Student Feedback Analyzer** processes raw student feedback stored in a CSV file (`feedback.csv`) and turns it into actionable metrics. Built with robustness in mind, it filters out corrupted or invalid entries, computes rating distributions, evaluates overall class sentiment, and performs natural language frequency analysis on student comments.

---

## ✨ Key Features

* 🛡️ **Strict Data Validation & Error Handling**
  * Verifies file existence (`feedback.csv`) prior to execution.
  * Ensures ratings are strictly whole numbers between `1` and `5`.
  * Gracefully skips malformed rows or non-numeric ratings with descriptive row-level warnings.
* 📈 **Comprehensive Rating Metrics**
  * Tallies total valid feedback submissions.
  * Calculates the exact average rating (formatted to 2 decimal places).
  * Displays a complete tier breakdown from `5 ★` down to `1 ★`.
* 💬 **Sentiment Classification**
  * **Positive (`4–5`):** High satisfaction percentage and count.
  * **Neutral (`3`):** Moderate satisfaction percentage and count.
  * **Negative (`1–2`):** Areas needing improvement percentage and count.
* 🔍 **Keyword Frequency & Text Mining**
  * Normalizes comment text (strips punctuation, converts to lowercase).
  * Filters out common English stop words (`and`, `but`, `the`, `is`, `a`, `of`, `too`).
  * Ranks the **Top 3 most frequent keywords**, resolving frequency ties alphabetically.

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.x
* **Libraries:** `pandas`, `re`, `collections`, `os`

### Installation
1. Ensure Python 3 is installed on your machine.
2. Install `pandas` via pip:
   ```bash
   pip install pandas
   ```

---

## 📂 Input Data Format (`feedback.csv`)

Place a file named `feedback.csv` in the root directory alongside the script. It must follow a 3-column CSV structure: `StudentID,Rating,Comment`.

```csv
StudentID,Rating,Comment
S1,5,Great teaching and clear notes
S2,4,Clear explanations and good examples
S3,2,Too fast and notes unclear
S4,3,Good but too fast
S5,5,Great examples
S6,4,Great notes
```

---

## 🚀 How to Run

1. Clone or download the repository to your local machine.
2. Ensure both `feedback_analyzer.py` and `feedback.csv` are in the same directory.
3. Execute the script via terminal:
   ```bash
   python feedback_analyzer.py
   ```

---

## 🖥️ Sample Console Output

### ✅ Standard Execution (Valid Dataset)
```text
--- RESULTS ---
Valid feedback: 6
Average rating: 3.83
Ratings: 5 -> 2, 4 -> 2, 3 -> 1, 2 -> 1, 1 -> 0
Positive: 4 (66.67%)
Neutral: 1 (16.67%)
Negative: 1 (16.67%)
Top 3 words: great (3), notes (3), clear (2)
```

### ⚠️ Edge Case Handling (Invalid Rows Detected)
When encountering invalid ratings like `S7,6,Nice` or `S8,abc,Nice`:
```text
Warning: Row 7 skipped - rating must be a whole number from 1 to 5.
Warning: Row 8 skipped - rating must be a whole number from 1 to 5.
```

---

<div align="center">
  <sub>Developed by <b>Pranav Baghel</b> • B.Tech CSE (in association with Google) • Rungta International Skills University</sub>
</div>
