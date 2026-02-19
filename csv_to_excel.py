import pandas as pd
import argparse
import os

def clean_data(df):
    # Keep only Name and Age columns
    df = df[['Name', 'Age']]

    # Clean Name column
    df['Name'] = df['Name'].str.strip().fillna("Unknown")

    # Convert Age to number
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce').fillna(0)

    return df

def main():
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output Excel file")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("❌ Input file not found")
        return

    df = pd.read_csv(args.input)
    df = clean_data(df)

    df.to_excel(args.output, index=False, engine="openpyxl")
    print("✅ Conversion successful!")

if __name__== "__main__":
    main()