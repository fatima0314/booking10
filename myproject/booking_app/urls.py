from django.urls import path, include
from .views import *
from rest_framework import  routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user_list')
router.register(r'hotel_list', HotelListViewSet, basename='hotel_list')
router.register(r'hotel_detail', HotelDetailViewSet, basename='hotel_detail')
router.register(r'hotel_image', HotelImageViewSet, basename='hotel_image')
router.register(r'room_list', RoomListViewSet, basename='room_list')
router.register(r'room_detail', RoomDetailViewSet, basename='room_detail')
router.register(r'room_images', RoomImageViewSet, basename='room_image')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'booking_list', BookingListViewSet, basename='booking_list')
router.register(r'booking_detail', BookingDetailViewSet, basename='booking_detail')



urlpatterns = [
    path('', include(router.urls))
]

