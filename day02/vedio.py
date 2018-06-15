from urllib import request

mp4_url = 'http://vali.cp31.ott.cibntv.net/youku/' \
          '6572ea18f04337143fe436c7e/' \
          '03000801005B19E55028BA1552FA5BD04B1B70-4A58-0' \
          '5E0-BA20-96EEA48A8F86.mp4?sid=052879182900010002577_00' \
          '_A4eb29018e2c491b8a6684e99c125b82d&sign=51bd10b8cd652e07d1' \
          'fceff35d7f73a8&ctype=50'

resp = request.urlretrieve(mp4_url, './imgs/aaa.mp4')
