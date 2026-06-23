from time import*
import random as r
def mistake(paratest, usertest):
    Error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
               Error=Error+1
        except:
            Error=Error+1
            return Error
def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_r=round(time_delay,2)
    speed=len(userinput)/time_r
    return round(speed)
while True:
    ck=input("Do you want to start the typing speed test? (yes/no): ")
    if ck=='yes': 
        test=["The quick brown fox jumps over the lazy dog",
          "A journey of a thousand miles begins with a single step",
          "To be or not to be that is the question",
          "All that glitters is not gold",
          "I think therefore I am"]
        test1=r.choice(test)
        print("**********Typing Speed Test**********")
        print(test1)
        # print()
        # print()
    
        time_1=time()
        test_input=input("\n\nEnter the above line:\n")
        time_2=time()
        print("\n\nspeed:", speed_time(time_1,time_2,test_input),"characters per second")
        print("Error:",mistake(test1,test_input))
    elif ck=='no':
        print("Thank you for using the typing speed test.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        