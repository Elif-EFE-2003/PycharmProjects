import time

def my_func_1():
    print("1.fonksiyon basliyor")
    time.sleep(5)
    print("1.fonksiyon bitti")
    return 5

def my_func_2():
    print("2.fonksiyon basliyor")
    time.sleep(5)
    print("2.fonksiyon bitti")
    return 10

if __name__=="__main__":
    x=my_func_1()
    y=my_func_2()
    print(f"my func 1'in calismasi sonucu x: {x}")
    print(f"my func 2'nin calismasi sonucu y: {y}")