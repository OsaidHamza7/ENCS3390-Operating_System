import threading


def EvenSortingArray(Array1,EvenArray,check):
    check["start"] += "T"
    for i in Array1:
        if i % 2 == 0:
            EvenArray.append(i)
    EvenArray.sort()
    print(f'Thread one results: {EvenArray}')

def OddSortingArray(Array1,OddArray,check):
    check["start"] += "T"
    for i in Array1:
        if i % 2 != 0:
            OddArray.append(i)
    OddArray.sort()
    print(f'Thread two results: {OddArray}')

def Merge(EvenArray,OddArray,MergeArray,check):

    while (check["start"] != "TT"):
        continue
    MergeArray = EvenArray + OddArray
    print(f'Thread three results: {MergeArray}')

even=[]
odd=[]
merge=[]
check={"start":""}
Array=[2,29,3,0,11,8,32,9,1,7,4,5,6,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31]

t1=threading.Thread(args=(Array,even,check),target=EvenSortingArray)
t2=threading.Thread(args=(Array,odd,check),target=OddSortingArray)
t3=threading.Thread(args=(even,odd,merge,check),target=Merge)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Multithreading was done!")
