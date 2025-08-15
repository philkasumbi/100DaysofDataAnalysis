# 🎓 Student Performance Insights Dashboard

## 📌 Overview
An interactive **Power BI dashboard** analyzing student performance data to identify trends and factors influencing academic results.

---

## 🗂 Dataset
- **Source**: [Students Performance Dataset - Kaggle](https://www.kaggle.com)  
- **Key Fields**: Gender, Grade Category, GPA, Absences, Study Hours

---

## 🛠 Data Preparation
Performed in **Python (Pandas)** and **Power Query**:
- Gender recoding (`0` → Male, `1` → Female)
- GPA classification:
  - A (≥ 3.5), B (≥ 3.0), C (≥ 2.5), D (≥ 2.0), F (< 2.0)
- Absenteeism grouped into bins:
  - 0–9 → Low Absences  
  - 10–19 → Moderate  
  - 20–29 → High  
  - 30+ → Very High
- Removed duplicates and handled missing values

---

## 📊 Dashboard Features
- **Slicers**: Gender, Grade Category, Absenteeism Group
- **KPIs**: Average GPA, Total Students, Avg. Study Hours
- **Charts**:
  - GPA by gender
  - Study hours vs grades
  - Absenteeism vs performance

---

## 📈 Key Insights
- Higher study hours → better grades  
- High absenteeism → lower GPA  
- Minimal but notable gender-based performance differences

---

## 📦 Tools Used
- Python (Pandas)  
- Power Query  
- Power BI  

---



