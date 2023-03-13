import logging
import os
import sys
sys.path.insert(0, 'C:/Users/admin/Documents/new repo/new-gitclone/Hotel Reservations Midterm Project/src/Hotel_Reservations')
import pandas as pd
from data_analysis.cleaning  import cleaning
from ssql.database_actions import create_tables_from_df
from ssql.queries import *

CURR_DIR = os.path.dirname(__file__)
LOG_FOLDER = CURR_DIR + '/logs'

logging.basicConfig(filename= LOG_FOLDER +'/my_Hotel_logs.txt',
filemode='a+',
format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
datefmt='%Y-%m-%d %H:%M:%S',
#datefmt='%H:%M:%S',
level=logging.INFO)


# hotel=pd.read_csv('C:/Users/admin/Documents/new repo/new-gitclone/Hotel Reservations Midterm Project/src/Hotel_Reservations/hotel_bookings.csv')
# hotel_cleaned=cleaning(hotel)
# create_tables_from_df(hotel_cleaned)
def main():
        menu_choice = None
        while menu_choice != 0:
                menu_choice=get_menu_choice()
                try:
                        if menu_choice == 1:        
                                country=input('Which country would you like to select?')
                                q_result=get_top_agents_reservations_in_country(country)
                                for each in q_result:
                                        print(each)
                                logging.info('The customer got info for the top agent in {}.'.format(country))
                        elif menu_choice == 2:        
                                year=input('What year would you like to get your info for?')
                                low_range=input('from what price range would you like to get your info for')
                                high_range=input('untill what price range would you like to get your info for')
                                logging.info('The customer got info for {} for price range {}-{} .'.format(year,low_range,high_range))
                
                        elif menu_choice == 3:
                                a=whether_children_impacts_number_nights()
                                print(a)
                                logging.info('The customer got info whether children impacts number nights .')  
                        elif menu_choice == 0:
                                pass
                except Exception as ex:
                        print('error' +str(ex))
                        logging.error('error' +str(ex))
        # hotel=pd.read_csv('hotel_bookings.csv', na_values=['none','undefined','','-'])
  
        
#         create_tables_from_df(hotel)
def get_menu_choice():
    menu = "\n1. View the best agent's top 10 reservations + guests in a specific country"
    menu +=	"\n2.  View reservations + guests that were not canceled that are within a specific price range  for a specific year." 
    menu +=	"\n3. whether the number of children impacts the number of nights" 
    choice = input(menu + "\nPlease enter 1-3 (or 0 to exit): ")
    return int(choice)

        
    
if __name__ =="__main__":
        main()
