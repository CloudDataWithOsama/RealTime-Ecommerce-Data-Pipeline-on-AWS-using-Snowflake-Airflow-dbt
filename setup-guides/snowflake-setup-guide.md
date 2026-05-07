# Snowflake Complete Setup Guide

## Step 1 — Create Database

CREATE DATABASE ECOMMERCE_DB;

--------------------------------------------------

# Step 2 — Create Schema

USE DATABASE ECOMMERCE_DB;

CREATE SCHEMA RAW;

--------------------------------------------------

# Step 3 — Create Warehouse

CREATE WAREHOUSE COMPUTE_WH
WITH
WAREHOUSE_SIZE = 'XSMALL'
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE;

--------------------------------------------------

# Step 4 — Create Tables

CREATE OR REPLACE TABLE ORDERS (

    ORDER_ID NUMBER,
    CUSTOMER_NAME STRING,
    ITEM_NAME STRING,
    PRICE NUMBER

);

CREATE OR REPLACE TABLE CUSTOMERS (

    CUSTOMER_NAME STRING,
    EMAIL STRING,
    COUNTRY STRING

);

--------------------------------------------------

# Step 5 — Create Storage Integration

CREATE OR REPLACE STORAGE INTEGRATION s3_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'S3'
ENABLED = TRUE
STORAGE_ALLOWED_LOCATIONS = (
's3://s3-ecommerce-raw-data-landing/'
);

--------------------------------------------------

# Step 6 — Create Stage

CREATE OR REPLACE STAGE my_s3_stage
URL='s3://s3-ecommerce-raw-data-landing/'
STORAGE_INTEGRATION=s3_integration;

--------------------------------------------------

# Step 7 — Create Snowpipe

CREATE OR REPLACE PIPE orders_pipe
AUTO_INGEST = TRUE
AS

COPY INTO ORDERS
FROM @my_s3_stage/orders/
FILE_FORMAT = (
TYPE = CSV
FIELD_DELIMITER = ','
SKIP_HEADER = 0
);

--------------------------------------------------

# Step 8 — Verify Loaded Data

SELECT * FROM ORDERS LIMIT 10;

SELECT * FROM CUSTOMERS LIMIT 10;

--------------------------------------------------

# Step 9 — Check Pipe Status

SHOW PIPES;

--------------------------------------------------

# Step 10 — Check Copy History

SELECT *
FROM TABLE(
    INFORMATION_SCHEMA.COPY_HISTORY(
        TABLE_NAME=>'ORDERS',
        START_TIME=>DATEADD(hours,-1,CURRENT_TIMESTAMP())
    )
);