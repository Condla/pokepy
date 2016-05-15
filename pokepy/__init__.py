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
    Get pokemon or type or ability command from command line
    arguments.
    '''
    paths = ['pokemon', 'type', 'ability']
    for path in paths:
        if arguments[path]:
            break
    return path


def get_id(arguments):
    '''
    Get id from command line arguments.
    '''
    return arguments['--id']


def call_pokeapi(path, id_number, key='name'):
    '''
    Call the RESTful PokeAPI and parse the response. If pokemon, ability or
    type ids are not found than the error message detail is returned.
    '''
    url = POKEAPI.format(path=path, id=id_number)
    response = requests.get(url)
    response_json = response.json()
    try:
        res = response_json[key]
    except:
        res = response_json['detail']

    return res


def __main__():
    '''
    Entrypoint of command line interface.
    '''
    from docopt import docopt
    arguments = docopt(__doc__, version='0.1.0')
    path = get_api_path(arguments)
    id_number = get_id(arguments)
    print(call_pokeapi(path, id_number))
