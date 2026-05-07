# Amazon QuickSight Setup Guide

## Step 1 — Open Amazon QuickSight

1. Login to AWS Console
2. Search for Amazon QuickSight
3. Click "Sign Up for QuickSight"
4. Choose Standard Edition
5. Complete setup

--------------------------------------------------

# Step 2 — Create Snowflake Connection

1. Open QuickSight
2. Go to:
   Manage Data → New Dataset

3. Select:
   Snowflake

4. Enter Connection Details:

Data Source Name:
Snowflake_Ecommerce_DS

Database Server:
<your-snowflake-account-url>

Warehouse:
COMPUTE_WH

Database:
ECOMMERCE_DB

Schema:
RAW

Username:
<your-username>

Password:
<your-password>

5. Click:
   Create Data Source

--------------------------------------------------

# Step 3 — Select Dataset

1. Choose:
   ANALYTICS_ORDERS

2. Click:
   Select

3. Click:
   Edit / Preview Data

4. Verify:
   - ORDER_ID
   - CUSTOMER_NAME
   - ITEM_NAME
   - PRICE
   - INSERTED_AT

--------------------------------------------------

# Step 4 — Import Data into SPICE

1. Select:
   Import to SPICE

2. Click:
   Visualize

--------------------------------------------------

# Step 5 — Create Dashboard Visuals

## KPI Card
Measure:
SUM(PRICE)

--------------------------------------------------

## Line Chart
X-Axis:
INSERTED_AT

Y-Axis:
COUNT(ORDER_ID)

--------------------------------------------------

## Pie Chart
Category:
ITEM_NAME

Value:
COUNT(ITEM_NAME)

--------------------------------------------------

## Top Customers Bar Chart
Category:
CUSTOMER_NAME

Value:
SUM(PRICE)

--------------------------------------------------

# Step 6 — Schedule Refresh

1. Open Dataset Settings
2. Click:
   Schedule Refresh

3. Configure:
   Every 1 Hour

4. Save