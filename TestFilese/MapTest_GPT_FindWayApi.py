import requests
import json

def get_route_from_kakao_api(start_lat, start_lng, end_lat, end_lng, api_key):
    url = "https://apis-navi.kakaomobility.com/v1/directions"

    headers = {
        "Authorization": f"KakaoAK {api_key}"
    }

    params = {
        "origin": f"{start_lng},{start_lat}",
        "destination": f"{end_lng},{end_lat}",
        "waypoints": "",
        "priority": "RECOMMEND",
        "car_fuel": "GASOLINE",
        "car_hipass": False
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None

def save_route_to_html(route_data, start_lat, start_lng, end_lat, end_lng, js_api_key):
    with open('route_map.html', 'w', encoding='utf-8') as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>경로 표시 지도</title>
            <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey={js_api_key}&libraries=services"></script>
        </head>
        <body>
            <div id="map" style="width:100%;height:500px;"></div>
            <script>
                var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
                    mapOption = {{
                        center: new kakao.maps.LatLng({start_lat}, {start_lng}), // 지도의 중심좌표
                        level: 7 // 지도의 확대 레벨
                    }}; 

                var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

                // 출발지 마커
                var startMarker = new kakao.maps.Marker({{
                    position: new kakao.maps.LatLng({start_lat}, {start_lng}),
                    map: map,
                    title: '출발지'
                }});

                // 도착지 마커
                var endMarker = new kakao.maps.Marker({{
                    position: new kakao.maps.LatLng({end_lat}, {end_lng}),
                    map: map,
                    title: '도착지'
                }});

                // 경로 폴리라인
                var linePath = {route_data};

                var path = linePath.map(function(coord) {{
                    return new kakao.maps.LatLng(coord[0], coord[1]);
                }});

                var polyline = new kakao.maps.Polyline({{
                    path: path,
                    strokeWeight: 5,
                    strokeColor: '#FF0000',
                    strokeOpacity: 0.7,
                    strokeStyle: 'solid'
                }});

                polyline.setMap(map);
            </script>
        </body>
        </html>
        """)

# 예시 좌표 (서울역에서 강남역까지)
start_lat = 37.5562
start_lng = 126.9723
end_lat = 37.4979
end_lng = 127.0276
api_key = "fab52d17b3e6b3db4b52bb786c369395"
js_api_key = "3e82e4c9e67d0cfde4ca2c11723f094b"

route_data = get_route_from_kakao_api(start_lat, start_lng, end_lat, end_lng, api_key)
if route_data:
    # 경로 데이터 추출
    line_path = []
    for section in route_data['routes'][0]['sections']:
        for road in section['roads']:
            for vertex in road['vertexes']:
                if isinstance(vertex, list) and len(vertex) == 2:
                    line_path.append([vertex[1], vertex[0]])

    save_route_to_html(json.dumps(line_path), start_lat, start_lng, end_lat, end_lng, js_api_key)
    print("route_map.html 파일이 생성되었습니다.")
else:
    print("API 요청 실패")
