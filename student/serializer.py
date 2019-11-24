from rest_framework import serializers
from .models import Students,Subjects,Dr

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=['id','S_name','Sub_name','Dr_name']
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields=['id','Sub_name','Dr_name']
class DrSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dr
        fields=['id','Dr_name']



