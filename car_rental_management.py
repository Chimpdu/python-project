from datetime import datetime,timedelta
import math
def menu():
    while True:
        print("You may select one of the following:\n1) List available cars\n2) Rent a car\n\
3) Return a car\n4) Count the money\n0) Exit")
        selection=int(input("What is your selection?\n"))
        if selection==1:
            list_available_cars()
        elif selection==2:
            rent_car()
        elif selection==3:
            return_car()
        elif selection==4:
            count_money()
        elif selection==0:
            break
        else:
            print("Invalid selection, try again.")

def get_all_cars_info():
    f=open("Vehicles.txt",'r')
    all_cars_list=[]
    while True:
        cars_str=f.readline().strip("\n")
        if len(cars_str)<=0:
            break
        else:
            cars_list=cars_str.split(",")
            all_cars_list.append(cars_list)
    f.close()
    return all_cars_list

def get_all_reg_nr():
    all_cars_info=get_all_cars_info()
    all_reg_nr=[]
    for car in all_cars_info:
        all_reg_nr.append(car[0])
    return all_reg_nr
    
def get_rented_cars_info():
    f=open("RentedVehicles.txt",'r')
    rented_cars_info=[]
    while True:
        rented_cars_str=f.readline().strip("\n")
        if len(rented_cars_str)<=0:
            break
        else:
            rented_cars_info.append(rented_cars_str.split(","))
    f.close()
    return rented_cars_info


def get_rented_reg_nr():
    rented_cars_info=get_rented_cars_info()
    rented_car_number_list=[]
    for rented_car in rented_cars_info:
        rented_car_number_list.append(rented_car[0])
    return rented_car_number_list

def get_customers_info():
    f=open('Customers.txt',"r")
    customers_info=[]
    while True:
        customer_info_str=f.readline().strip("\n")
        if len(customer_info_str)<=0:
            break
        else:
            customer_list=customer_info_str.split(",")
            customers_info.append(customer_list)
    return customers_info

def get_customers_birthday():
    customers=get_customers_info()
    existing_birthdays=[]
    for customer in customers:
        existing_birthdays.append(customer[0])
    return existing_birthdays

def add_new_customer(birthday,firstname,surname,email):
    f=open("Customers.txt",'a')
    new_info=birthday+","+firstname+","+surname+","+email
    f.write(new_info)
    f.close()

def add_new_rented_car(reg_nr,birthday):
    f=open("RentedVehicles.txt",'a')
    all_cars=get_all_cars_info()
    for car in all_cars:
        if reg_nr==car[0]:
            time=datetime.now()
            now=time.strftime("%d/%m/%Y %H:%M")
            content=car[0]+","+birthday+","+now
            f.write(content)
    f.close()

def add_new_transaction(reg_nr,birthday,start_time,end_time,daily_price):
    start=datetime.strptime(start_time,"%d/%m/%Y %H:%M")
    duration=math.floor((end_time-start).total_seconds()/60/60/24)
    end_time_str=end_time.strftime("%d/%m/%Y %H:%M")
    total_money=duration*int(daily_price)
    f=open("transActions.txt",'a')
    data="{},{},{},{},{},{:.2f}".format(reg_nr,birthday,start_time,end_time_str,duration,total_money)
    f.write(data)
    f.close()

def remove_rented_cars(reg_nr):
    all_infos=get_rented_cars_info()
    for info in all_infos:
        if info[0]==reg_nr:
            all_infos.remove(info)
    f=open("RentedVehicles.txt","w")
    datas=''
    for info in all_infos:
        data=info[0]+","+info[1]+","+info[2]+"\n"
        datas=datas+data
    f.write(datas)
    f.close()

def list_available_cars():
    all_cars_list=get_all_cars_info()
    rented_car_number_list=get_rented_reg_nr()
    for number in rented_car_number_list:
        for car in all_cars_list:
            if car[0]==number:
                all_cars_list.remove(car)
    print("The following cars are available:")
    for car in all_cars_list:
        properties=(car[3:])
        n=len(properties)
        print("* Reg. nr: {}, Model: {}, Price per day: {}".format(car[0],car[1],car[2]))
        string='Properties: '
        for number in range(n):
            string=string+properties[number]+", "
        print(string.strip(", "))

