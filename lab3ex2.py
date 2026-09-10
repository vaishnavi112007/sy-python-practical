score=float(input("Enter graduation score(%):"))
backlogs=int(input("Enter academic Backlogs:"))

if score>=70 and backlogs==0:
    print("Candidate is Eligible for Placement")

else:
    print("candidate is Not Eligible for Placement")