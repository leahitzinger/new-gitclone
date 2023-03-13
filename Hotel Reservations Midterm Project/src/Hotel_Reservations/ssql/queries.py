import sys
sys.path.insert(0, 'C:/Users/admin/Documents/new repo/new-gitclone/Hotel Reservations Midterm Project/src/Hotel_Reservations')
from ssql.database_actions import query
from entities.Reservation import * 

def get_top_agents_reservations_in_country(country):
    
    query1='''with TopAgent as
        (select top 1 agent, count(*) as amount from Reservation r 
        left join Guest g
        on g.GuestId=r.GuestId
        where g.country=' '''+country+''' 'and agent!=0
        group by agent
        Order by amount desc)
        select top 10 r.* from Reservation as r
        join TopAgent t
        on t.agent=r.agent
        join Guest g
        on g.GuestId=r.GuestId where g.country=' '''+country+''' ';'''
    result=query(query1)
    guests=[Reservation(each) for each in result]
    return guests



def View_reservations_guests(year,low_range,high_range):
    query2='''select r.*,g.* from Reservation r
        join Guest g
        on g.GuestId=r.GuestId 
        where r.arrival_date_year='''+year+''' and r.adr>'''+low_range+''' and r.adr<'''+high_range+''' and r.is_canceled=1'''
    result=query(query2)
    guests=[Reservation(each) for each in result]
    return guests
            
            
def whether_children_impacts_number_nights():
    query3='''select g.children, avg(r.stays_in_week_nights) as 'avg stay in weekend',avg(r.stays_in_weekend_nights) as 'avg stay in week' from Reservation r
    join Guest g
    on g.GuestId=r.GuestId 
    group by g.children'''
    return query3