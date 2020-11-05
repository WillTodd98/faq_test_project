"""kubrick_faq_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, questions_view
from faq_log.views import question_lookup_view, question_create_view, question_delete_view, question_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
    path('questions/<int:my_id>/', question_lookup_view, name='questions-detail'),
    path('questionslist', question_list_view, name="questionlist"),
    path('submissions', question_create_view, name='submissons'),
    path('questions/<int:my_id>/delete/', question_delete_view, name="question-delete"),
]
