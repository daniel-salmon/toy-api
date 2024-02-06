build:
	docker build -t toy-api:latest .

run:
	docker run -d -p 8080:8080 toy-api:latest
