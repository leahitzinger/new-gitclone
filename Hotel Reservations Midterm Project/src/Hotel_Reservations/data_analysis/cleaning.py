def cleaning(hotel):
    import pandas as pd    

    hotel['reservation_status_date']= pd.to_datetime(hotel['reservation_status_date'])
    hotel['arrival_date_month']=hotel['arrival_date_month'].astype('str')
    hotel['arrival_date_year']=hotel['arrival_date_year'].astype('str')
    hotel['arrival_date_day_of_month']=hotel['arrival_date_day_of_month'].astype('str')

    hotel['arrival_date']=[day+' '+month+' '+year for day,month,year in zip(hotel['arrival_date_day_of_month'],hotel['arrival_date_month'],hotel['arrival_date_year'])]

    hotel=hotel.drop(columns=['arrival_date_day_of_month','arrival_date_month'])

    import math
    hotel['direct_booking']=hotel.apply(lambda row : 'yes' if math.isnan(row['agent']) and math.isnan(row['company']) else 'no',axis=1)

    hotel['country']=hotel['country'].fillna('PRT')    
    hotel['children']=hotel['children'].fillna(0)
    hotel['agent']=hotel['agent'].fillna(0)
    hotel['company']=hotel['company'].fillna(0)
    
    return hotel
def change_type(df,col,type):
    df[col] = df[col].astype(type)
    return df
def filling_nans(df,col,what):
    df[col]=df[col].fillna(what)
    return df
    