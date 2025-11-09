from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cafe/<int:cafe_id>/', views.cafe_detail, name='cafe_detail'),
    path('review/<int:review_id>/vote/<str:vote_type>/', views.review_vote, name='review_vote'),
    path('edit/', views.edit_page, name='edit_page'),
    path('edit/add/', views.add_cafe, name='add_cafe'),
    path('edit/cafe/<int:cafe_id>/', views.edit_cafe, name='edit_cafe'),
    path('edit/cafe/<int:cafe_id>/delete/', views.delete_cafe, name='delete_cafe'),
]
