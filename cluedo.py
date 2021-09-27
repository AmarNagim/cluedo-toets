# Amar Nagim

# alle conclusies
notPassedText = print('Je mag helaas niet op auditie.')


KolonelVanGeelen = 'Je mag op auditie voor de rol van Kolonel van Geelen'
KolonelVanGeelen = False
# voor alle personages
leeftijd = int(input('Hoe oud bent u?: '))
verhuizen = input('Ben je bereid te verhuizen naar Amsterdam?: ').lower()

# per personage
geslacht = input('Wat is uw geslacht?: ').lower()
haarkleur = input('Wat is uw haarkleur?: ').lower()
lengte = input('Wat is uw lengte?: ').lower()
specialiteit = input('Wat is uw specialiteit in het acteren? (boos/onrechtmatig/bekend/slim):')


# conclusie
if leeftijd <18 or verhuizen != 'nee':
    print(notPassedText)
    exit

if leeftijd <18 or verhuizen != 'nee':
    notPassedText = True






