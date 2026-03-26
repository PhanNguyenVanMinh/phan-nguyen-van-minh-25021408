a=int(input("So chu ho"))
ten=[]
dientruoc=[]
diennay=[]
ten=[]
for i in range(a):
    ten.append(input("Ten chu ho thu "+str(i+1)+":"))
    dientruoc.append(input("so dien thang truoc ho thu "+str(i+1)+":"))
    diennay.append(input("so dien thang nay ho thu "+str(i+1)+":"))

    tong=[]
    for i in diennay:
         for j in range(a):
            if int(i)>=401:
                tong.append((50*1984+50*2050+100*2380+100*2998+100*3350+(int(i)-400)*3460)*1.08)
                break
            if 301 <= int(i) <= 400:
                tong.append((50*1984+50*2050+100*2380+100*2998+(int(i)-300)*3350)*1.08)
                break
            if 201 <= int(i) <= 300:
                tong.append((50*1984+50*2050+100*2380+(int(i)-200)*2998)*1.08)
                break
            if 101 <= int(i) <= 200:
                tong.append((50*1984+50*2050+(int(i)-100)*2380)*1.08)
                break
            if 51 <= int(i) <= 100:
                tong.append((50*1984+(int(i)-50)*2050)*1.08)
                break
            else:
                tong.append((int(i)*1984)*1.08)
                break
for i in range(a):   
    print("tien dien thang nay ho ",i+1+":",tong[i])