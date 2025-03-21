COMPOSE_FILE ?= docker-compose.yml
MIGRATION_MSG ?= "Auto-generated migration"
BACKEND_SERVICE := backend
DB_SERVICE := db

.PHONY: help build up down logs \
		migrate generate clean \
        shell-backend shell-db status

help:
	@echo "Usage:"
	@echo "  make build             Build Docker containers"
	@echo "  make up                Run Docker containers"
	@echo "  make down              Stop and remove Docker containers"
	@echo "  make logs              Show Docker containers logs"
	@echo "  make migrate           Apply migrations (containers should be running)"
	@echo "  make generate          Generate migration (no needed running containers)"
	@echo "  make generate-local    Generate local migrations (PostgreSQL needed)"
	@echo "  make clean             Remove Docker containers, volumes and images"
	@echo "  make shell-backend     Backend container shell"
	@echo "  make shell-db          Database container shell"
	@echo "  make status            Show Docker container status"

build:
	docker-compose -f $(COMPOSE_FILE) build

up:
	docker-compose -f $(COMPOSE_FILE) up -d --build

down:
	docker-compose -f $(COMPOSE_FILE) down

logs:
	docker-compose -f $(COMPOSE_FILE) logs -f

updown:
	make down && make up

migrate:
	@BACKEND_CONTAINER=$$(docker-compose -f $(COMPOSE_FILE) ps -q $(BACKEND_SERVICE) | head -n 1); \
	if [ -z "$$BACKEND_CONTAINER" ]; then \
		echo "Error: No app container running. Run 'make up' first."; \
		exit 1; \
	else \
		docker exec -it $$BACKEND_CONTAINER alembic upgrade head; \
	fi

generate:
	@if [ -z "$(MESSAGE)" ]; then \
		docker-compose -f $(COMPOSE_FILE) run --rm $(BACKEND_SERVICE) alembic revision --autogenerate -m "$(MIGRATION_MSG)"; \
	else \
		docker-compose -f $(COMPOSE_FILE) run --rm $(BACKEND_SERVICE) alembic revision --autogenerate -m "$(MESSAGE)"; \
	fi

clean:
	docker-compose -f $(COMPOSE_FILE) down -v --rmi all

shell-backend:
	@BACKEND_CONTAINER=$$(docker-compose -f $(COMPOSE_FILE) ps -q $(BACKEND_SERVICE) | head -n 1); \
	if [ -z "$$BACKEND_CONTAINER" ]; then \
		echo "Error: No app container running. Run 'make up' first."; \
		exit 1; \
	else \
		docker exec -it $$BACKEND_CONTAINER bash; \
	fi

shell-db:
	@DB_CONTAINER=$$(docker-compose -f $(COMPOSE_FILE) ps -q $(DB_SERVICE) | head -n 1); \
	if [ -z "$$DB_CONTAINER" ]; then \
		echo "Error: No database container running. Run 'make up' first."; \
		exit 1; \
	else \
		docker exec -it $$DB_CONTAINER bash; \
	fi

status:
	docker-compose -f $(COMPOSE_FILE) ps