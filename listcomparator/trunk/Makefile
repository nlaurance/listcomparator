#
# Makefile for listcomparator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Combines scripts for common tasks.
#

PYTHON ?= python

export PYTHONPATH = $(shell echo "$$PYTHONPATH"):$(shell python -c 'import os; print ":".join(os.path.abspath(line.strip()) for line in file("PYTHONPATH"))' 2>/dev/null)

.PHONY: all clean clean-pyc docs \
    pylint test test-coverage

all: clean-pyc test

clean: clean-pyc
	-rm -rf build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

docs: docs/build

docs/build: docs/src/*.txt
	$(PYTHON) docs/generate.py html docs/build $?
	touch docs/build

pylint:
	@pylint --rcfile scripts/pylintrc pygments

test:
	@$(PYTHON) tests/run.py $(TESTS)

test-coverage:
	@$(PYTHON) tests/run.py -C $(TESTS)
