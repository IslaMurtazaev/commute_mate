from math import radians, sin, cos, sqrt, atan2
import requests
from django.conf import settings

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points using the Haversine formula.
    Returns distance in miles.
    """
    R = 3959  # Earth's radius in miles

    # Convert coordinates to radians
    lat1, lon1, lat2, lon2 = map(radians, [float(lat1), float(lon1), float(lat2), float(lon2)])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance

def send_push_notification(expo_push_token, title, body, data=None):
    """
    Send push notification using Expo's push notification service
    """
    messages = [{
        'to': expo_push_token,
        'sound': 'default',
        'title': title,
        'body': body,
        'data': data or {}
    }]
    
    response = requests.post(
        'https://exp.host/--/api/v2/push/send',
        json=messages,
        headers={
            'Accept': 'application/json',
            'Accept-encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
        }
    )
    
    return response.json() 