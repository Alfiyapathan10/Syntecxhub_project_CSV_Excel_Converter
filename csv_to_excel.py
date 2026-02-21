import pandas as pd

def clean_data(df):
    df = df[['Name', 'Age']]
    df['Name'] = df['Name'].str.strip().fillna("Unknown")
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce').fillna(0)
    return df

try:
    input_file = "data.csv"
    output_file = "output.xlsx"

    df = pd.read_csv(input_file)
    df = clean_data(df)
    df.to_excel(output_file, index=False)

    print("✅ Conversion Successful!")
    print("File saved as:", output_file)

except FileNotFoundError:
    print("❌ Error: data.csv file not found.")
except Exception as e:
    print("❌ Error:", e)