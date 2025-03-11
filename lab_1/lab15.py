from datetime import datetime
import calendar
class person:
    def __init__(self,name,country):
        self.name=name
        self.country=country
 
    def data(self):
        self.birthYear=int(input("please enter the birth year"))
        self.month=int(input("please enter birht month"))
        self.day=int(input("please enter the birth day"))
    
    def ageCalc(self):
        date=datetime.now()
        currentYear=int(date.year)
        currentMonth=int(date.month)
        currentDay=int(date.day)
        day=currentDay-self.day
        if day<0:
            currentMonth-=1
        month=currentMonth-self.month
        if month<0:
            month=12-month
            currentYear-=1
        year=currentYear-self.birthYear
        return year,month,day
Ram=person(input("Name: "),input("country: "))
Ram.data()
age=Ram.ageCalc()
print(f"The age is {age[0]} year {age[1]} month {age[2]} day")