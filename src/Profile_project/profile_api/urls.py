from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.UserProfileViewSet)
router.register("login", views.LoginViewSet, basename="login")
router.register("feed", views.UserProfileFeedItem)

urlpatterns = [
    path('hello_api/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
