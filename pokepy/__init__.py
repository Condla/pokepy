'''
Usage:
    pokepy (pokemon | type | ability) --id=ID

Options:
    -i --id=ID                # specify the id of the pokemon, type or ability
    -h --help                 # Show this help
'''


import requests


POKEAPI = 'https://pokeapi.co/api/v2/{path}/{id}'


def get_api_path(arguments):
    '''
Get pokemon or type or ability command
    '''
    paths = ['pokemon', 'type', 'ability']
    for path in paths:
        path = arguments[path]
        if path:
            break
    return path


def get_id(arguments):
    return arguments['--id']


def call_pokeapi(path, id_number, key='name'):
    url = POKEAPI.format(path=path, id=id_number)
    response = requests.get(url)
    res = response.json()[key]
    return res


def __main__():
    from docopt import docopt
    arguments = docopt(__doc__, version='0.1.0')
    path = get_api_path(arguments)
    id_number = get_id(arguments)
    print(call_pokeapi(path, id_number))
