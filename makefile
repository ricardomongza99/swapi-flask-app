.DEFAULT_GOAL := build

build:
	docker build -t swapi-app .
.PHONY: build

run:
	docker run -p 3000:3000 swapi-app
.PHONY: run
