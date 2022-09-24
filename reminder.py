#ФУНКЦИЯ выводит данные о днях рождениях на ТЕКУЩЕЙ неделе, если она вызвана в понедельник, в том числе отображаются именинники на прошедших выходных(дополнительным блоком).
import datetime


def get_birthdays_per_week(birhtsday_list):
   
    mon=[]
    tue=[]
    wed=[]
    thu=[]
    fri=[]
    sat=[]
    sun=[]
    l_sat=[]
    l_sun=[]

    dic={"Monday":mon, "Tuesday":tue, "Wednesday":wed, "Thursday":thu, "Friday":fri, "Saturday":sat, "Sunday":sun}
    l_dic={"Last Saturday":l_sat, "Last Sunday":l_sun}
 
    current_datetime = datetime.date.today() 
    #current_datetime = datetime.date(2022,9,26) #Тестовая дата
    current_datetime_wday = current_datetime.weekday() # Mon====0
    current_datetime_week=current_datetime.isocalendar()[1]
   
    #print("Current date:",current_datetime)
    #print("Current weekday:",current_datetime_wday)
    #print("Current week No.:",current_datetime_week)
    
    start_week = current_datetime - datetime.timedelta(days=current_datetime_wday)
    end_week = start_week + datetime.timedelta(days=6)
 

    for name, date in birhtsday_list.items():  

        date= date.replace(year=current_datetime.isocalendar()[0]) #Приводим год к нынешнему
        #print(date)

        if start_week <= date <= end_week:
            
            if date.isocalendar()[2] == 1: #Monday 1
                #print("Monday")
                
                mon.append(name)

            if date.isocalendar()[2] == 2: #Tuesday 2
                #print("Tuesday")
                
                tue.append(name)

            if date.isocalendar()[2] == 3: #Wednesday 3
                #print("Wednesday")
                
                wed.append(name)

            if date.isocalendar()[2] == 4: #Thursday 4
                #print("Thursday")
                
                thu.append(name)

            if date.isocalendar()[2] == 5: #Friday 5
                #print("Friday")
                
                fri.append(name)

            if date.isocalendar()[2] == 6: #Saturday 6
                #print("Saturday")
                
                sat.append(name)

            if date.isocalendar()[2] == 7: #Sunday 7
                #print("Sunday")

                sun.append(name)

        #------- weekend birthsdays-------
        if current_datetime_wday == 0:
            marker_l_sun=current_datetime-datetime.timedelta(days=1)
            marker_l_sat=current_datetime-datetime.timedelta(days=2)    

            if date == marker_l_sun:
                l_sun.append(name)
            if date == marker_l_sat:
                l_sat.append(name)
    
    #OUTPUT-----"THIS WEEK"--------------------
    print("-----------------------------------------------------\nOUTPUT:\n")
    for day, person in dic.items():
        
        if dic[day]:
            print(f"{day}:{','.join(dic[day])}") 
    #------------------------------
    
    #OUTPUT-----"LAST WEEKEND"-----------------
    if l_sat or l_sun:
        print("-----------------------------------------------------\n")
        for day, person in l_dic.items():
            if l_dic[day]:
                print(f"{day}:{','.join(l_dic[day])}")
    #------------------------------
    
    return 




birhtsday_list={"Daria":datetime.date(year=1990, month=9, day=24), "Pavel":datetime.date(year=1990, month=9, day=25), "Natali":datetime.date(year=1990, month=9, day=25), "Sam":datetime.date(year=1990, month=9, day=29)}
print("input data dic:",birhtsday_list)

get_birthdays_per_week(birhtsday_list)