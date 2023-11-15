import requests

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='

road_type = 'ROAD' #도로명주소
road_type2 = 'PARCEL' #지번주소
address = '&address='
keys = '&key='
primary_key ='4E3C3F9D-14C3-3444-BF98-F95A5012A921'

def request_geo(road):
  page = requests.get(url+params+road_type+address+road+keys+primary_key)
  json_data = page.json()
  if json_data['response']['status'] == 'OK':
    x = json_data['response']['result']['point']['x']
    y = json_data['response']['result']['point']['y']
    return x,y
  else:
    x = 0
    y = 0
    return x,y
  
x,y = request_geo("경기도 시흥시 산기대학로 237 (정왕동, 한국산업기술대학교)")

print(f'x 값: {x}')
print(f'y 값: {y}')