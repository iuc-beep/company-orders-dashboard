import pandas as pd
import sys

INPUT = sys.argv[1] if len(sys.argv) > 1 else "orders.xlsx"
OUTPUT = "data.csv"

df = pd.read_excel(INPUT, usecols=["ORDER_CREATED_AT", "COMPANY_NAME"])
df["date"] = pd.to_datetime(df["ORDER_CREATED_AT"], errors="coerce").dt.strftime("%Y-%m-%d")
df["COMPANY_NAME"] = df["COMPANY_NAME"].fillna("Unknown").astype(str).str.strip()
out = df.dropna(subset=["date"]).groupby(["date","COMPANY_NAME"]).size().reset_index(name="orders")
out.to_csv(OUTPUT, index=False)
print(f"Created {OUTPUT} with {len(out):,} company-date rows.")
