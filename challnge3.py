

def hachage(chaine):
    hachage = 1037
    accumulateur = 11  
    
    for caractere in chaine:
        valeur = ord(caractere)
        
        # Décalage dynamique basé sur le caractère et l'accumulateur
        hachage ^= ((hachage << (accumulateur % 5)) & 0xFFFFFFFF)
        hachage += valeur * accumulateur
        
                               
        # inverser certains bits de hachage 
        if valeur % 2 == 0:
            hachage = ~hachage & 0xFFFFFFFF  # Inversion des bits
        
        accumulateur = (accumulateur * 3 + valeur) % 97
    
    # 
    return hachage & 0xFFFFFFFF


texte = "Salam"
texte2="salam"
print(f"Le hachage de '{texte}' est : {hachage(texte)}")
print(f"Le hachage  de '{texte2}' est : {hachage(texte2)}")

