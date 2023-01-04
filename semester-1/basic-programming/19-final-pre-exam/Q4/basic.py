ans=["red","blue","red","green"]
list1=[]
check=0
strcheck=""
time=0
for i in range(0,10,1):
    x=input("依序輸入四個顏色(中間以空白隔開)")
    list1=x.split(" ")
    for i in range (0,4,1):
        if list1[i] == ans[i]:
            check+=1
            strcheck+="1"
        elif ans.count(list1[i])>0:
            strcheck+="2"
        elif ans.count(list1[i])==0:
            strcheck+="3"
    if check==4:
        print("正確答案")
        break
    else:
        print(strcheck)
        strcheck=""
        check=0
        time+=1
        if time == 10 :
            print("挑戰失敗")
