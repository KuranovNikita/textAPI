from django.urls import path
from .views import ArticleView, showtext
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api/', ArticleView.as_view()),
    path('text/', showtext),
]