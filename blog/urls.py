from django.urls import path
from . import views

# FBV CBV
# FBV (Function based view)
# CBV (Class based view)

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]
