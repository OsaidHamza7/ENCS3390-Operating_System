import random
from collections import deque
from time import sleep
import keyboard
from threading import Thread
import matplotlib.pyplot as Mat

#Turnaround time for process P[i] = Completion time of P[i] - Arrival time of P[i]
#Waiting time for process P[i] = Turnaround time of P[i] - sum of all CPU burst time of P[i]


#Start Project
#//////////////////////////////////////////////////////////////////////////////////////////


def GanttChart(Catt):
    s="|_______"*(len(Catt)-1)
    s+="|"
    a="_"*len(s)
    print("\033[1;93m")
    print(a)
    for i in range(1,len(Catt)):
        if Catt[i][0]=="idle":
            print("|%-7s" % (Catt[i][0]), end="")
        else:
            print("|P%-6d"%(Catt[i][0]), end="")
    print("|", end="")
    print()
    print(s)
    for i in range(len(Catt)):
        print("%-8d"%(Catt[i][1]), end="")
    print("\033[0m")
def CheckFinish(processes):
    count=0
    for p in processes:
        a=p["CPU_IO"]
        if a.count(0)==len(a):
            count+=1
    if count==len(processes):
        return True
    return False


def GetCPU():
    return CPU
def DisplyProcessesQueue(Queue):
        s = "|_______" * (len(Queue))
        s += "|"
        a = "_" * len(s)
        print("\033[1;93m")
        print(a)
        for i in range(0, len(Queue)):
            print("|P%-6d" % (Queue[i]["PID"]), end="")
        print("|", end="")
        print()
        print(s)

def GetQueue1():
    return Queue1
def GetQueue2():
    return Queue2
def GetQueue3():
    return Queue3
def GetQueue4():
    return Queue4
def GetProcessesIO():
    return IO
def DisplayProcessesIO(IO):
    print("The Processes In IO In This Time:")
    s = "|_______" * (len(IO))
    s += "|"
    a = "_" * len(s)
    print("\033[1;93m")
    print(a)
    for i in range(0, len(IO)):
        print("|P%-6d" % (IO[i][0]), end="")
    print("|", end="")
    print()
    print(s)
def GetCurrentProcess():
    return Current_Process
def GetFinishProgram():
    return FinishProgram

def Running():
    while True:
        FinishProgram=GetFinishProgram()
        if FinishProgram==1:
            break
        keyboard.wait('esc')
        Q1=GetQueue1()
        Q2=GetQueue2()
        Q3=GetQueue3()
        Q4=GetQueue4()
        CPU=GetCPU()
        IO=GetProcessesIO()
        if Q1:
            print("\033[1;94mThe Processes In Queue1 In This Time:\033[0m")
            DisplyProcessesQueue(Q1)
        else:
            print("\033[1;91mThere Is No Processes In Queue1 Right Now!\033[0m")

        if Q2:
            print("\033[1;94mThe Processes In Queue2 In This Time:\033[0m")
            DisplyProcessesQueue(Q2)
        else:
            print("\033[1;91mThere Is No Processes In Queue2 Right Now!\033[0m")


        if Q3:
            print("\033[1;94mThe Processes In Queue3 In This Time:\033[0m")
            DisplyProcessesQueue(Q3)
        else:
            print("\033[1;91mThere Is No Processes In Queue3 Right Now!\033[0m")



        if Q4:
            print("\033[1;94mThe Processes In Queue4 In This Time:\033[0m")
            DisplyProcessesQueue(Q4)
        else:
            print("\033[1;91mThere Is No Processes In Queue4 Right Now!\033[0m")

        PROCESS=GetCurrentProcess()
        if PROCESS:
            print("\033[1;91mThe Currently Running Process is: "+"\033[1;92mP"+str(PROCESS["PID"])+"\033[0m")
        else:
            print("\033[1;91mThere Is No Currently Running Process!\033[0m")
        if IO :
            DisplayProcessesIO(IO)
        else:
            print("\033[1;91mThere Is No Processes In I/O Right Now!\033[0m")


        print("\033[1;94mThe Gant Chart Right Now\033[0m")
        while len(CPU) > 14:
            GanttChart(CPU[0:15])
            CPU = CPU[14:]
        if len(CPU) > 1:
            GanttChart(CPU)

#//////////////////////////////////////////////////////////////////////////////////////////



# #Workload Generator
while True:
    try :
        Nprocesses=int(input("\033[2;93mPlease enter a number of processes:\033[0m"))
        break
    except :
        print("\033[2;91mEnter a valid value!!\033[0m")

