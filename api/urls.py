from django.urls import path, include
from .views import RocketList, RocketDetail, RocketCreate, RocketEdit, RocketDelete, MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rocket/', RocketList.as_view()),
    path('rocket/<int:pk>', RocketDetail.as_view()),
    path('rocket/create/', RocketCreate.as_view()),
    path('rocket/update/<int:pk>', RocketEdit.as_view()),
    path('rocket/delete/<int:pk>', RocketDelete.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]