from django.urls import path
from .views import (
    CourseViewSet,
    LessonListView,
    LessonDetailView,
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView
)

# Для Course используем Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),
]

urlpatterns += router.urls
