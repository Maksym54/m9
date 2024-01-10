from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quotes/', include('quotes_app.urls')),  # Тут вказуємо шлях до наших url-ів з додатку
]