def create_map_url(latitude, longitude, name=None):
    base_url = "https://map.kakao.com/link/map/"
    if name:
        url = f"{base_url}{name},{latitude},{longitude}"
    else:
        url = f"{base_url}{latitude},{longitude}"
    return url

def create_directions_url(latitude, longitude, name=None):
    base_url = "https://map.kakao.com/link/to/"
    if name:
        url = f"{base_url}{name},{latitude},{longitude}"
    else:
        url = f"{base_url}{latitude},{longitude}"
    return url

# 예시 사용
latitude = 37.402056
longitude = 127.108212
name = "카카오판교오피스"

map_url = create_map_url(latitude, longitude, name)
directions_url = create_directions_url(latitude, longitude, name)

print("Map URL:", map_url)
print("Directions URL:", directions_url)
