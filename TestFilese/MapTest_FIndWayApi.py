import requests
import json

def get_kakao_api(start_lat, start_lng, end_lat, end_lng, api_key):
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