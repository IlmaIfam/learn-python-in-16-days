import math
    
while True:
        print("\n Basic Calculator")
        print("Operations:")
        print("1 . Arithmetic Operations (+,- , * , /)")
        print("2 . Exponentical Function (e^x)")
        print("3 . Logarithmic Functions (log, log10)")
        print("4 . Trigonometric Functions (sin, cos, tan)")
        print("5 . Hyperbolic Functions(sinh, cosh, tanh)")
        print(" Type 'exit' to quit the calculator.")
        
        operation = input("choose an operation (1- 5) or type 'exit' :")
        
        if operation.lower()=='exit':
            print("Exiting the calculator.Goodbye!")
            break
        if operation in ['1','2','3','4','5']:
            if operation == '1':
                # Arithmetic Operations
                try:
                    num1 = float(input("Enter the first number :"))
                    num2 = float(input("Enter the second number :"))
                    operation =(input("choose an operation (+ , - , *  , / ) :"))
                    
                    if operation =='+':
                        result = (num1 + num2)
                        print(num1 + num2)
                    elif  operation=='-':
                        result = (num1 - num2) 
                        print(num1- num2)
                    elif operation =='*':
                        result = (num1 * num2)
                        print(num1 *num2) 
                        
                    elif operation =='/':
                        if num2 == 0:
                            continue
                        result = num1 / num2
                        print(num1 / num2)
                    else:    
                        print("Error: Invalid operation.")
                        continue
                    print(f"result: {num1} {operation} {num2} = {result}")
                except ValueError:
                    print("Error: Invalid input. please enter numerical values.")             
            elif operation in ['2','3','4','5']:
                try:
                     value = float(input("Enter the value :"))
                     if operation == '2':
                        print(f"e^{value} = {math.exp(value)}")
                     elif operation == '3':
                        print(f"log({value}) = {math.log(value)}") 
                        print(f"log10({value}) = {math.log10(value)}")
                     elif operation == '4':
                        print(f"sin({value}) = {math.sin(value)}")
                        print(f"cos({value}) = {math.cos(value)}")
                        print(f"tan({value}) = {math.tan(value)}")    
                     elif operation == '5':
                        print(f"sinh({value}) = {math.sinh(value)}") 
                        print(f"cosh({value}) = {math.cosh(value)}") 
                        print(f"tanh({value}) = {math.tanh(value)} ")
                     else:   
                        print("Error: Invalid operations. please enter a numerical value.")
                        
                    #option to continue or exit
                     continue_cal = input("Do you want to  perform another calculation? (yes/no):")
                     if continue_cal.lower() !=  'yes':  
                        print("Thank you for using the calculator. Good bye!.")
                        break
                except ValueError: 
                    print("Error: Invalid input. please enter a numerical value.")
                    
                    
else:
        print("Error: Please select a valid operation.") 