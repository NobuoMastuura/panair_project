# views.pyに記述したコードを呼ぶためには
# このファイル（urls.py）にコードを記述する必要がある
from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'school_admin'

urlpatterns = [
    # メニュー画面
    url(r'^$', views.index, name='index'),
    # レッスン受講記録
    path('attend/', views.attend, name='attend'),
    # レッスン記録
    path('attend/add_attend/', views.add_attend, name='add_attend'),
    # レッスン更新
    path('update_attend/<int:pk>/', views.update_attend, name='update_attend'),
    # ユーザー一覧画面
    path('user/', views.user, name='user'),
    # ユーザー登録画面
    path('users/add_user/', views.add_user, name='add_user'),
    # ユーザー編集画面
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    # 請求画面
    path('invoice_list/', views.invoice_list, name='invoice_list'),
    # レポート画面
    path('report/', views.report, name='report'),
]
