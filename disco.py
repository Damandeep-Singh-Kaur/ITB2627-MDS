edat = int(input("Introduceix la teva edat: "))
entrada = int(input("Tens entrada? (1 = Sí, 0 = No): "))
vestit_blanc = int(input("Vas vestit/da de blanc estil Eivissa? (1 = Sí, 0 = No): "))


if edat >= 18 and entrada == 1 and vestit_blanc == 1:
    print("Pots entrar a la discoteca! Compleixes tots els requisits i portes l'estil Eivissa adequat.")
elif edat >= 18 and entrada == 1 and vestit_blanc != 1:
    print("Tens l'edat i l'entrada, però no pots entrar perquè no vas vestit/da d'estil Eivissa (de blanc).")
elif edat < 18:
    print("No pots entrar a la discoteca perquè ets menor d'edat.")
elif entrada != 1:
    print("No pots entrar a la discoteca perquè no tens entrada.")
else:
    print("No pots entrar a la discoteca.")