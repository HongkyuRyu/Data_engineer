# the versioned Airflow image with specific Python version
FROM apache/airflow:2.3.3-python3.8

# COPY requirements file
COPY requirements.txt /requirements.txt

# upgrade pip and install dependencies
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt

# Copy the DAG and script files to the container
COPY ./extract/crawling.py /opt/airflow/dags/crawling.py
COPY ./dag/dag_python_operator.py /opt/airflow/dags/dag_python_operator.py



