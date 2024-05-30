units=int(input("Enter the units: "))
bill = 0
if units<=50:
    print("bills is ",units*0.50)
    bill=bill+units*0.50
elif units>50 and units<=100:
    print("bills is ",units*0.75)
    bill=bill+units*0.75
elif units>100 and units<=250:
    bill = bill + units * 1.25
else:
    bill = bill + units * 1.5

total_bill = bill + bill*(17/100)
print("total bill amount :", total_bill)

print("_"*100)

def calculate_bill(units):
    if units<=50:
        rate=0.50
    elif units<=100:
        rate=0.75
    elif units <=250:
        rate=1.25
    else:
        rate=1.50
    # calculating totalcost
    cost=units*rate
    #add surcharge
    surcharge=cost*0.17
    #Total bill including surcharge
    total_bill1=cost+surcharge

    return total_bill1

units_consumed=float(input("Enter the units consumed: "))
bill=calculate_bill(units_consumed)
print("Electricity bill including surcharge: Rs.",bill)