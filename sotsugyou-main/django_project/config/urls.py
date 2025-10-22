"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
# include を追加し、後で meeting_rooms アプリのURLを組み込めるようにします

urlpatterns = [
    # 管理画面へのルーティング
    path('admin/', admin.site.urls),

    # ユーザー向けの予約システムへのルーティング（未実装）
    # path('', include('meeting_rooms.urls')),
]
