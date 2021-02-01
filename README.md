![ANA](https://raw.githubusercontent.com/nlo-portfolio/nlo-portfolio.github.io/master/style/images/programs/ana.png "ANA")

## Description ##

ANA (Alpha Numeric Augmenter) is an application for modifying wordlists with commonly used password mnemonic substitutions (also called 'munged passwords'). Given a wordlist file, ANA will substitute out characters for numbers based on settings in the provided configuration file.

## Dependencies ##

Ubuntu<br>
Python v3<br>
\* All required components are included in the provided Docker image.

## Usage ##

Place the wordlist file in the project root directory, and enter the filename at the prompt after running.<br>
<br>
Ubuntu:

```
python3 ana.py
python3 -m unittest --verbose
```

Docker:

```
docker-compose build
docker run <ana | test>
```
