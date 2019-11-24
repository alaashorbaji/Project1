from .models import Students,Subjects,Dr
from .serializer import SubjectsSerializer,StudentsSerializer,DrSerializer
from rest_framework import generics, status
class StudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class SubjectsList(generics.ListCreateAPIView):
        queryset = Subjects.objects.all()
        serializer_class = SubjectsSerializer

class SubjectsDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Subjects.objects.all()
        serializer_class = SubjectsSerializer

class DrList(generics.ListCreateAPIView):
            queryset = Dr.objects.all()
            serializer_class = DrSerializer
class DrDetail(generics.RetrieveUpdateDestroyAPIView):
            queryset = Dr.objects.all()
            serializer_class = DrSerializer