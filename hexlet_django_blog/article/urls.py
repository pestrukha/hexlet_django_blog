from django.urls import path
from .views import IndexView, ArticleView, ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view(), name='article_detail'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]