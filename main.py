import threading
import time
def MultiThreading(Array1,Array2,option):
    num=""
    if option!="merge":
        if option=="even":#sort even elements in Array1
            num="one"
            for i in Array1:
                if i % 2 == 0:
                    Array2.append(i)
        elif option=="odd":#sort odd elements in Array1
            num="two"
            for i in Array1:
                if i % 2 != 0:
                    Array2.append(i)
        Array2.sort()
        print(f'Thread {num} results: {Array2}')

    else:#merge even array and odd array
        merge=Array1+Array2
        print(f'Thread three results: {merge}')

even=[]
odd=[]
merge=[]

Array=[2,29,3,0,11,8,32,9,1,7,4,5,6,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31]

t1=threading.Thread(args=(Array,even,"even"),target=MultiThreading)
t2=threading.Thread(args=(Array,odd,"odd"),target=MultiThreading)
t3=threading.Thread(args=(even,odd,"merge"),target=MultiThreading)

t1.start()
t2.start()
t1.join()
t2.join()
t3.start()
t3.join()
print("Multithreading was done!")