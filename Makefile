.PHONY: clean-dangling-images setup \
build build-push build-run build-cold \
push run

-include .env

$(eval REGISTRY=$(shell grep '* Registry:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))
$(eval REPOSITORY=$(shell grep '* Repository name:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))
$(eval VERSION=$(shell grep '* Current version:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))

clean-dangling-images:
	@docker rmi -f $$(docker images -f 'dangling=true' -q)

setup:
	@cp ./.env-dist ./.env

build:
	@docker build \
		--no-cache \
		-f Dockerfile \
		-t $(REGISTRY)/$(REPOSITORY):$(VERSION) .

build-push:
	@make build
	@make docker-login
	@make push

docker-login:
	@echo $(REGISTRY_PASSWORD) | docker login --username $(REGISTRY_USERNAME) --password-stdin

push:
	@docker push $(REGISTRY)/$(REPOSITORY):$(VERSION)

run:
	@docker run -it \
	-e PORT=$(PORT) \
	-e DEBUG=$(DEBUG) \
	-e DEV=$(DEV) \
	-e SECRET_KEY=$(SECRET_KEY) \
	-e QA=$(QA) \
	-p $(PORT):$(PORT) \
	-v $(PWD)/covid_19_us:/usr/src/covid_19_us \
		$(REGISTRY)/$(REPOSITORY):$(VERSION)

run-prod:
	@docker run -it -p 8000:8000 desholmes/covid-19-uk-api:1.0.2

build-run:
	@make build
	@make run

build-cold:
	@make setup
	@make build-run