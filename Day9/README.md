Perfume Dataset Cleaning
🔍 Overview

This script cleans and preprocesses a raw perfume dataset using pandas and regex, then saves the cleaned version as a new CSV file.

✅ Cleaning Steps

Brand & Perfume Names: Capitalized, stripped spaces

Type: Standardized (edp → EDP, etc.), removed invalid rows

Category & Target Audience: Cleaned whitespace, mapped values (Men → Male)

Longevity: Removed unwanted text via regex, normalized values (6–8 hours → Strong)

Duplicates: Removed duplicate rows

Nulls: Checked for missing values

📦 Output

Cleaned file saved as:

cleaned_perfume_dataset.csv

🛠 Tools

Python, pandas, re (regex)

IDE: VS Code
