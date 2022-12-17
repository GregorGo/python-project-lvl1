# Hexlet tests and linter status:

[![Actions Status](https://github.com/GregorGo/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/GregorGo/python-project-lvl1/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/b2c44847c63ad5cdb69e/maintainability)](https://codeclimate.com/github/GregorGo/python-project-lvl1/maintainability)

This project contains various math games

To install, use:
install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: 
	python3 -m pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games

BRAIN-EVEN
[![asciicast](https://asciinema.org/a/hGfechWRX7hy5a34fKhsN5FSR.svg)](https://asciinema.org/a/hGfechWRX7hy5a34fKhsN5FSR)

BRAIN-CALC
[![asciicast](https://asciinema.org/a/PFvLCXoQFPXucHwdnnrqLDtmF.svg)](https://asciinema.org/a/PFvLCXoQFPXucHwdnnrqLDtmF)

BRAIN-GCD
[![asciicast](https://asciinema.org/a/It3OqPXXXRVNUODEVPq1b3RzH.svg)](https://asciinema.org/a/It3OqPXXXRVNUODEVPq1b3RzH)

BRAIN-PROGRESSION
[![asciicast](https://asciinema.org/a/0n2N8ts8Y7ebSksPri1Ul2q7l.svg)](https://asciinema.org/a/0n2N8ts8Y7ebSksPri1Ul2q7l)

BRAIN-PRIME
[![asciicast](https://asciinema.org/a/2qPe683ec35fBxxZlZZyidRnE.svg)](https://asciinema.org/a/2qPe683ec35fBxxZlZZyidRnE)



