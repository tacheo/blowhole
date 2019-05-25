.PHONY: all clean lint type test test-cov

CMD:=poetry run
PYMODULE:=blowhole

all: lint type test

lint:
	$(CMD) flake8 $(PYMODULE) tests

type:
	$(CMD) mypy $(PYMODULE) tests 

test:
	$(CMD) pytest --cov=$(PYMODULE) tests

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) tests --cov-report html

clean:
	git clean -Xdf # Delete all files in .gitignore
