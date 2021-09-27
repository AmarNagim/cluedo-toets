# Amar Nagim

# alle conclusies
notPassedText = 'Je mag helaas niet op auditie.'
KolonelVanGeelen = 'Je mag op auditie voor de rol van Kolonel van Geelen.'
DomineeGroenewoud = 'Je mag op auditie voor de rol van Dominee Groenewoud.'
ProfessorPimpel = 'Je mag op auditie voor de rol van Professor Pimpel.'
MwDeWit = 'Je mag op auditie voor de rol van Mevrouw de Wit.'
RosaRoodhart = 'Je mag op auditie voor de rol van Rosa Roodhart.'
BlaauwVanDraet = 'Je mag op auditie voor de rol van Mevrouw Blaauw van Draet.'

# voor alle personages
leeftijd = int(input('Hoe oud bent u?: '))
verhuizen = input('Ben je bereid te verhuizen naar Amsterdam?: ').lower()

# per personage
geslacht = input('Wat is uw geslacht?: ').lower()
haarkleur = input('Wat is uw haarkleur?: ').lower()
lengte = input('Wat is uw lengte?: ').lower()
specialiteit = input('Wat is uw specialiteit in het acteren? (bekend/slim/militair/acteur/geestelijke/koken):').lower()


# conclusie
if leeftijd <18 or verhuizen != 'nee':
    print(notPassedText)
    exit

elif geslacht == 'man' and specialiteit == 'militair' and leeftijd >= 35 and leeftijd <= 60:    # Kolonel van Geelen
    print(KolonelVanGeelen)

elif geslacht == 'man' and specialiteit == 'geestelijke' and lengte >= 175 and lengte <= 195:    
    print(DomineeGroenewoud)

elif geslacht == 'man' and specialiteit == 'slim' and leeftijd >= 55




