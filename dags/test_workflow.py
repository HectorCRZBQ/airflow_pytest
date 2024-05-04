from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def run_tests():
    # Ejecuta las pruebas con pytest
    subprocess.run(['pytest', '/opt/airflow/dags/tests/test_suma.py'])
#Actualización al repositorio de github
def upload_to_github(branch):
    # Agrega los cambios, hace commit y los sube a GitHub
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Resultados del Testeo'])
    subprocess.run(['git', 'push', 'origin', branch])
# Diseño del DAG
dag = DAG(
    'run_tests_and_upload_to_github',
    default_args=default_args,
    description='Realizamos el tests correspondientes, lo actualizamos a Github para el codigo de test_suma',
    schedule_interval=None,
)
# Ejecucción del testeo
run_tests_task = PythonOperator(
    task_id='run_tests',
    python_callable=run_tests,
    dag=dag,
)
# Actualizar el cambio a la rama main
upload_to_github_develop_task = PythonOperator(
    task_id='upload_to_github_develop',
    python_callable=upload_to_github,
    op_args=['develop'], # Insertamos el nombre de la rama como un argumento
    dag=dag,
)
# Actualizar el cambio a la rama main
upload_to_github_main_task = PythonOperator(
    task_id='upload_to_github_main',
    python_callable=upload_to_github,
    op_args=['main'],  # Insertamos el nombre de la rama como un argumento
    dag=dag,
)

run_tests_task >> upload_to_github_develop_task
run_tests_task >> upload_to_github_main_task
