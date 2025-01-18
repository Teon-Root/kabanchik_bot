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
    
  
# print(get_new_orders('cb98985a2930f87b9f5f0014127253f041321179'))


