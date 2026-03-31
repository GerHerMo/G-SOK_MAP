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
	        <meta charset="utf-8"/>
        	<title>Kakao 지도 시작하기</title>
        </head>
        <body>
        	<div id="map" style="width:500px;height:400px;"></div>
        	<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey={js_api_key}."></script>
        	<script>
        		var container = document.getElementById('map');
        		var options = {{
                center: new kakao.maps.LatLng(33.450701, 126.570667),
        			level: 3
        		}};

        		var map = new kakao.maps.Map(container, options);
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
