from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="Login"),
    path('logout/', views.logoutUser, name="logout"),
    path('clubs/logout/', views.logoutUser, name="logout"),
    path('gallery/logout/', views.logoutUser, name="logout"),
    path('', views.home, name="Home"),
    path('clubs/', views.clubs, name="Clubs"),
    path('gallery/', views.gallery, name="Gallery"),
    path('club1/', views.club1, name='club1'),
    path('club2/', views.club2, name='club2'),
    path('club3/', views.club3, name='club3'),
    path('club4/', views.club4, name='club4'),
    path('club5/', views.club5, name='club5'),
    path('club6/', views.club6, name='club6'),
    path('club7/', views.club7, name='club7'),
    path('club8/', views.club8, name='club8'),
    path('club9/', views.club9, name='club9'),
    path('club10/', views.club10, name='club10'),
    path('club11/', views.club11, name='club11'),
    path('club12/', views.club12, name='club12'),
    path('club13/', views.club13, name='club13'),
]