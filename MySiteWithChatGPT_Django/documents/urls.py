from django.contrib import admin
from django.urls import path, include
from MySiteWithChatGPT_Django.documents import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('documents/', views.document_list, name='document_list'),
]
