from datetime import datetime


def sprawdz_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel[4:6])
    
    if miesiac > 20:
        miesiac -= 20
        rok += 2000
    elif miesiac > 12:
        miesiac -= 40
        rok += 1800
    else:
        rok += 1900
    
    try:
        datetime(rok, miesiac, dzien)
    except ValueError:
        return False

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10))
    kontrolna = (10 - suma % 10) % 10
    if kontrolna != int(pesel[-1]):
        return False

    return True

def data_urodzenia(pesel):
    if not sprawdz_pesel(pesel):
        return "Niepoprawny PESEL"
    
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel[4:6])
    temp = pesel[9]
    temp = int(temp)
    plec = ""
    if temp % 2 == 0:
        plec = "kobieta"
    else:
        plec = "mężczyzna"
    if miesiac > 20:
        miesiac -= 20
        rok += 2000
    elif miesiac > 12:
        miesiac -= 40
        rok += 1800
    else:
        rok += 1900

    data_urodzenia = datetime(rok, miesiac, dzien)
    return data_urodzenia.strftime("%d-%B-%Y" + ", płeć: " + plec)

pesel = "12221189567"
data = data_urodzenia(pesel)


f = open ("daty.txt", "w")
f.write("Data urodzenia: " + data)
f = open("daty.txt","r")
print(f.read())