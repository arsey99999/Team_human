import os
import django
from .fetch import fetch_places
from .utils import process_places
from .models import Place

# ✅ Django 환경 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

def save_places():
    """네이버 API에서 데이터를 가져와 DB에 저장하는 함수"""
    queries = {
        "tourist": "부산 관광지",
        "restaurant": "부산 맛집",
        "cafe": "부산 카페"
    }

    places_to_add = []
    for category, query in queries.items():
        data = fetch_places(query, display=50)  # ✅ API에서 데이터 가져오기
        processed_places = process_places(data, category)  # ✅ 데이터 정제

        for place in processed_places:
            places_to_add.append(Place(
                name=place["name"],
                category=place["category"],
                address=place["address"],
                rating=place["rating"],
                review_count=place["review_count"],
                link=place["link"]
            ))

    if places_to_add:
        Place.objects.bulk_create(places_to_add, ignore_conflicts=True)  # ✅ DB에 저장
        print(f"✅ {len(places_to_add)}개 장소 데이터 추가 완료!")
    else:
        print("❌ 새로운 데이터 없음.")

if __name__ == "__main__":
    save_places()
