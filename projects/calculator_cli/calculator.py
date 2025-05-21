def operation(x,y,op):
    if op =="+":
        return x+y
    elif op=="-":
        return x-y
    elif op=="*":
        return x*y
    elif op=="/":
        if y==0:
            print("ERROR :Division by 0 is not possible!")
            return None
        return x/y
    else:
        print("enter +,-,*,/")
      
def history():
    for x,y,op,a in zip(list_input1,list_input2,list_input3,list_input4):
        print(f"{x} {op} {y} = {a}")
        
              
def calculator():
    print("Welcome to the CLI Calculator!!!")           
    
 
calculator()
list_input1=[]
list_input2=[]
list_input3=[]
list_input4=[]
while True:
    try:
        x=float(input("enter first number: "))
        y=float(input("input second number: "))
        op=input("enter operation: ").strip()
        
        result=operation(x,y,op)
        if result is None:
            continue
        
        print(f"result: {result}")
        
        list_input1.append(x)
        list_input2.append(y)
        list_input3.append(op)
        list_input4.append(result)
        
        h=input("Do you wish to view your history(y/n)")
        if h=="y":
            history()   
        cont=input("Do you want to continue(y/n):").strip().lower()
        if cont=="n":
            print("You have exited the calculator.Goodbye!")
            break
        
    except ValueError:
        print(" Please enter a valid number ")
    except KeyboardInterrupt:
        print("keyboard exiting:")
        break