PYTHON := PYTHONPATH=dags /usr/bin/env python3

init:
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install -r requirements.txt
	echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
	docker-compose up airflow-init