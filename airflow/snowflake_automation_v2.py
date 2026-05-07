from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Osama',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'snowflake_test_dag',
    default_args=default_args,
    description='Snowflake Ingestion and Transformation DAG with Deduplication',
    schedule_interval='@hourly',
    catchup=False
) as dag:

    check_orders_count = SnowflakeOperator(
        task_id='check_orders_count',
        sql='SELECT COUNT(*) FROM ECOMMERCE_DB.RAW.ORDERS;',
        snowflake_conn_id='snowflake_conn',
    )

    transform_data = SnowflakeOperator(
        task_id='transform_data',
        sql="""
        INSERT OVERWRITE INTO ECOMMERCE_DB.RAW.ANALYTICS_ORDERS (
            ORDER_ID,
            CUSTOMER_NAME,
            ITEM_NAME,
            PRICE
        )

        SELECT
            ORDER_ID,
            CUSTOMER_NAME,
            ITEM_NAME,
            PRICE

        FROM ECOMMERCE_DB.RAW.ORDERS

        QUALIFY ROW_NUMBER()
        OVER (
            PARTITION BY ORDER_ID
            ORDER BY ORDER_ID
        ) = 1;
        """,
        snowflake_conn_id='snowflake_conn',
    )

    check_orders_count >> transform_data