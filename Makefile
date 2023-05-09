
run:
	python3 src/__main__.py

docker-all:
	docker build --tag try .
	docker run -it try

docker-run:
	docker run -it try