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
            count_money
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

list_available_cars()

    

    
    
    
        
            
  




        
    
    
    

