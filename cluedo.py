# Amar Nagim

# initiele text
print("""
Er zullen u een aantal vragen worden gesteld die u naar waarheid moet beantwoorden.
Daaruit zal blijken of je wel of niet op auditie wordt gevraagd.""")
print()

# alle conclusies
notPassedText = 'Je mag helaas niet op auditie.'
KolonelVanGeelen = 'Je mag op auditie voor de rol van Kolonel van Geelen.'
DomineeGroenewoud = 'Je mag op auditie voor de rol van Dominee Groenewoud.'
ProfessorPimpel = 'Je mag op auditie voor de rol van Professor Pimpel.'
MwDeWit = 'Je mag op auditie voor de rol van Mevrouw de Wit.'
RosaRoodhart = 'Je mag op auditie voor de rol van Rosa Roodhart.'
BlaauwVanDraet = 'Je mag op auditie voor de rol van Mevrouw Blaauw van Draet.'

# algemene eisen
leeftijd = int(input('Hoe oud bent u?: '))
verhuizen = input('Ben je bereid te verhuizen naar Amsterdam?: ').lower()
algemeneEisen = False
# per personage
geslacht = input('Wat is uw geslacht?: ').lower()
haarkleur = input('Wat is uw haarkleur?: ').lower()
lengte = input('Wat is uw lengte?: ').lower()
specialiteit = input('Wat is uw specialiteit in het acteren? (bekendheid/slim/militair/acteur/geestelijke/koken):').lower()


if leeftijd <18 or verhuizen == 'nee':
    algemeneEisen == True


# conclusie

if algemeneEisen == True:
    print(notPassedText)

elif geslacht == 'man' and specialiteit == 'militair' and leeftijd >= 35 and leeftijd <= 60:  # Kolonel van Geelen
    print()  
    print(KolonelVanGeelen)

elif geslacht == 'man' and specialiteit == 'geestelijke' and lengte >= 175 and lengte <= 195:   
    print()
    print(DomineeGroenewoud)

elif geslacht == 'man' and specialiteit == 'slim' and leeftijd >= 55:
    print()
    print(ProfessorPimpel)

elif geslacht == 'vrouw' and specialiteit == 'koken' and leeftijd >= 40 and leeftijd <= 60:
    print()
    print(MwDeWit)

elif geslacht == 'vrouw' and specialiteit == 'acteur' and leeftijd >= 20 and leeftijd <= 30:
    print()
    print(RosaRoodhart)

elif geslacht == 'vrouw' and specialiteit == 'bekendheid' and leeftijd >25 and leeftijd <=40:
    print()
    print(BlaauwVanDraet)      

else:
    print()
    print(notPassedText)
