from django.contrib import admin
from django.urls import path

from blog.views import BlogView, CategoryView, PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view()),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', PostView.as_view(), name='post')
]
