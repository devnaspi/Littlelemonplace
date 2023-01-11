from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menuItemView.as_view()),
    path('menu/<int:pk>', views.singleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]



