install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C flask_app.py

test:
	#python -m pytest -vv test_flask_app.py

deploy:
	echo "Deploying app"
	eb deploy eb-flask-app

all: install format lint test