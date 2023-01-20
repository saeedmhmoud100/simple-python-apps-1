First = float(input("first number: "))
second = float(input("second number: "))
result = float(input("result: "))
total = First + second
multiply = First * second
power1 = First ** second
power2 = second ** First
difference1 = First - second
difference2 = second - First
division = First / second
division2 = second / First
remainder = First % second
if result == total:
    print(First, "+", second, "=", result)
if result == multiply:
    print(First, "*", second, "=", result)
if result == power1:
    print(First, "**", second, "=", result)
elif result == power2:
    print(second, "**", First, "=", result)
if result == difference1:
    print(First, "-", second, "=", result)
if result == difference2:
    print(second, "-", First, "=", result)
if result == division:
    print(First, "/", second, "=", result)
if result == division2:
    print(second, "-", First, "=", result)
if result == remainder:
    print(First, "%", second, "=", result)
