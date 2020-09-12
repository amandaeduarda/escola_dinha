from django.contrib import admin
from django.urls import path
from aluno.views import alunos

urlpatterns = [
    path('', alunos),
    path('admin/', admin.site.urls),
]
