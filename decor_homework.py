import logging
import pathlib
import os
import requests

"""TASK 1"""


def logging_1(func):
    logging.basicConfig(level=logging.INFO, filename='main.log',
                        format='%(asctime)s %(levelname)s:%(message)s')

    def wrapper(*args, **kwargs):
        result = str(func(*args, **kwargs))

        print(logging.info("fuction  %s is called with args: %s, result = %s" % (func.__name__, args, result)))

        return result

    return wrapper


@logging_1
def my_func_1(*args):
    return sum(args)


"""TASK 2"""


def logging_2(arg):
    def inner_decorator(func):
        logging.basicConfig(level=logging.INFO, filename='main.log',
                            format='%(asctime)s %(levelname)s:%(message)s')

        def wrapped(*args, **kwargs):
            result = str(func(*args, **kwargs))
            logging.info("fuction  %s is called with args: %s, result = %s, file_path: %s" % (
                func.__name__, args, result, arg))
            return result

        return wrapped

    return inner_decorator


def get_filepath(file_name):
    return os.path.abspath(file_name)


@logging_2(get_filepath('main.log'))
def my_func_2(*args):
    return sum(args)


"""TASK 3"""


@logging_1
def get_the_smartest_superhero(superheros):
    base_url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(base_url + '/all.json')
    all_heroes_data = response.json()
    clever_heroes_dict = {}
    for hero in all_heroes_data:
        for id in superheros:
            if id == hero['id']:
                clever_heroes_dict[hero['name']] = hero['powerstats']['intelligence']
    the_smartest_superhero = max(clever_heroes_dict, key=clever_heroes_dict.get)
    return the_smartest_superhero


my_func_1(10, 30, 40)

my_func_2(1, 3, 4)

id_list = [1, 2, 3]

get_the_smartest_superhero(id_list)
