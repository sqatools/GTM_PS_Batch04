marks = 65

if marks > 100:
    print("Marks should not be greater than 100")
elif 40 < marks <= 50 :
    print ("C grade")
elif 50 < marks <= 60:
    print("B grade")
elif 60 < marks <= 70:
    print ("A grade")
elif 70 < marks <= 80:
    print ("A+ grade")
elif 80 < marks <=90:
    print("A++ grade")
elif 90 < marks < 100:
    print("Excellent grade")
else :
    print("Failed")