while True:
    try :
        ArrivalTime=int(input("\033[2;93mPlease enter a Max arrival time:\033[0m"))
        break
    except :
        print("\033[2;91mEnter a valid value!!\033[0m")

while True:
    try :
        NumCPUBurst=int(input("\033[2;93mPlease enter a max number of CPU burst :\033[0m"))
        break
    except :
        print("\033[2;91mEnter a valid value!!\033[0m")

while True:
    try :
        MinCPU = int(input("\033[2;93mPlease enter a minimum value of CPU burst :\033[0m"))
        break
    except :
        print("\033[2;91mEnter a valid value!!\033[0m")

while True:
    try :
        MaxCPU=int(input("\033[2;93mPlease enter a maximum value of CPU burst :\033[0m"))
        while MaxCPU < MinCPU:
            print("\033[2;91mError!!Invalid value because it is less than the minimum value of CPU burst\033[0m")
            MaxCPU = int(input("\033[2;93mPlease enter a maximum value of CPU burst :\033[0m"))

        break
    except :
        print("\033[2;91mEnter a valid value!!\033[0m")

while True:
    try :
        MinIO = int(input("\033[2;93mPlease enter a minimum value of I/O burst :\033[0m"))
        break
    except :
        print("\033[2;91mEnter a valid value!!\033[0m")

while True :
    try:
        MaxIO=int(input("\033[2;93mPlease enter a maximum value of I/O burst :\033[0m"))
        while MaxIO<MinIO:
            print("\033[2;91mError!!Invalid value because it is less than the minimum value of I/O burst\033[0m")
            MaxIO = int(input("\033[2;93mPlease enter a maximum value of I/O burst :\033[0m"))
        break
    except:
        print("\033[2;91mEnter a valid value!!\033[0m")



print("\033[0m",end="")
Workload=[]
Workload.append("PID");Workload.append("ِTime");Workload.append("CPU")
for _ in range(NumCPUBurst-1):
    Workload.append("I/O");Workload.append("CPU")
array=[]
#make Workload Genrator using random
for i in range(Nprocesses):
    P=[]
    P.append(i)
    P.append(random.randint(0,ArrivalTime))
    NBurst=str(random.randint(1,NumCPUBurst))
    for j in range(int(NBurst)*2-1):
        if j%2==0:
            P.append(random.randint(MinCPU,MaxCPU))
        else:
            P.append(random.randint(MinIO,MaxIO))
    array.append(P)

print("\033[1;96m",end="")
for i, w in enumerate(Workload):
    print("%-7s"%w,end="")

print("\n----------------------------------------------------------------------------")
for num in array:
    for j in num:
        print("%-7s"%j,end="")
    print("\n")

FileName=input("\033[2;93mPlease enter a file name to save a generated workload (.txt):\033[0m")
while not FileName.endswith(".txt"):
    FileName=input("\033[2;91mError!,Please enter a valid filename(.txt):\033[0m")

file=open("FileName`", "w+")#to write and read into the file
for num in array:
    for i,j in enumerate(num):
        if i==0 or i==1 or i==len(num)-1:
            file.write(str(j)+";")
        else:
            file.write(str(j)+",")
    file.write("\n")
#///////////////////////////////////////////////////////////////////////////////////////////////
#Simulator

file.seek(0)# to move the file pointer to the beginning of the file so that the contents can be read.
processes=[]
q1=int(input("\033[2;93mPlease enter a value of q1 :\033[0m"))
q2=int(input("\033[2;93mPlease enter a value of q2 :\033[0m"))
alpha=float(input("\033[2;93mPlease enter a value of \u03B1(ALPHA) :\033[0m"))
processes=[]
File=open("File.txt","r")
lines=File.readlines()
for line in lines:
    p=list(map(str,line.strip().split(";")))
    a=int(p[0])
    b=int(p[1])
    c=list(map(int,p[2].split(",")))
    SumCPU=0
    for i in range(len(c)):
        if i%2==0:
            SumCPU+=c[i]

    # Sum_CPU:sum of all CPU burst time of process
    processes.append(dict(PID=a,AT=b,CPU_IO=c,Q1=q1*10,Q2=q2*10,gusses=0,Ignore=0,Queue=1,WT=0,First_AT=b,Sum_CPU=SumCPU))#FAT:first arrival time
