from django.contrib import admin
from django.urls import path, include  # Добавлен import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MySiteWithChatGPT_Django.documents.urls')),  # Подключение urls из documents
]
