
from django.contrib import admin
from django.urls import path
from blog import views as blog_views


urlpatterns = [
    # Single post route <pattern:variable>
    path('post/<slug:slug>/', blog_views.post),
    # Index page
    path('', blog_views.index),
    path('about/', blog_views.about),
    path('admin/', admin.site.urls),
]
