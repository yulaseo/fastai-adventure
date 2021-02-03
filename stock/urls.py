from stock import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StockView

#app_name='stock'

home = StockView.as_view({
    'post': 'create',
    'get': 'list'
})
stock_detail = StockView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', home, name='home'),
    path('stock/<stock_code>/', stock_detail, name='stock_detail'),
])

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('home/', views.home, name='home'),
#     path('bookmark/', views.bookmark, name='bookmark'), # 비회원 북마크
#     path('bookmark/<int:user_id>/', views.bookmark, name='bookmark'), # 회원 북마크
#     path('bookmark-list/', views.bookmark_list, name='bookmark_list'),
#     path('bookmark-list/<int:user_id>/', views.bookmark_list, name='bookmark_list'),
#     path('market/', views.market, name='market'),
#     path('market-list/', views.market_list, name='market_list'),
#     path('stock/<stock_code>/', views.stock_detail, name='stock_detail'),
#     path('api_test/', views.api_test, name='api_test'),
#     path('search/', views.home, name='search'),
# ]