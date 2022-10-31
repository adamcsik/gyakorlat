def nagybetu(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].isupper():
            hiba = False
            break
    if hiba:
        print('Nincs benne nagybetű!')
    return hiba


def kisbetu(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].islower():
            hiba = False
            break
    if hiba:
        print('Nincs benne kisbetű!')
    return hiba


def hossz(jelszo):
    hiba = False
    if len(jelszo) <8:
        print('Túl rövid a jelszó (min 8 karakter)!')
        hiba = True
    return hiba


def szamjegy(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].isnumeric():
            hiba = False
            break
    if hiba:
        print('Nincs számjegy a jelszóban!')
    return hiba


def jelszo_ellenorzese():
    hibakod = 1
    while hibakod != 0:
        hibakod = 0
        psw = input('Kérek egy jelszót: ')
        if hossz(psw):
            hibakod +=1
        if szamjegy(psw):
            hibakod +=1
        if nagybetu(psw):
            hibakod +=1
        if kisbetu(psw):
            hibakod +=1
    print('\nMegfelelő jelszót adott meg!')
    return psw


def felhasznalo():
    print("REGISZTRÁCIÓ\n")
    felhasznalonev = input('Kérem a felhasználónevet (email): ')
    while '@' not in felhasznalonev or '.' not in felhasznalonev or '' not in felhasznalonev:
        print('Nem jó az email!')
        felhasznalonev = input('Kérem megint a felhasználónevet (email): ')
    with open('psw.txt', 'a', encoding='utf-8') as user:
        user.write('\n' + felhasznalonev)


def jelszokeres():
    jelszo1 = jelszo_ellenorzese()
    jelszo2 = input("\nKérem ismét a jelszót: ")
    probalkozas = 1
    while jelszo1 != jelszo2:
        probalkozas += 1
        if probalkozas == 4:
            break
        jelszo2 = input("\nA jelszó nem egyezik, kérem ismét a jelszót: ")
    if probalkozas != 4:
        print('\nElfogadtam a jelszót! Vége a regisztrációnak!')
        with open('psw.txt', "a", encoding='utf-8') as jelszofajl:
            jelszofajl.write(';' + jelszo1)
    else:
        print('\nSajnálom, hogy nem iskerült jó jelszót megadnia! \n VISZLÁT!')


def beleptetes():
    print("BELÉPÉS")
    user = []
    with open('psw.txt', 'r', encoding='utf-8') as user_fajl:
        for sor in user_fajl:
            user.append(sor.strip().split(';'))
    felhasznalonev = input('Kérem a felhasználó nevét: ')
    van = False
    i = 0
    for i in range(len(user)):
        if user[i][0] == felhasznalonev:
            van = True
            break
    if van:
            jelszo = input('Kérem a jelszót: ')
            probalkozas = 1
            while jelszo != user[i][1]:
                print('Nem megfelelő a jelszó!')
                jelszo = input('Kérem a jelszót: ')
                probalkozas += 1
                if probalkozas == 4:
                    break
            if probalkozas == 4:
                print('BELÉPÉS megtagadva!')
            else:
                print('BELÉPÉS engedélyezve!')
    else:
        print("Nincs ilyen felhasználó!")

# Innen indul a program
# felhasznalo()
# jelszokeres()
# beleptetes()

