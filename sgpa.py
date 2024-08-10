def grade(m):
    return 10 if m>=90 else 9 if m<90 and m>=80 else 8 if m<80 and m>=70 else 7 if m<70 and m>=60 else 6 if  m<60 and m>=50 else 5 if m<50 and m>=45 else 4 if  m<45 and m>=40 else 0
def sgpaa():
    marks = []
    grades = []
    cg = []
    credit = []
    sub =[]
    print("\n\n")
    n = int(input("enter how many subjects : "))
    for i in range(n):
        a = input("Enter the subject name : ")
        sub = sub + [a]
        credit = credit + [int(input(f"Enter the credit for {a} : "))]
        m = int(input(f"\t Enter the marks in {sub[i]}  :  "))
        marks = marks + [m]
        g = grade(m)
        grades = grades + [g]
        cg = cg + [g*credit[i]]
    if 0 in grades:
        print("\n Ohh!! sorry to say this but you're failed !!!")
        exit
    else:
        print("\n\t Congratulations buddy !! You have successfully passed the exam ")
        print("\n\t Your total marks is : ",sum(marks))
        print("\n\t Your total percentage is : ", str(sum(marks)/n)+"%")
        ans = (sum(cg)/sum(credit))
        print("\n\t Your SGPA is  : ", ans)
sgpaa()