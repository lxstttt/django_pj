from django.urls import path

from app1 import views

urlpatterns = [
    path('fn1/', views.fn1),
    path('user2/', views.user.as_view()),
    path('user3/', views.UserView.as_view()),
    path("emp/", views.EmployeeView.as_view()),
    path("emp/<str:id>/", views.EmployeeView.as_view()),
]