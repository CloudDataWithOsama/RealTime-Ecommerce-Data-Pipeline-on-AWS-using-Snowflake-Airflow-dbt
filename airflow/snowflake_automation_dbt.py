from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 4, 24),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'snowflake_test_dag',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False,
) as dag:

    check_orders_count = SnowflakeOperator(
        task_id='check_orders_count',
        snowflake_conn_id='snowflake_conn',
        sql="SELECT COUNT(*) FROM ECOMMERCE_DB.RAW.ORDERS;"
    )

    transform_data = SnowflakeOperator(
        task_id='transform_data',
        snowflake_conn_id='snowflake_conn',
        sql="""
        CREATE OR REPLACE TABLE ECOMMERCE_DB.RAW.ANALYTICS_ORDERS AS
        SELECT * FROM ECOMMERCE_DB.RAW.ORDERS
        QUALIFY ROW_NUMBER() OVER (
            PARTITION BY ORDER_ID
            ORDER BY ORDER_ID
        ) = 1;
        """
    )

    run_dbt_transformations = BashOperator(
        task_id='run_dbt_transformations',
        bash_command='cd /home/ec2-user/ecommerce_dbt && /home/ec2-user/airflow_env/bin/dbt run',
    )

    check_orders_count >> transform_data >> run_dbt_transformations