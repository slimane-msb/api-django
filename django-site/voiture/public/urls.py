from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import home,signup,profile,login,logout,voiture,cle,garage

urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view() ,name="logout"),
    path("signup/", signup, name="signup"),
    path("profile/", profile, name="profile"),
    path("voiture/", voiture, name="voiture"),
    path("garage/", garage, name="garage"),
    path("cle/", cle, name= "cle"),
]