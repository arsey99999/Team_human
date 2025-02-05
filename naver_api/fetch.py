import json
import requests
import os

# ✅ 네이버 API 키 불러오기
config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
with open(config_path, "r") as config_file:
    config = json.load(config_file)
    NAVER_CLIENT_ID = config["NAVER_CLIENT_ID"]
    NAVER_CLIENT_SECRET = config["NAVER_CLIENT_SECRET"]

# ✅ 네이버 API를 사용하여 장소 정보 가져오기
def fetch_places(query, display=50):
    """네이버 API에서 장소 데이터를 가져오는 함수"""
    url = "https://openapi.naver.com/v1/search/local.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }
    params = {"query": query, "display": display, "start": 1, "sort": "random"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"❌ 네이버 API 호출 실패: {response.status_code}")
        return []
