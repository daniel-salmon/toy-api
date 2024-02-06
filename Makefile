build:
	docker build -t danielsalmon/toy-api:latest .

push:
	docker push danielsalmon/toy-api:latest

run:
	docker run -d -p 8080:8080 danielsalmon/toy-api:latest
