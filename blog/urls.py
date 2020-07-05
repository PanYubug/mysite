from django.urls import path
from . import views
import blog.views

urlpatterns = [
    path('hello', views.hello_world),
    path('content', views.article_content),
    path('index', blog.views.get_index_page)
]
