# from typing import Union
# import requests


# def get_new_orders(kabanchik_auth: str) -> Union[list[dict], bool]:
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'X-Requested-With': 'XMLHttpRequest',
#         'User-Agent': (
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#             'Chrome/117.0.0.0 Safari/537.36'
#         ),
#     }

#     cookies = {
#         'auth': kabanchik_auth
#     }

#     try:
#         r = requests.get(
#             'https://kabanchik.ua/ua/cabinet/recommended?page=1&category=92',
#             cookies=cookies,
#             headers=headers
#         )

#         if r.status_code != 200:
#             return False

#         else:
#             return r.json().get('items')

#     except Exception as e:
#         print(e)
#         return False
    
  
# print(get_new_orders())

from time import sleep
import pyautogui
import random
from dataclasses import dataclass


@dataclass
class Region:
    x1: int
    y1: int
    x2: int
    y2: int


@dataclass
class Point:
    x: int
    y: int


class Clicker:
    def __init__(self, radius: int):
        point = pyautogui.position()
        x1, y1 = (int(point.x - radius), int(point.y - radius))
        x2, y2 = (int(point.x + radius), int(point.y + radius))
        self.region = Region(x1, y1, x2, y2)

    def get_random_point_position(self) -> Point:
        x = random.randint(self.region.x1, self.region.x2)
        y = random.randint(self.region.y1, self.region.y2)

        return Point(x, y)

    def start(self, clicks: int):
        counter = 0

        while counter <= clicks:
            point: Point = self.get_random_point_position()
            pyautogui.click(x=point.x, y=point.y, button='left')
            sleep(random.randint(1, 10) / 100)

            counter += 1


def main():
    clicker = Clicker(radius=5)
    clicker.start(clicks=100)


if __name__ == '__main__':
    main()
