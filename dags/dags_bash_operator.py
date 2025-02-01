"""Example DAG demonstrating the usage of the BashOperator."""

from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 2, 2, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    '''
    run_this_last = EmptyOperator(
        task_id="run_this_last",
    )
    '''
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami", # whoami 출력
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME", # HOSTNAME이라는 환경변수 값을 출력해라
    )

    bash_t1 >> bash_t2 # Task 순서 (t1 -> t2)

if __name__ == "__main__":
    dag.test()
