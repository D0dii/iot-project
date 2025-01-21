from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='users'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('questions/', views.QuestionListCreate.as_view(), name='questions'),
    path('questions/<int:pk>/', views.QuestionRetrieveUpdateDestroy.as_view(), name='question-detail'),
    path('user-answers/', views.UserAnswerListCreate.as_view(), name='user-answers'),
    path('user-answers/<int:pk>/', views.UserAnswerRetrieveUpdateDestroy.as_view(), name='user-answer-detail'),
]
