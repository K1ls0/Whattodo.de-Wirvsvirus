install:
	python -m pip install -r requirements.txt

run:
	cd ./web && npm run build
	cd ./Webserver && python ./app.py