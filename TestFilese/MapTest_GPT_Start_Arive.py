import requests
import pandas as pd
import numpy as np
import folium
from folium.plugins import MiniMap

# 카카오 API
def elec_location(region, page_num):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region, 'page': page_num}
    headers = {"Authorization": "KakaoAK fab52d17b3e6b3db4b52bb786c369395"}

    response = requests.get(url, params=params, headers=headers)
    response_json = response.json()
    places = response_json['documents']
    total = response_json['meta']['total_count']
    if total > 45:
        print(total, '개 중 45개 데이터밖에 가져오지 못했습니다!')
    else:
        print('모든 데이터를 가져왔습니다!')
    return places

def elec_info(places):
    X = []
    Y = []
    stores = []
    road_address = []
    place_url = []
    ID = []
    for place in places:
        X.append(float(place['x']))
        Y.append(float(place['y']))
        stores.append(place['place_name'])
        road_address.append(place['road_address_name'])
        place_url.append(place['place_url'])
        ID.append(place['id'])

    ar = np.array([ID, stores, X, Y, road_address, place_url]).T
    df = pd.DataFrame(ar, columns=['ID', 'stores', 'X', 'Y', 'road_address', 'place_url'])
    return df

def keywords(location_name):
    df = None
    for loca in location_name:
        for page in range(1, 4):
            local_name = elec_location(loca, page)
            local_elec_info = elec_info(local_name)

            if df is None:
                df = local_elec_info
            elif local_elec_info is None:
                continue
            else:
                df = pd.concat([df, local_elec_info], join='outer', ignore_index=True)
    return df

def make_map(dfs, start, end):
    # 지도 생성하기
    m = folium.Map(location=[33.4935, 126.6266],   # 기준좌표: 제주어딘가로 내가 대충 설정
                   zoom_start=12)

    # 미니맵 추가하기
    minimap = MiniMap()
    m.add_child(minimap)

    # 마커 추가하기
    for i in range(len(dfs)):
        folium.Marker([float(dfs['Y'][i]), float(dfs['X'][i])],
                      tooltip=dfs['stores'][i],
                      popup=dfs['place_url'][i],
                      icon=folium.Icon(color='blue')
                      ).add_to(m)

    # 출발지와 목적지 추가하기
    folium.Marker(start, tooltip='출발지', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(end, tooltip='목적지', icon=folium.Icon(color='red')).add_to(m)

    # 출발지와 목적지 연결하기
    folium.PolyLine(locations=[start, end], color='red', weight=2.5, opacity=1).add_to(m)

    return m

location = ['대동역 7번 출구', '목포시 갓바위']
df = keywords(location)
df = df.drop_duplicates(['ID'])
df = df.reset_index(drop=True)

# 출발지와 목적지 설정
start = [33.4607, 126.9364]  # 예시 좌표 (출발지)
end = [33.5097, 126.4913]    # 예시 좌표 (목적지)

map_object = make_map(df, start, end)
map_object.save('map_start_arrive.html')

# 맵을 시각화하기 위해 웹 브라우저에서 'map.html' 파일을 열 수 있습니다.
