# Apex Planet - Task 1: Data Immersion & Wrangling

## Project Overview
This repository contains the deliverables for Task 1. The goal of this task is to take a raw, messy dataset containing Indian customer transactions, profile it for quality issues, and use Python to clean and transform it for downstream business analysis.

## Data Dictionary

| Variable Name | Data Type | Description | Business Relevance |
| :--- | :--- | :--- | :--- |
| `Transaction_ID` | String | Unique identification number for each purchase. | Used to track total order volume and identify unique sales. |
| `Customer_Name` | String | Full name of the Indian customer. | Used for personalizing marketing emails and CRM records. |
| `City` | Category | Metro/Tier city location of the customer. | Crucial for regional sales analysis and logistics planning. |
| `Date_of_Birth` | DateTime | The customer's birthdate. | Used to determine target audience demographics. |
| `Product_Category`| Category | The department the item belongs to. | Helps inventory management see which categories perform best. |
| `Purchase_Date` | DateTime | The exact date the transaction occurred. | Used to analyze festive sales trends and revenue cycles. |
| `Order_Amount_INR`| Float | The total money spent in Indian Rupees (₹). | Core metric for calculating gross company revenue. |
| `Order_Status` | Category | Current state of delivery. | Used by operations to monitor fulfillment performance. |
| `Customer_Age` | Integer | **(Engineered Feature)** Calculated age of the customer. | Allows the marketing team to build age-targeted campaigns. |

