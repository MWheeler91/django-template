SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c

PROJECT_NAME=django-template
VENV=~/venv/$(PROJECT_NAME)
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Set up virtual environment and install requirements
install:
	@echo "Creating venv at $(VENV)"
	python3 -m venv $(VENV)
	@echo "Installing requirements"
	$(PIP) install -r z_requirements/linux_requirements.txt

# Show command to activate the venv
activate:
	@echo "Run: source $(VENV)/bin/activate"

# Run Django dev server
run:
	$(PYTHON) manage.py runserver

# Apply migrations
migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

# Run unit tests
test:
	$(PYTHON) manage.py test

# Format code with black
format:
	black .

# Collect static files
collectstatic:
	$(PYTHON) manage.py collectstatic --noinput

# Clean Python cache files
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

rebuild:
	rm -rf $(VENV)
	$(MAKE) install

# Create Secret and add it to .env
secret:
	@echo "Updating SECRET_KEY in .env"
	@KEY=$$(python3 -c 'from django.core.management.utils import get_random_secret_key as g; print(g())'); \
	if grep -q '^SECRET_KEY=' .env; then \
		sed -i.bak "s|^SECRET_KEY=.*|SECRET_KEY='$$KEY'|" .env; \
	else \
		echo "SECRET_KEY='$$KEY'" >> .env; \
	fi


init: install
	@echo "Step 1: Removing existing .gitignore if present"
	@rm -f .gitignore

	@echo "Step 2: Renaming gitignore.txt to .gitignore"
	@cp gitignore.txt .gitignore

	@echo "Step 3: Renaming z_env.example to .env"
	@if [ -f z_env.example ] && [ ! -f .env ]; then mv z_env.example .env; fi

	@echo "Step 4: Generating SECRET_KEY and updating .env"
	@SECRET=$$(python3 -c 'from django.core.management.utils import get_random_secret_key as g; print(g())'); \
	sed -i "/^SECRET_KEY=/c\SECRET_KEY='$$SECRET'" .env; \
	echo "Generated SECRET_KEY: $$SECRET"