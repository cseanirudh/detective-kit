from django.urls import path
from .import views

urlpatterns = [
path('', views.index, name='index'),
path('about', views.about, name='about'),
path('covidu', views.covidu, name='covidu'),
path('ucovedit', views.ucovedit, name='ucovedit'),
path('uucovedit/<int:id>/', views.uucovedit, name='uucovedit'),
path('addstate', views.addstate, name='addstate'),
path('self', views.self, name='self'),
path('alogin', views.alogin, name='alogin'),
path('logout', views.Logout, name='logout'),
path('register', views.register, name='register'),
path('login', views.Login, name='login'),
path('alltest', views.alltest, name='alltest'),
path('allreg', views.allreg, name='allreg'),
path('user', views.userdetail, name='user'),
path('covid', views.covid, name='covid'),
    ]