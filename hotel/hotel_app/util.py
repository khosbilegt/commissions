from datetime import datetime, timedelta
from django.db import transaction
from hotel_app.models import Room, RoomBooking, User

def process_dates_string(user_id, room_id, dates_string):
    date_list = dates_string.split("|")
    date_list.pop()

    # Convert date strings to datetime objects
    date_objects = [datetime.strptime(date, "%Y/%m/%d") for date in date_list]

    # Find the start and end dates
    start_date = date_objects[0]
    end_date = date_objects[-1] + timedelta(days=1)

    with transaction.atomic():
        # Create a single booking for the entire range
        room_booking = RoomBooking.objects.create(
            room_id=room_id,
            user_id=user_id,
            start_date=start_date.replace(hour=13, minute=0, second=0, microsecond=0),
            end_date=end_date.replace(hour=13, minute=0, second=0, microsecond=0),
            is_received=False  # Assuming the default value for is_received is False
        )

    return room_booking.booking_id
