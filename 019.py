try:
    num = int(input("enter: "))
    print(10 / num)

except ZeroDivisionError:
    print("num can not 0")
except ValueError:
    print("input must exist")

