from airflow import DAG
from datetime import date, datetime
from airflow.providers.common.sql.hooks.sql import  DbApiHook
#from airflow.hooks. import PostgresHook
from airflow.providers.common.sql.sensors.sql import SqlSensor
default_args = {
'start_date': datetime(2021, 1, 1)
}
with DAG('DB_Hook', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    check1_postgres=SqlSensor(task_id="check1_postgres",conn_id="local-postgres",sql='select * from public."emp"')
    check2_postgres_hook = DbApiHook(conn_name_attr="local-postgres", default_conn_name="local_postgres",sql='select * from public."emp"')
    check1_postgres>>check2_postgres_hook