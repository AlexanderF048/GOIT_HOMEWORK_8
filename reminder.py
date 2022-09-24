#ФУНКЦИЯ выводит данные о днях рождениях на ТЕКУЩЕЙ неделе, если она вызвана в понедельник, в том числе отображаются именинники на прошедших выходных(дополнительным блоком).
import datetime


def get_birthdays_per_week(birhtsday_list):
   
    monday=[]
    tuesday=[]
    wednesday=[]
    thusday=[]
    friday=[]
    saturday=[]
    sunday=[]
    

    birthsdays={"Monday":monday, "Tuesday":tuesday, "Wednesday":wednesday, "Thursday":thusday, "Friday":friday, "Saturday":saturday, "Sunday":sunday}
    
    week_days={1:"Monday",2:"Tuesday", 3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
 
    current_datetime = datetime.date.today() 
    ##current_datetime = datetime.date(2022,9,26) #Тестовая дата
    current_datetime_wday = current_datetime.weekday() # Mon====0
    
  
    start_week = current_datetime - datetime.timedelta(days=current_datetime_wday)
    end_week = start_week + datetime.timedelta(days=4)
 

    for name, date in birhtsday_list.items():  

        date= date.replace(year=current_datetime.isocalendar()[0]) #Приводим год к нынешнему
        #print(date)

        if start_week <= date <= end_week:
            
            day=week_days[date.isocalendar()[2]]
            birthsdays[day].append(name)
          
        #------- weekend birthsdays-------
        if current_datetime_wday == 0:
            marker_l_sun=current_datetime-datetime.timedelta(days=1)
            marker_l_sat=current_datetime-datetime.timedelta(days=2)    

            if date == marker_l_sun or date == marker_l_sat:
                monday.append(name)
            
    
    #OUTPUT-----"THIS WEEK"--------------------
    print("-----------------------------------------------------\nOUTPUT:\n")
    for day, person in birthsdays.items():
        
        if birthsdays[day]:
            print(f"{day}:{','.join(birthsdays[day])}") 
    #------------------------------
    
   
    #print(birthsdays)
    return 




#birhtsday_list={"Daria":datetime.date(year=1990, month=9, day=24), "Pavel":datetime.date(year=1990, month=9, day=28), "Natali":datetime.date(year=1990, month=9, day=25), "Sam":datetime.date(year=1990, month=9, day=29)}
#print("input data dic:",birhtsday_list)

#get_birthdays_per_week(birhtsday_list)
