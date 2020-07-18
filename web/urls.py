from django.urls import path
from web import views

urlpatterns = [
    path('', views.main),
    path('publication/<int:pub_id>', views.publication),
    path('post', views.post),
    path('publication/<int:pub_id>/comment', views.comment),
]
