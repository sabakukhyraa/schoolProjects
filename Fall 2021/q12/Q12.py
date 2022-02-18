days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days)
holiday = input("Choose a holiday from weekdays: ")
days.remove(holiday)
turns = ["0-8", "8-16", ["16-20", "20-24"]]

#600 workers consume fresh water for their own needs. And consume it for the product of processes.
#Water producter has different prices for water for different time slices.
#200 Workers are working in every shift and manufacturing the end product with different amounts.

# 1m^3 water = 1000 Liters of water
# 1000 Liters of water = 12.05TL or 20.0TL
# 1 Liter of water = 0,01205TL or 0,02TL

# We assumed that 1 month = 28 days.

amount_of_water_consumed = 0
amount_be_paid = 0

def accountant(amount_daily_piece, amount_employee, price_water_per_liter):

    global amount_be_paid
    global amount_of_water_consumed
    
    #20+10+30 = 60
    #The a variable is amount of water consumed that day.
    a = ((amount_daily_piece*(60)) + (amount_employee*10))
    amount_of_water_consumed += a
    amount_be_paid += a*price_water_per_liter


def Bill(x,y):


    if x != "Saturday" and x != "Sunday":
        #Meaning, in weekdays;
        if y == "0-8":
           #Meaning, in 00-08 shift, price is 20TL/m^3;
            accountant(250, 200, 0.02)

        elif y == "8-16":
            #Meaning, in 08-16 shift, price is 12.05TL/m^3;
            accountant(450, 200, 0.01205)  

        else:
            #Meaning, in 16-24 shift. Price is 12.05TL/m^3 until the 20:00. After 20:00, it is 20TL/m^3.
            #This is a 'nested for loop' from the outside of the function.
            for s in y:
                #Amount of pieces that produced by workers at 16-24 is 300. We assumed that it is 150 until 20:00 than another 150.
                if s == "16-20":
                    accountant(150, 100, 0.01205)

                else:
                    accountant(150, 100, 0.02)  

    else:
        #Meaning, in weekends;
        if y == "0-8":
            #It is shift number one at weekend, price is %15 more. 0.020x(115รท100).
            accountant(250, 200, 0.023)

        elif y == "8-16": 
            #It is shift number two(08-16) at weekend, price is %15 more. 0.01205x(115รท100).
            accountant(450, 200, 0.0138575)

        else:

            for s in y:
                if s == "16-20":
                    accountant(150, 100, 0.0138575)   

                else:
                    accountant(150, 100, 0.023)



week_no = 1
while  week_no < 5:  
                 
    for i in days:        
        for j in turns:
            Bill(i,j)

    week_no += 1

print(f"Amount of water that consumed is {amount_of_water_consumed}L.")
print(f"Amount of money that should be paid is {amount_be_paid}TL.")