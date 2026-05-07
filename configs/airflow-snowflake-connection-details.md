# Airflow Snowflake Connection Setup

## Step 1 — Open Airflow UI

Open Browser:

http://<EC2-PUBLIC-IP>:8080

--------------------------------------------------

# Step 2 — Login

Username:
admin

Password:
Admin#123

--------------------------------------------------

# Step 3 — Open Connections

Go to:

Admin → Connections

--------------------------------------------------

# Step 4 — Create New Connection

Click:
+

--------------------------------------------------

# Step 5 — Enter Connection Details

Connection Id:
snowflake_conn

Connection Type:
Snowflake

--------------------------------------------------

# Snowflake Credentials

Account:
EJPKLNN-SKB17371

Warehouse:
COMPUTE_WH

Database:
ECOMMERCE_DB

Schema:
RAW

Login:
TAHIRHASHMI90

Password:
12qwaszx9090Osama

Role:
SYSADMIN

--------------------------------------------------

# Step 6 — Save Connection

Click:
Save

--------------------------------------------------

# Step 7 — Verify DAG

Run:

airflow dags list

Expected DAG:

snowflake_test_dag