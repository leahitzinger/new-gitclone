    # some_file.py

    # caution: path[0] is reserved for script path (or '' in REPL)


import sys
sys.path.insert(0, 'C:/Users/admin/Documents/new repo/new-gitclone/Hotel Reservations Midterm Project/src/Hotel_Reservations')

from enums_1.deposit_type import DepositType
from enums_1.Hotel import Hotel
from enums_1.type import Type
from enums_1.meals import Meals
from entities.Guest import guest
import pandas as pd
class Reservation():
    def __init__(self,row):
        self.enum_hotel_name=Hotel[row['hotel'].upper().replace(' ', '_')]
        self.b_was_canaled=row['is_canceled']
        self.i_lead_time=row['lead_time']
        self.s_year_arrival=['arrival_date_year']
        self.i_week_into_year=row['arrival_date_week_number']
        self.i_num_of_weekend_nights=row['stays_in_weekend_nights']
        self.i_num_of_week_nights=row['stays_in_week_nights'] 
        self.s_meals=Meals[row['meal'].upper().replace(' ', '_')]
        self.s_market_segment=row['market_segment']
        self.s_distribution_channel=row['distribution_channel']
        self.i_is_repeated_guest=row['is_repeated_guest']
        self.i_previous_cancellations=row['previous_cancellations']
        self.i_previous_bookings_not_canceled=row['previous_bookings_not_canceled']
        self.s_reserved_room_type=row['reserved_room_type']
        self.s_assigned_room_type=row['assigned_room_type']
        self.i_booking_changes=row['booking_changes']
        self.enum_deposit_type= DepositType[row['deposit_type'].upper().replace(' ', '_')]
        self.n_agent=row['agent']
        self.n_company=row['company']
        self.n_days_in_waiting_list=row['days_in_waiting_list']
        self.s_customer_type=Type[row['customer_type'].upper.replace('-', '_')]
        self.n_adr=row['adr']
        self.i_required_car_parking_spaces=row['required_car_parking_spaces']
        self.i_total_of_special_requests=row['total_of_special_requests']
        self.s_reservation_status=row['reservation_status']
        self.s_arrival_date=row['arrival_date']
        self.d_reservation_status_date=row['reservation_status_date ']
        self.s_direct_booking=row['direct_booking']        
        self.o_guest=guest(row)
    def __str__(self):
        return ' Hotel name:{}\n arrival date:{}\n car parking:{}\n costumer type:{}\n num of week nights:{}\n num of weekend nights:{}'.format(self.enum_hotel_name,self.s_arrival_date,self.i_required_car_parking_spaces,self.s_customer_type,self.i_num_of_week_nights,self.i_num_of_weekend_nights)    
        