print(processes)
#///////////////////////////////////////////////////////////////////////////////////////////////
currentTime=0
Queue1=deque()
Queue2=deque()
Queue3=deque()
Queue4=deque()
CPU=[[0,0]]
Current_Process={}
count=0
IO=[]
count2=0
WasteTime=0
Finish_Time=0
idle=0
Wiating_Time=[]
FinishProgram=0


t1=Thread(target=Running)#start a thread to wait the user to puase the Simulator
t1.start()




# start multilevel

while True:
    print(f"Time:{currentTime}")
    # check if theres no any process in all queues,and theres no process has a CPU burst
    if not Queue1 and not Queue2 and not Queue4 and CheckFinish(processes) == True:
        print("\033[1;92mThe program is finished!\033[0m")
        Finish_Time = currentTime
        break
    # //////////////////////////////////////////////////////////////////////////////
    # Check if any process has arrived
    for i, p in enumerate(processes):
        if currentTime == p["AT"]:  # the process has arrived
            if p in IO:
                IO.remove(p)
            if idle > 0:
                CPU.append(["idle", currentTime])
                idle = 0
            if p["Queue"] == 1:
                if currentTime == 0:
                    CPU.clear()
                    CPU.append([p["PID"], p["AT"]])

                elif not Queue1:
                    if Current_Process:
                        CPU.append([Current_Process["PID"], currentTime])
                Queue1.append(p)
                print(f"\033[1;96mThe Process " + str(p["PID"]) + " enter a Queue1 at the second " + str(
                    p["AT"]) + "\033[0m")
            elif p["Queue"] == 2:
                Queue2.append(p)

                print(f"\033[1;96mThe Process " + str(p["PID"]) + " enter a Queue2 at the second " + str(
                    p["AT"]) + "\033[0m")
            elif p["Queue"] == 3:
                gusses = alpha * p["CPU_IO"][0] + (1 - alpha) * p["gusses"]
                p["gusses"] = gusses
                Queue3.append(p)
                print(f"\033[1;96mThe Process " + str(p["PID"]) + " enter a Queue3 at the second " + str(
                    p["AT"]) + "\033[0m")
            elif p["Queue"] == 4:
                Queue4.append(p)
                print(f"\033[1;96mThe Process " + str(p["PID"]) + " enter a Queue4 at the second " + str(
                    p["AT"]) + "\033[0m")
    # ////////////////////////////////////////////////////////////////////////////////////////////////

    if Queue1:  # queue1 not empty
        Current_Process = Queue1[0]
        if Current_Process["CPU_IO"][0] != 0 and Current_Process["Q1"] != 0 and count < q1:
            print(f"\033[1;92mThe Process " + str(Current_Process["PID"]) + " is running..." + "\033[0m")
            Current_Process["CPU_IO"][0] -= 1
            Current_Process["Q1"] -= 1
            count += 1
        if Current_Process["CPU_IO"][0] == 0:
            count = 0
            if Current_Process["CPU_IO"].count(0) == len(Current_Process["CPU_IO"]):
                TT = currentTime +1- Current_Process["First_AT"]
                WT=TT - Current_Process["Sum_CPU"]
                Wiating_Time.append(WT)
                print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " finish All CPU Bursts" + "\033[0m")
                Queue1.popleft()
                CPU.append([Current_Process["PID"], currentTime + 1])
                Current_Process = []

            else:
                print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " finish it's CPU Burst" + "\033[0m")
                for j, co in enumerate(Current_Process["CPU_IO"]):
                    if co != 0:
                        if j % 2 != 0:
                            CPU.append([Current_Process["PID"], currentTime + 1])
                            Current_Process["CPU_IO"][0] = Current_Process["CPU_IO"][j + 1]
                            Current_Process["CPU_IO"][j + 1] = 0
                            Current_Process["AT"] = Current_Process["CPU_IO"][j] + currentTime+1
                            Current_Process["CPU_IO"][j] = 0
                            Current_Process["Queue"] = 1
                            Current_Process["Q1"] = 10 * q1
                            print(
                                f"\033[1;95mThe Process " + str(Current_Process["PID"]) + " enter an I/O " + "\033[0m")
                            Queue1.popleft()
                            IO.append(Current_Process)
                            Current_Process = {}
                            count = 0
                            break

        elif Current_Process["Q1"] == 0:
            print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " enter a Queue2 at the second " + str(
                currentTime) + "\033[0m")
            CPU.append([Current_Process["PID"], currentTime + 1])
            Queue2.append(Current_Process)
            Queue1.popleft()
            Current_Process = {}
            count = 0

        elif count >= q1:
            CPU.append([Current_Process["PID"], currentTime + 1])
            Queue1.append(Current_Process)
            Queue1.popleft()
            Current_Process = {}
            count = 0

    # /////////////////////////////////////////////////////////////////////////////////////////////////////

    elif Queue2:
        Current_Process = Queue2[0]
        if Current_Process["CPU_IO"][0] != 0 and Current_Process["Q2"] != 0 and count2 < q2:
            print(f"\033[1;92mThe Process " + str(Current_Process["PID"]) + " is running..." + "\033[0m")
            Current_Process["CPU_IO"][0] -= 1
            Current_Process["Q2"] -= 1
            count2 += 1
        if Current_Process["CPU_IO"][0] == 0:
            count2 = 0
            if Current_Process["CPU_IO"].count(0) == len(Current_Process["CPU_IO"]):
                TT = currentTime+1 - Current_Process["First_AT"]
                Wiating_Time.append(TT - Current_Process["Sum_CPU"])
                print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " finish All CPU Bursts" + "\033[0m")
                Queue2.popleft()
                CPU.append([Current_Process["PID"], currentTime + 1])
                Current_Process = {}

            else:
                print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " finish it's CPU Burst" + "\033[0m")
                for j, co in enumerate(Current_Process["CPU_IO"]):
                    if co != 0:
                        if j % 2 != 0:
                            CPU.append([Current_Process["PID"], currentTime + 1])
                            Current_Process["CPU_IO"][0] = Current_Process["CPU_IO"][j + 1]
                            Current_Process["CPU_IO"][j + 1] = 0
                            Current_Process["AT"] = Current_Process["CPU_IO"][j] + currentTime+1
                            Current_Process["CPU_IO"][j] = 0
                            Current_Process["Queue"] = 2
                            Current_Process["Q2"] = 10 * q2
                            print(
                                f"\033[1;95mThe Process " + str(Current_Process["PID"]) + " enter an I/O " + "\033[0m")
                            Queue2.popleft()
                            IO.append(Current_Process)
                            Current_Process = {}

                            break

        elif Current_Process["Q2"] == 0:
            print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " enter a Queue3 at the second " + str(
                currentTime) + "\033[0m")
            CPU.append([Current_Process["PID"], currentTime + 1])
            gusses = alpha * Current_Process["CPU_IO"][0]+(1-alpha)*50
            Current_Process["gusses"] = gusses
            Queue3.append(Current_Process)
            Queue2.popleft()
            Current_Process = []
            count2 = 0

        elif count2 >= q2:
            CPU.append([Current_Process["PID"], currentTime + 1])
            Queue2.append(Current_Process)
            Queue2.popleft()
            Current_Process = []
            count2 = 0
