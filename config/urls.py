from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/',include('students.urls')),
    path('api/staffs/',include('staffs.urls')),
    path('api/courses/',include('courses.urls')),
    path('api/batches/',include('batches.urls')),
    path('api/enrollment/',include('enrollments.urls'))
]