def rent_car():
    requested_reg_nr=input("Please write down the register number of the car you want to rent.\n")
    all_cars_reg_nr=get_all_reg_nr()
    rented_cars_reg_nr=get_rented_reg_nr()
    if requested_reg_nr in all_cars_reg_nr:
        if requested_reg_nr in rented_cars_reg_nr:
            print("Sorry, this car has already been rented.")
        else:
            reported_birthday=input("Please write down your birthday.\n")
            if reported_birthday[2]=="/" and reported_birthday[5]=="/":
                
                given_date=int(reported_birthday[:2].lstrip("0"))
                given_month=int(reported_birthday[3:5].lstrip("0"))
                if 1<=given_date<=31 and 1<=given_month<=12:
                    birth_time=datetime.strptime(reported_birthday,"%d/%m/%Y")
                    year_end=datetime.strptime("31/12/2022","%d/%m/%Y")
                    year_start=datetime.strptime("01/01/2022","%d/%m/%Y")
                    diff_1=math.floor(((year_end-birth_time).total_seconds())/60/60/24/365)
                    diff_2=math.floor(((year_start-birth_time).total_seconds())/60/60/24/365)
                    if 18<=diff_1<100 and 18<=diff_2<100:
                        existing_customers=get_customers_birthday()
                        if reported_birthday in existing_customers:
                            add_new_rented_car(requested_reg_nr,reported_birthday)
                            all_info=get_customers_info()
                            for info in all_info:
                                if reported_birthday==info[0]:
                                    print("Hello {}\nYou rented\
 the car {}".format(info[1],requested_reg_nr))

                        
                        else:
                            firstname=input("Please write down your first name:\n")
                            surname=input("Please write down your surname:\n")
                            email=input("Please leave your e-mail address:\n")
                            if "@" in email and "." in email:
                                add_new_customer(reported_birthday,firstname,surname,email)
                                add_new_rented_car(requested_reg_nr,reported_birthday)
                                print("Hello {}\nYou rented the car \
{}".format(firstname,requested_reg_nr))
                            else:
                                print("Sorry, email address is invalid.")
                    else: print("You cannot rent cars due to your age.")
                else:
                    print("Sorry, the date given is insensible.")
                
            else:
                print("Sorry, birthday format invalid.")
    else:
        print("Sorry, the register number you submitted is invalid.")

def return_car():
    return_reg_nr=input("Please write down the register number of the vehicle to be returned.\n")
    rented_cars_info=get_rented_cars_info()
    all_reg_nr=get_all_reg_nr()
    rented_reg_nr=get_rented_reg_nr()
    all_cars_info=get_all_cars_info()
    if return_reg_nr not in all_reg_nr:
        print("Sorry the register number you provided does not exist.")
    else:
        if return_reg_nr not in rented_reg_nr:
            print("Sorry, this car is not rented.")
        else:
            for rented_car in rented_cars_info:
                if rented_car[0]==return_reg_nr:
                    start_time=rented_car[-1]
                    birthday=rented_car[-2]
                    remove_rented_cars(rented_car[0])
            for car in all_cars_info:
                if car[0]==return_reg_nr:
                    daily_price=car[2]
            return_time=datetime.now()
            add_new_transaction(return_reg_nr,birthday,start_time,return_time,daily_price)

def count_money():
    f=open("transActions.txt","r")
    money=[]
    while True:
        row=f.readline().strip("\n").split(",")
        if len(row)<6:
            break
        else:
            money_0=int(row[-1][:-3])
            money.append(money_0)
    total=0
    for money_0 in money:
        total=total+money_0
    print("The total amount of money is {:.2f} euros".format(total))

        
            



                
                        




    
    
    
        
            
  




        
    
    
    

