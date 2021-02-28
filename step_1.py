import tkinter
import PIL

str1 = "abc"
str2 = "bcd"
print(str1<str2)

# первый комментарий
msg1 = "Всем привет!"
print(msg1)

iYears = input("Сколько Вам лет? ")
print(f"Вам {iYears}")


# обработка секунд ========================================================
iSeconds = int(input("Введите число секунд: "))
iHours = int(iSeconds / 3600)
iSeconds = iSeconds % 3600
iMinutes = int(iSeconds / 60)
iSeconds = iSeconds % 60
# приведение к формату hh:mm:ss
if iHours > 9:
    sHours = str(iHours)
else:
    sHours = "0"+str(iHours)

if iMinutes > 9:
    sMinutes = str(iMinutes)
else:
    sMinutes = "0"+str(iMinutes)

if iSeconds > 9:
    sSeconds = str(iSeconds)
else:
    sSeconds = "0" + str(iSeconds)

print(f"Вы ввели {sHours}:{sMinutes}:{sSeconds}")

# n + nn + nnn =============================================
iNum= int(input("Введите число n: "))
iResult = 123*iNum
print(f"n + nn + nnn = {iResult}")

# самая большая цифра в числе ==============================
sNum = input("Введите число: ")
iMax = 0
iLength = len(sNum)
i=0
while i < iLength :
    if int(sNum[i]) > iMax:
        iMax = int(sNum[i])
    i = i + 1

print(f"Максимальная цифра в числе {sNum} : {iMax}")

# работа фирмы ==============================
iRevenue = int(input("Введите выручку: "))
iCosts = int(input("Введите расходы: "))
iProfit = iRevenue - iCosts
if iProfit > 0:
    print("У нас есть прибыль!")
    fRent = iProfit / iRevenue
    print(f"Рентабельность: {fRent}")
    nEmployees = int(input("Введите число сотрудников: "))
    if nEmployees > 0:
        fIpE = iProfit / nEmployees
        print(f"Прибыль на сотрудника : {fIpE}")
else:
    print("У нас убытки :(")

# спортсмен ==============================
iDay1 = int(input("Введите дистанцию первого дня: "))
iFinal = int(input("Введите итоговую дистанцию: "))
fCurrent = iDay1
iDay = 1
while fCurrent<iFinal:
    fCurrent *= 1.1
    iDay += 1

print(f"Результат достигнут после : {iDay} дней")


