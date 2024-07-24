from django.urls import path
from. import views
urlpatterns = [
    path('index/',views.indexfun,name='indexfun'),
    path('aboutpg/', views.aboutpg, name='aboutpg'),
    path('resume/', views.resume, name='resume'),
    path('cert/', views.cert, name='cert'),
    path('cont/', views.cont, name='cont')
]
