# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def data_processing(string):
    string = string.strip()
    try:    
        if abs(int(string)) == 6 or abs(int(string)) == 7: print(True)
        else: print(False)
    except ValueError: print("Вы ввели некорректные данные")


value = input("Введите число - ")
data_processing(value)