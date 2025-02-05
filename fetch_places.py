import os
import sys
import django

# ✅ 프로젝트 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ✅ Django 환경 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# ✅ 네이버 장소 데이터 저장 함수 실행
from naver_api.save import save_places

if __name__ == "__main__":
    print("✅ 네이버 API에서 데이터를 가져오는 중...")
    save_places()
    print("✅ 네이버 데이터 가져오기 완료!")