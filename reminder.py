#ФУНКЦИЯ выводит данные о днях рождениях на 7 дней, если она вызвана в понедельник, в том числе отображаются именинники на прошедших выходных(дополнительным блоком).
import datetime


def get_birthdays_per_week(birhtsday_list):  
      
    birthsdays={"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
    week_days={1:"Monday",2:"Tuesday", 3:"Wednesday",4:"Thursday",5:"Friday"}
 
    current_datetime = datetime.date.today() 
    print(current_datetime)
        
    end_week = current_datetime + datetime.timedelta(days=7)
 
    for name, date in birhtsday_list.items():  

        date= date.replace(year=current_datetime.isocalendar()[0]) #Приводим год к нынешнему
        
        if current_datetime <= date <= end_week or (current_datetime.isocalendar()[2] == 1 and current_datetime-datetime.timedelta(days=2)  <= date <= current_datetime):
            day = week_days.get(date.isocalendar()[2], 'Monday') #возвращает значение для ключа key, если ключ находится в словаре, если ключ отсутствует то вернет значение default "Monday"
            birthsdays[day].append(name)
          
    print("-----------------------------------------------------\nOUTPUT:\n")
    for day, person in birthsdays.items():
        
        if birthsdays[day]:
            print(f"{day}:{','.join(birthsdays[day])}") 

    return 
