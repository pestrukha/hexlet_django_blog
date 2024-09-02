from django.urls import path
from .views import IndexView, ArticleView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_detail'),
]