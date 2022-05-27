from django.urls import path

from . import views

app_name = 'hamch'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('category-create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('count_up_try/<int:pk>', views.CountUpTryView.as_view(), name='count_up_try'),
    path('count_up_try_done/<int:pk>', views.CountUpTryDoneView.as_view(), name='count_up_try_done'),
    path('search/', views.SearchView.as_view(), name='search'),
]