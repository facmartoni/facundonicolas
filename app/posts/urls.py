# Django

from django.urls import path

# Own

from posts import views

urlpatterns = [
    path(
        route='',
        view=views.HomeView.as_view(),
        name='home'
    )
]
