# GNU Make
# https://www.gnu.org/software/make/

DIR:=$(shell pwd)

.PHONY: default
default:

.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: tests
tests:
	nosetests
