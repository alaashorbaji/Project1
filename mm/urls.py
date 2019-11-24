from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from student import views
schema_view = get_swagger_view(title='welcome')

urlpatterns = [
    path(r'', schema_view),
    path('students/', views.StudentsList.as_view()),
    path('students/<int:pk>', views.StudentsDetail.as_view()),
    path('admin/', admin.site.urls),
    path('subjects/', views.SubjectsList.as_view()),
    path('subjects/<int:pk>', views.SubjectsDetail.as_view()),
    path('dr/', views.DrList.as_view()),
    path('dr/<int:pk>', views.DrDetail.as_view()),
    path(r'api-auth/', include('rest_framework.urls')),





]