#////////////////////////////////////////////////////////////////////////////////////////////////////


    elif Queue3:

        k = 0

        if not Current_Process:
            Current_Process = Queue3[0]

            HighestProcess = Current_Process

            k = 1

        HighestProcess = Current_Process

        for n in Queue3:

            if n["gusses"] < Current_Process["gusses"]:

                if k == 0:
                    CPU.append([Current_Process["PID"], currentTime])

                    k = 1

                HighestProcess = n

                Current_Process["Ignore"] += 1

                if Current_Process["Ignore"] == 3:
                    print(f"\033[1;96mThe Process " + str(

                        Current_Process["PID"]) + " enter a Queue4 at the second " + str(

                        currentTime) + "\033[0m")

                    # CPU.append([Current_Process["PID"], currentTime])

                    Queue4.append(Current_Process)

                    Queue3.pop()

                    Current_Process = {}

        Current_Process = HighestProcess

        if Current_Process["CPU_IO"][0] != 0:
            print(f"\033[1;92mThe Process " + str(Current_Process["PID"]) + " is running..." + "\033[0m")

            Current_Process["CPU_IO"][0] -= 1

        if Current_Process["CPU_IO"][0] == 0:

            if Current_Process["CPU_IO"].count(0) == len(Current_Process["CPU_IO"]):

                TT = currentTime + 1 - Current_Process["First_AT"]

                Wiating_Time.append(TT - Current_Process["Sum_CPU"])

                print(f"\033[1;96mThe Process " + str(

                    Current_Process["PID"]) + " finish All CPU Bursts" + "\033[0m")

                CPU.append([Current_Process["PID"], currentTime + 1])

                Queue3.remove(Current_Process)

                Current_Process = {}



            else:

                print(f"\033[1;96mThe Process " + str(

                    Current_Process["PID"]) + " finish it's CPU Burst" + "\033[0m")

                for j, co in enumerate(Current_Process["CPU_IO"]):

                    if co != 0:

                        if j % 2 != 0:
                            CPU.append([Current_Process["PID"], currentTime + 1])

                            Current_Process["CPU_IO"][0] = Current_Process["CPU_IO"][j + 1]

                            Current_Process["CPU_IO"][j + 1] = 0

                            Current_Process["AT"] = Current_Process["CPU_IO"][j] + currentTime + 1

                            Current_Process["CPU_IO"][j] = 0

                            Current_Process["Queue"] = 3

                            print(f"\033[1;95mThe Process " + str(

                                Current_Process["PID"]) + " enter an I/O " + "\033[0m")

                            Queue3.remove(Current_Process)

                            Current_Process = {}




