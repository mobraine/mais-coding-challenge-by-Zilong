import csv
import numpy as np
import matplotlib.pyplot as plt


MortgageUsers = []
OwnUsers = []
RentUsers = []

MortgageTotal = 0
OwnTotal = 0
RentTotal = 0

MLoanTotal = 0
OLoanTotal = 0
RLoanTotal = 0

with open('home_ownership_data.csv') as ownershipD:
    ownershipDReader = csv.reader(ownershipD,delimiter = ',')
    lineNum = 0
    
    for row in ownershipDReader:
        if lineNum == 0:
            print ('member_id'+' '+ 'home_ownership')
            lineNum += 1
        else :
            #print (row[0]+' '+ row[1])

            if row[1] == 'MORTGAGE':
                MortgageUsers = MortgageUsers + [row[0]]
                MortgageTotal += 1
            elif row[1] == 'OWN':
                OwnUsers = OwnUsers + [row[0]]
                OwnTotal += 1
            else :
                RentUsers = RentUsers + [row[0]]
                RentTotal += 1
            
            lineNum += 1
            
    print (str(lineNum)+" lines in total.")
    print (RentTotal)
    print (MortgageTotal)
    print (OwnTotal)

with open('loan_data.csv') as loanD:
    loanDReader = csv.reader(loanD,delimiter = ',')
    lineNum = 0

    for row in loanDReader:
        if lineNum == 0:
            lineNum += 1
        else:
            if row[0] in MortgageUsers:
                MLoanTotal += float(row[3])
            elif row[0] in OwnUsers:
                OLoanTotal += float(row[3])
            else:
                RLoanTotal += float(row[3])

            lineNum += 1
            
    print (OLoanTotal)
    print (MLoanTotal)
    print (RLoanTotal)

M_ave = MLoanTotal/MortgageTotal
O_ave = OLoanTotal/OwnTotal
R_ave = RLoanTotal/RentTotal

print ('MORTGAGE   ' + str(M_ave))
print ('OWN   ' + str(O_ave))
print ('RENT   ' + str(R_ave))

label = ['MORTGAGE','OWN','RENT']
loan_amnt_ave = [M_ave,O_ave,R_ave]

index = np.arange(len(label))
plt.bar(index, loan_amnt_ave)
plt.xlabel('Home ownership', fontsize=5)
plt.ylabel('Average loan amount', fontsize=5)
plt.xticks(index, label, fontsize=5)
plt.title('Average loan amount per home ownership',fontsize = 7)
plt.show()


