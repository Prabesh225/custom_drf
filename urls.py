from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sets import views

from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('get_token/', CustomToken.as_view(), name='custom-token'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token-obtain-pair'),  # new endpoint to obtain access and refresh tokens
]
