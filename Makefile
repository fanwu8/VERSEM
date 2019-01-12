# Makefile for the VERSEM Python suite
#
#

all: init test docs

# Initializing installation
init:
	pip install -r requirements.txt

# Testing installation
test:
	py.test tests

# Make Documentation
docs: docs/source/*.rst
	sphinx-apidoc -o ./docs/source/autogenerated/src ./src [*.rst *.npy]
	sphinx-apidoc -o ./docs/source/autogenerated/tests ./tests [*.rst *.npy]
	sphinx-apidoc -o ./docs/source/autogenerated/input ./input [*.rst *.npy]
	make latexpdf -C docs
	make html -C docs

# Cleaning up
clean:
	rm -rf docs/source/autogenerated/
	rm -rf results/timesteps
	rm -f results/gll_coordinates.npy
	make clean -C docs
		

.PHONY: init test