# /////////////////////////////////////////////////////////////////////////////////////////////////////

    elif Queue4:
        Current_Process = Queue4[0]
        if Current_Process["CPU_IO"][0] != 0:
            print(f"\033[1;92mThe Process " + str(Current_Process["PID"]) + " is running..." + "\033[0m")
            Current_Process["CPU_IO"][0] -= 1
        if Current_Process["CPU_IO"][0] == 0:
            if Current_Process["CPU_IO"].count(0) == len(Current_Process["CPU_IO"]):
                TT = currentTime+1 - Current_Process["First_AT"]
                Wiating_Time.append(TT - Current_Process["Sum_CPU"])
                print(f"\033[1;96mThe Process " + str(Current_Process["PID"]) + " finish All CPU Bursts" + "\033[0m")
                Queue4.popleft()
                CPU.append([Current_Process["PID"], currentTime + 1])
                Current_Process = {}

            else:
                print(f"\033[1;96mThe Process " + str(
                    Current_Process["PID"]) + " finish it's CPU Burst" + "\033[0m")
                for j, co in enumerate(Current_Process["CPU_IO"]):
                    if co != 0:
                        if j % 2 != 0:
                            CPU.append([Current_Process["PID"], currentTime + 1])
                            Current_Process["CPU_IO"][0] = Current_Process["CPU_IO"][j + 1]
                            Current_Process["CPU_IO"][j + 1] = 0
                            Current_Process["AT"] = Current_Process["CPU_IO"][j] + currentTime + 1
                            Current_Process["CPU_IO"][j] = 0
                            Current_Process["Queue"] = 4
                            print(f"\033[1;95mThe Process " + str(Current_Process["PID"]) + " enter an I/O " + "\033[0m")
                            Queue4.popleft()
                            IO.append(Current_Process)
                            Current_Process={}
                            break


    else:#there is no any process in cpu(they in IO)
        idle+=1
        WasteTime+=1


    currentTime+=1
    sleep(0.1)

Finish_Time=currentTime

# the end of the simulation
#////////////////////////////////////////////////////////////////////////////////////////////

#GanttChart

while len(CPU)>14:
    GanttChart(CPU[0:15])
    CPU=CPU[14:]
if len(CPU)>0:
    GanttChart(CPU)

#CPU utilization

CPU_uti=int(((Finish_Time - WasteTime)*100)/Finish_Time)
print(f"\033[1;91mCPU utilization:\033[1;92m{CPU_uti}%\033[0m")
IDLE=100-CPU_uti
print(f"\033[1;91mIdle:\033[1;92m{IDLE}%\033[0m")
s=[CPU_uti,IDLE]
l=["CPU utilization","IDLE"]
exp=[0,0]
Mat.pie(s,labels=l,explode=exp,autopct="%1.1f%%")
Mat.title("CPU Utilization")
Mat.legend()
Mat.show()

#The average waiting time for all the processes.
if Wiating_Time:
    print(f"\033[1;91mAverage Waiting Time :\033[1;92m{sum(Wiating_Time)/len(Wiating_Time)} msec\033[0m")
else:
    print(f"\033[1;91mAverage Waiting Time :\033[1;92m0 msec\033[0m")

FinishProgram=1
print(f"\033[1;92mEnter ESC In Your Keyboard To Leave The program \U0001f600\033[0m")

t1.join()

#The end