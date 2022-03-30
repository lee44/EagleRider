from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


def getLongLat(address):
    tf = TimezoneFinder()
    geolocator = Nominatim(user_agent="GetLoc")
    coords = geolocator.geocode(address)
    latitude = coords.latitude
    longitude = coords.longitude
    timezone = tf.timezone_at(lng=coords.longitude, lat=coords.latitude)
    return latitude, longitude
