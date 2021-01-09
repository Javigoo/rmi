from rest_framework import serializers
from .models import *

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__' 

    description = serializers.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    date = serializers.DateField(required=False, format="%d-%m-%Y",)
    time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    location = serializers.CharField(max_length=MAX_UBICATION_LENGTH)

class GradeSerializer(serializers.Serializer):
    class Meta:
        model = StudentExam
        fields = '__all__'
        
    universityId = serializers.CharField(max_length=UNIVERSITY_ID_LENGTH)
    grade = serializers.IntegerField()