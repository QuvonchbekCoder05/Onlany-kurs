from rest_framework import serializers
from .models  import Instructor,Course,Lesson
from rest_framework.exceptions import ValidationError


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

    def validate_email(self, value):
        if '@' not in value:
            raise ValidationError("Email formati xato berilgan.")
        return value


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise ValidationError("Boshlanish sanasi tugash sanasidan oldinroq bo'lishi kerak.")
        return data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate_order(self, value):
        if value <= 0:
            raise ValidationError("Buyurtma ijobiy raqam bo'lishi kerak.")
        return value
