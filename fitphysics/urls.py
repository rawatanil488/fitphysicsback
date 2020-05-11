from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# views
from fitphysics.profiles.api import UserProfileDetails
from fitphysics.blogs.api import BlogDetails, CreateNewBlog

schema_view = get_schema_view(
   openapi.Info(
      title="FitnessPhysics API",
      default_version='v1',
      description="Fitnessphysics APIs described",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', UserProfileDetails.as_view(), name='store_owner_details'),
    path('api/blogs/', BlogDetails.as_view(), name='blogs'),
    path('api/blogs/create/', CreateNewBlog.as_view({"post": "create"}), name='create_new_blogs')
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
