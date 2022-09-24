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
    l_saturday=[]
    l_sunday=[]

    birthsdays={"Monday":monday, "Tuesday":tuesday, "Wednesday":wednesday, "Thursday":thusday, "Friday":friday, "Saturday":saturday, "Sunday":sunday}
    l_birthsdays={"Last Saturday":l_saturday, "Last Sunday":l_sunday}
    week_days={1:"Monday",2:"Tuesday", 3:"Wdnesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
 
    current_datetime = datetime.date.today() 
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

            if date == marker_l_sun:
                l_sunday.append(name)
            if date == marker_l_sat:
                l_saturday.append(name)
    
    #OUTPUT-----"THIS WEEK"--------------------
    print("-----------------------------------------------------\nOUTPUT:\n")
    for day, person in birthsdays.items():
        
        if birthsdays[day]:
            print(f"{day}:{','.join(birthsdays[day])}") 
    #------------------------------
    
    #OUTPUT-----"LAST WEEKEND"-----------------
    if l_saturday or l_sunday:
        print("-----------------------------------------------------\n")
        for day, person in l_birthsdays.items():
            if l_birthsdays[day]:
                print(f"{day}:{','.join(l_birthsdays[day])}")
    #------------------------------
    print(birthsdays)
    return 




#birhtsday_list={"Daria":datetime.date(year=1990, month=9, day=24), "Pavel":datetime.date(year=1990, month=9, day=25), "Natali":datetime.date(year=1990, month=9, day=25), "Sam":datetime.date(year=1990, month=9, day=29)}
#print("input data dic:",birhtsday_list)

#get_birthdays_per_week(birhtsday_list)
