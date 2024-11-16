from .models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['first_name', 'last_name']



class HotelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']



class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'hotel_image']



class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'room_image']




class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
         model = Room
         fields = ['id', 'room_number', 'room_type', 'room_status', 'room_price', 'all_inclusive', 'room_images']



class ReviewSimpleSerializer(serializers.ModelSerializer):
    user_name= UserSimpleSerializer()
    class Meta:
         model = Review
         fields = ['user_name', 'text', 'stars', 'parent']



class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserSimpleSerializer()
    hotel = HotelSimpleSerializer()
    class Meta:
         model = Review
         fields = ['id', 'user_name', 'hotel', 'text', 'stars', 'parent']



class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields =  ['id', 'hotel_name', 'country', 'city', 'average_rating','hotel_images']


    def get_average_rating(self, obj):
        return obj.get_average_rating()



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images =  HotelImageSerializer(many=True, read_only=True)
    reviews = ReviewSimpleSerializer(many=True, read_only=True)
    owner =  UserSimpleSerializer()
    rooms = RoomListSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'owner', 'description', 'country', 'city', 'address',
                  'reviews','average_rating', 'hotel_stars', 'hotel_video', 'hotel_images', 'rooms']


    def get_average_rating(self, obj):
         return obj.get_average_rating()




class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_number',  'room_type', 'room_images',
                  'room_status', 'room_price', 'all_inclusive', 'room_description']
