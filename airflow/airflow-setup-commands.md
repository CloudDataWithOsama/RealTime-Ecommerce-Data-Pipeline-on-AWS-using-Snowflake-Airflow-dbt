# Airflow Setup Commands

python3 -m venv airflow_env

source airflow_env/bin/activate

pip install --upgrade pip

pip install "apache-airflow==2.8.1" apache-airflow-providers-snowflake --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.9.txt"

export AIRFLOW_HOME=~/airflow

airflow db init

airflow users create \
--username admin \
--firstname Osama \
--lastname Hashmi \
--role Admin \
--email osamahashmi28@gmail.com \
--password 'Admin#123'

airflow scheduler -D

airflow webserver -D