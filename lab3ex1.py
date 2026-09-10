name=input("Enter the name:")
age=int(input("Enter the age:"))
income=int(input("Enter the income:"))
caste=input("Enter the caste(OPEN,SC,ST,OBC:")
if age<25 and income<300000 and caste in["OPEN"]:
    print("You Are Eligible:")
else:
    print("You Are Not Eligible:")
 