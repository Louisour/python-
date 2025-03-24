import requests
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

response = requests.get(url)

with open('logo.png', 'wb')as file:
    file.write(response.content)
