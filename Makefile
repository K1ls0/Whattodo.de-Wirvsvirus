install:
	python -m pip install -r requirements.txt

run:
	cd ./web; npm run build; cd ..
	cd ./Webserver && python3 ./app.py