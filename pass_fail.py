total_classes = 40
print("insert your grade")
grade = float(input())
print("how many classes have you attended?")
attended_classes = int(input())
attendance = attended_classes / total_classes * 100
if attendance > 80 and grade > 70 :
    print ("you passed this class") 
else  :
    print ("you did not pass this class")