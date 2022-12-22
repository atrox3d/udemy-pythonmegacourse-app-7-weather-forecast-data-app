from secret.openweathermap import API_KEY
import requests
import json


def get_from_cache(cache_path='cache.json'):
    """
    get weather data from local file, if present.\n
    returns None otherwise\n
    :param cache_path:
    :return: json as dict or None
    """
    try:
        print(f'Loading data from {cache_path}')
        with open(cache_path, 'r') as cache_file:
            data = json.load(cache_file)
    except FileNotFoundError:
        print(f'Failed to load {cache_path}')
        return None
    return data


def get_from_api(place):
    """
    get weather data from api for the chosen place\n
    :param place: city name
    :return: json data as dict
    """
    url = f'https://api.openweathermap.org/data/2.5/forecast' \
          f'?q={place}' \
          f'&units=metric' \
          f'&appid={API_KEY}'
    print(f'Loading data from {url}')
    response = requests.get(url)
    data = response.json()
    return data


def get_data(place, days=None, kind=None, use_cache=False):
    """
    get weather data either from local file or from API, depending from use_cache\n
    :param place: city name
    :param days: number of days to return
    :param kind: temperature or sky
    :param use_cache: boolean
    :return:
    """
    data = None
    if use_cache:
        data = get_from_cache()
    if not data or not use_cache:
        data = get_from_api(place)

    # filter the number of days
    if days:
        data = data['list'][:8 * days]

    # filter the kind of data
    match kind.lower():
        case None:
            pass
        case 'temperature':
            data = [item['main']['temp'] for item in data]
        case 'sky':
            data = [item['weather'][0]['main'] for item in data]

    return data


if __name__ == '__main__':
    data = get_data(place='volterra', days=5, kind='sky', use_cache=False)
    print(json.dumps(data, indent=4))
    print(len(data))
