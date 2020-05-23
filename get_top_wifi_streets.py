import requests
import os
from pathlib import Path
import json
from zipfile import ZipFile
from collections import OrderedDict
from operator import itemgetter

MOS_RU_OBJECTS = {'libraries': '781682',
                  'cinemas': '781634',
                  'parks': '781642',
                  'cultural centers': '781690'}
NUMBER_OF_TOP_STREETS = 5


def get_json_files_from_mosru():
    mos_url = "https://op.mos.ru/EHDWSREST/catalog/export/get?id= "
    for wifi_object, value in MOS_RU_OBJECTS.items():
        response = requests.get(f'{mos_url}{value}')
        response.raise_for_status()
        with open(f"{wifi_object}.zip", 'wb') as file:
            file.write(response.content)
        with ZipFile(f'{wifi_object}.zip', 'r') as zipObj:
            zipObj.extractall('json')
        os.remove(f'{wifi_object}.zip')


def get_streets_from_files(directory='json'):
    streets = OrderedDict()
    for currentFile in Path(directory).iterdir():
        with open(currentFile, encoding='cp1251', errors='ignore') as json_file:
            for element in json.load(json_file, strict=False):
                if 'Address' in element and 'NumberOfAccessPoints' in element:
                    street = element['Address'].split(',')[1]
                    if street in streets:
                        streets[street] += element['NumberOfAccessPoints']
                    else:
                        streets[street] = element['NumberOfAccessPoints']
        os.remove(currentFile)
    os.rmdir(directory)
    return dict(sorted(streets.items(),
                       key=itemgetter(1), reverse=True)[:NUMBER_OF_TOP_STREETS])


def main():
    get_json_files_from_mosru()
    print(f'Топ {NUMBER_OF_TOP_STREETS} улиц с бесплатным Wi-Fi:')
    for street, wifi_number in get_streets_from_files().items():
        print(f'{street} - {wifi_number} точек')


if __name__ == '__main__':
    main()
