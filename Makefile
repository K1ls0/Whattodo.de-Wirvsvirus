install:
	python -m pip install -r requirements.txt

run:
	cd ./web; npm run build; cd ..
	cd ./Webserver && python3 ./app.py

httpGetElements:
	curl -H "Content-Type: application/json" --request GET --data '{"tags":["Kreativ"],"include":false}' "http://0.0.0.0:3000/elements"

httpGetTags:
	curl -H "Content-Type: application/json" --request GET "http://0.0.0.0:3000/tags"

httpNewItem:
	curl -H "Content-Type: application/json" --request PUT --data '{"NewTask":["Tag1", "Tag2"]}' "http://0.0.0.0:3000/elements"
