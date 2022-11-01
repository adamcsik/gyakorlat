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


def hossz(jelszo, karakterhossz):
    hiba = False
    if len(jelszo) < karakterhossz:
        print(f'Túl rövid a jelszó (min {karakterhossz} karakter)!')
        hiba = True
    return hiba


def szamjegy(jelszo, szjegy):
    if not szjegy:
        hiba = False
        return hiba
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].isnumeric():
            hiba = False
            break
    if hiba:
        print('Nincs számjegy a jelszóban!')
    return hiba


def jelszo_ellenorzese(karakter,szjegy):
    psw = ''
    hibakod = 1
    while hibakod != 0:
        hibakod = 0
        psw = input('Kérek egy jelszót: ')
        if hossz(psw, karakter):
            hibakod += 1
        if szamjegy(psw, szjegy):
            hibakod += 1
        if nagybetu(psw):
            hibakod += 1
        if kisbetu(psw):
            hibakod += 1
    print('\nMegfelelő jelszót adott meg!')
    return psw
