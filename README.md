# Pokepy
Command line wrapper of Pokeapi for educational purposes.

## Prerequisites
In order to access the Pokeapi using the requests module, Python must be compiled with OpenSSL version >= 1.0.2

## Installation
For testing purposes it's best you install pokepy via pip in a virtual environment.

* Get the source from this repo or fork it to your own repo and clone it:
```bash
git clone https://github.com/Condla/pokepy/
cd pokepy
```

* Optional: Install the tool in a virtualenv:
```bash
sudo pip install virtualenv
mkdir venv
virtualenv venv
source venv/bin/activate
```

* Then install pokepy:
```bash
pip install -e .
```

## Usage
```bash
Usage:
    pokepy (pokemon | type | ability) --id=ID

Options:
    -i --id=ID                # specify the id of the pokemon, type or ability
    -h --help                 # Show this help
```

## Examples
```bash
# Get the name of Pokemon 150
$ pokepy pokemon 150
mewtwo
# Get the name of Pokemon type 3
$pokepy type -i 3
flying
# Get the Pokemon ability 6
$ pokepy ability -i 6
damp
```
