# Syntecxhub_project_CSV_Excel_Converter

CSV → Excel Converter

A simple Python utility to read, clean, and convert CSV files into Excel (.xlsx) format using pandas. Ideal for data preparation, reporting automation, and handling messy CSV files.

Features

Convert CSV to Excel with a single command.

Data cleaning & normalization:

Fill missing values (e.g., empty Age → 0)

Trim whitespace from text

Rename or standardize columns


CLI support: Specify input and output paths.

Logging & error handling for invalid files or missing data.

Installation

Make sure Python 3.x is installed. Install dependencies:

pip install pandas openpyxl

Usage

Run the script from the command line:

python csv_to_excel.py --input sample.csv --output output.xlsx

CLI Arguments:

--input : Path to the input CSV file

--output : Path for the output Excel file



---

Example

CSV Input (sample.csv):

Name	Age	Grade

Sagar	20	A
Sara	19	B
Alfiya		C


Excel Output (sample.xlsx):

Name	Age	Grade

Sagar	20	A
Sara	19	B
Alfiya	0	C


Workflow Diagram:

