import json
import os
import math
from functools import partial



def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as json_file:
        return json.load(json_file)


def get_biggest_bar(json_data):
    biggest_bar = max(json_data['features'],
                      key=lambda sc: sc['properties']
                                        ['Attributes']
                                        ['SeatsCount'])
    return biggest_bar


def get_smallest_bar(json_data):
    smallest_bar = min(json_data['features'],
                       key=lambda sc: sc['properties']
                                        ['Attributes']
                                        ['SeatsCount'])
    return smallest_bar


def _get_distance(user_location, bar_data):
    bar_coordinates = bar_data['geometry']['coordinates']
    distance = math.sqrt((user_location[0] - bar_coordinates[0]) ** 2 + (user_location[1] - bar_coordinates[1]) ** 2)
    return distance


def get_closest_bar(_json_data, longitude, latitude):
    coord = longitude, latitude
    return min(_json_data['features'], key=partial(_get_distance, coord))


if __name__ == '__main__':
    filepath = input('Введите адрес файла: ')
    json_data = load_data(filepath)
    longitude = float(input('Введите координаты долготы (Пример ввода: 38.2323): '))
    latitude = float(input('Введите координаты широты (Пример ввода: 38.2323): '))
    print('Самый большой бар - ', get_biggest_bar(json_data)['properties']['Attributes']['Name'],',',
          'Количество мест:', get_biggest_bar(json_data)['properties']['Attributes']['SeatsCount'])
    print('Самый маленький бар - ', get_smallest_bar(json_data)['properties']['Attributes']['Name'],',',
          'Количество мест: ', get_smallest_bar(json_data)['properties']['Attributes']['SeatsCount'])
    print('Ближайший к Вам бар - ', get_closest_bar(json_data, longitude, latitude)['properties']['Attributes']['Name'], ',',
          'адрес: ', get_closest_bar(json_data, longitude, latitude)['properties']['Attributes']['Address'], ',',
          'Количество мест: ', get_closest_bar(json_data, longitude, latitude)['properties']['Attributes']['SeatsCount'])
    
