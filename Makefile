install:
	poetry install

activate:
	( \
		python3 -m venv .venv; \
        . .venv/bin/activate; \
        pip install -r requirements.txt; \
    )

lint:
	poetry run flake8

db_init:
	poetry run python3 job_bot/data/init_db.py

run:
	poetry run python3 run.py
