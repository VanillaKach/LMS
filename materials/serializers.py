from rest_framework import serializers
from .models import Course, Lesson

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()  # Новое поле

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lessons.count()  # Считаем количество уроков в курсе

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
