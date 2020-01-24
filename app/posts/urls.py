# Django

from django.urls import path

# Own

from posts import views

urlpatterns = [
    path(
        route='',
        view=views.home_view,
        name='home'
    ),
    path(
        route='confirmation',
        view=views.confirmation_view,
        name='confirmation'
    ),
    path(
        route='blog/<str:slug>',
        view=views.post_detail,
        name='post_detail'
    ),
    path(
        route='blog/tag/<str:slug>',
        view=views.tag_detail,
        name='tag'
    ),
]
