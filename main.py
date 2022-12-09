import threading
import time
def EvenNumbers(a,even):
    for i  in a:
        if i % 2 == 0:
            even.append(i)
    even.sort()
    print(f'Thread one results: {even}')


def OddNumbers(a,odd):
    for i  in a:
        if i % 2 != 0:
            odd.append(i)
    odd.sort()
    print(f'Thread two results: {odd}')


def Merg(a,b,merg):
    time.sleep(0.001)
    merg+=a+b
    print(f'Thread three results: {merg}')


even=[]
odd=[]
merg=[]
a=[2,29,3,0,11,8,32,9,1,7,4,5,6,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31]
t1=threading.Thread(args=(a,even),target=EvenNumbers)
t2=threading.Thread(args=(a,odd),target=OddNumbers)
t3=threading.Thread(args=(even,odd,merg),target=Merg)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Multithreading was done!")