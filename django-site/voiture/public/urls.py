from django.urls import path

from .views import home,signup,login,logout,voiture,cle,garage

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
    path("voiture/", voiture, name="voiture"),
    path("garage/", garage, name="garage"),
    path("cle/", cle, name= "cle"),
]