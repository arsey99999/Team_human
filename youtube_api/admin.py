from django.contrib import admin
<<<<<<< HEAD
from .models import YouTubeVideo, Place  # Place 모델 추가
=======
from .models import YouTubeVideo, Place
>>>>>>> d5b8ffb63ce002a17e6bb23b1b2bc58ce2d63ac0
from naver_api.models import Place

@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id', 'published_date')
    search_fields = ('title', 'description')

@admin.register(Place)  # Place 모델 등록
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address', 'rating')  # 'review_count' 제거
    search_fields = ('name', 'address')  # 검색 필드
    list_filter = ('category',)  # 카테고리별 필터 추가