import math
a=float(input("nhap canh thu nhat"))
b=float(input("nhap canh thu hai"))
c=float(input("nhap canh thu ba"))
p=(a+b+c)/2
if a+b>c and b+c>a and c+a>b:
    if a==b and a==c:
        print("la tam giac vuong")
    elif a==b or b==c or c==a:
        if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            print("tam giac vuong can")
        else:
            print("tam giac can")
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print("tam giac vuong")
    else:
        print("tam giac thuong")
            
    print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    
else:
    print("khong phai 3 canh tam giac")