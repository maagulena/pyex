#Napisz funkcję, która będzie prostą wersją gry „Kamień, papier, nożyce”. Może to być wersja polska lub angielska. Funkcja jako argumenty przyjmuje dwa stringi („kamień”, „papier” lub „nożyce”), a następnie w formie alertu podaje wynik (czyli np. wypisuje „Gracz nr 1 wygrał” – zakładamy, że gracz numer 1 to osoba, która podała pierwszy string). Jeśli do funkcji zostanie podany nieodpowiedni argument, tj. taki, który nie jest ani kamieniem, ani papierem, ani nożycami, poinformuj o tym gracza wyświetlając alert z tekstem.
allowedinp = ['kamień', 'papier', 'nożyce', 'zakończ']

def gra(x,y):
    if inpGracz1 == inpGracz2:
        wyn = 'Remis'
    elif inpGracz1 == 'kamień' and inpGracz2 == 'nożyce':
        wyn = 'Gracz1'
    elif inpGracz1 == 'nożyce' and inpGracz2 == 'kamień':
        wyn = 'Gracz2'
    elif inpGracz1 == 'papier' and inpGracz2 == 'nożyce':
        wyn = 'Gracz2'
    elif inpGracz1 == 'nożyce' and inpGracz2 == 'papier':
        wyn = 'Gracz1'
    elif inpGracz1 == 'kamień' and inpGracz2 == 'papier':
        wyn = 'Gracz2'
    elif inpGracz1 == 'papier' and inpGracz2 == 'kamień':
        wyn = 'Gracz1'
    else:
        print("Błąd. Spróbuj jeszcze raz")
    return wyn

countGracz1 = 0
countGracz2 = 0
while True:
    while True:
        inpGracz1 = input("Gracz 1 - Wpisz kamień, papier lub nożyce.  Wpisz zakończ aby zakończyć: ")
        inpGracz1 = inpGracz1.strip()
        if not inpGracz1 in allowedinp:
            print("Błąd. Wpisz kamień, papier lub nożyce.  Wpisz zakończ aby zakończyć: ")
            continue
        elif inpGracz1 == 'zakończ':
            print('Ok papa!')
            exit()
        else: break
    while True:
        inpGracz2 = input("Gracz 2 - Wpisz kamień, papier lub nożyce.  Wpisz zakończ aby zakończyć: ")
        inpGracz2 = inpGracz2.strip()
        if not inpGracz2 in allowedinp:
            print("Błąd. Wpisz kamień, papier lub nożyce.  Wpisz zakończ aby zakończyć: ")
            continue
        elif inpGracz2 == 'zakończ':
            print('Ok papa!')
            exit()
        else: break
    # gra(inpGracz1,inpGracz2) zwraca wartość zmiennej wyn
    if gra(inpGracz1,inpGracz2) == 'Remis':
        print('Remis')
    elif gra(inpGracz1,inpGracz2) == 'Gracz1':
        print('Gracz 1 wygrywa')
        countGracz1 += 1
    elif gra(inpGracz1,inpGracz2) == 'Gracz2':
        print('Gracz 2 wygrywa')
        countGracz2 +=1
    cont = input ('Chcesz grać dalej? t/n: ')
    if cont == 't': continue
    elif cont == 'n':
        break
print('Wynik Gracz1:', countGracz1, 'Wynik Gracz2:', countGracz2)
