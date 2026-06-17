import pandas as pd
import numpy as np

def generate_and_clean_indian_data():
    # ----------------------------------------------------
    # STEP 1: GENERATE IMAGINARY MESSY INDIAN DATASET
    # ----------------------------------------------------
    print("⏳ Step 1: Simulating raw Indian customer dataset...")
    np.random.seed(42)
    rows = 1000
    
    names = ['Aarav Patel', 'Priya Sharma', 'Rohan Das', 'Ananya Iyer', 'Rahul Verma', 'Sneha Reddy', 'Amit Mishra', 'Vikram Singh']
    cities = ['Delhi', 'delhi', 'Mumbai', 'MUMBAI ', 'Bangalore', 'bangalore', ' Kolkata', 'Chennai']
    categories = ['electronics', 'ELECTRONICS', ' Apparel', 'Apparel ', 'Home & Kitchen', 'Footwear']
    statuses = ['shipped', 'Shipped', 'SHIPPED ', 'pending', 'cancelled', 'delivered']
    
    raw_data = {
        'Transaction_ID': [f"APEX{10000 + i}" for i in range(rows)],
        'Customer_Name': np.random.choice(names, size=rows),
        'City': np.random.choice(cities, size=rows),
        'Date_of_Birth': np.random.choice(['1992-05-14', '1988/11/23', '2001-01-01', None, '1979.12.05'], size=rows),
        'Product_Category': np.random.choice(categories, size=rows),
        'Purchase_Date': np.random.choice(['2026-03-01', '02/03/2026', '2026/03/04', '2026-03-05'], size=rows),
        'Order_Amount_INR': np.random.choice([499.0, 2499.0, 12500.0, 95000.0, -150.0, 1500.0], size=rows),
        'Order_Status': np.random.choice(statuses, size=rows)
    }
    
    df = pd.DataFrame(raw_data)
    df = pd.concat([df, df.iloc[[10, 20, 30, 40]]], ignore_index=True)
    print(f"📊 Raw Data Loaded. Shape: {df.shape}")

    # ----------------------------------------------------
    # STEP 2: DATA CLEANING & WRANGLING
    # ----------------------------------------------------
    print("\n🧹 Step 2: Initiating data cleaning process...")

    df = df.drop_duplicates()
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
    df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce')

    current_year = 2026
    df['Customer_Age'] = current_year - df['Date_of_Birth'].dt.year
    median_age = df['Customer_Age'].median()
    df['Customer_Age'] = df['Customer_Age'].fillna(median_age).astype(int)

    df['City'] = df['City'].astype(str).str.strip().str.title()
    df['Product_Category'] = df['Product_Category'].astype(str).str.strip().str.title()
    df['Order_Status'] = df['Order_Status'].astype(str).str.strip().str.upper()

    median_amt = df[df['Order_Amount_INR'] > 0]['Order_Amount_INR'].median()
    df.loc[df['Order_Amount_INR'] < 0, 'Order_Amount_INR'] = median_amt
    
    Q1 = df['Order_Amount_INR'].quantile(0.25)
    Q3 = df['Order_Amount_INR'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    df['Order_Amount_INR'] = np.where(df['Order_Amount_INR'] > upper_bound, upper_bound, df['Order_Amount_INR'])

    # ----------------------------------------------------
    # STEP 3: OUTPUT FINAL CLEANED DATASET
    # ----------------------------------------------------
    output_file = "cleaned_indian_sales_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\n🚀 Step 3: Success! Cleaned file saved as '{output_file}'. Final Shape: {df.shape}")

if __name__ == "__main__":
    generate_and_clean_indian_data()
  
