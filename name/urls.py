from django.contrib import admin
from django.urls import path, include
from django.views import View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todolist_app.urls')),
    path('', include('home_page.urls')),
    path('contacts/', include('contacts.urls')),
    path('account/', include('users_app.urls')),
]
