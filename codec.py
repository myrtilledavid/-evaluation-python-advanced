def occurence(chaine):
    '''
    retourne un dico avec en clé chaque caractère de la chaine
    et en valeur son nombre d'occurence
    '''
    dico = {}
    for i in chaine:
        if i not in dico:
            dico[i]=1
        else:
            dico[i]+=1
    return dico


class TreeBuilder:
    def __init__(self, text):
        self.text = text

    def tree(self):
        '''
        Renvoie l'arbre binaire de text sous forme d'un dictionnaire
        avec pour chaque caractère sa valeur codée
        '''
        dico = occurence(self.text)
        clefs = sorted(dico.keys(), key=lambda t: -dico[t]) 
        chemin = {}
        while len(clefs)>1:
            a, b = clefs.pop(), clefs.pop() #on sort les deux éléments les moins récurrents
            dico[a+b]=dico[a]+dico[b] #on les fusionne et on rajoute une instance dans le dictionnaire avec comme clé la fusion des deux chaines et comme valeur la somme de leurs occurences
            dico.pop(a) #puis on actualise le dictionnaire
            dico.pop(b)
            if len(a)>1:
                 for i in a:
                     chemin[i] +='0' #0 pour indiquer la branche de gauche
            else:
                chemin[a]='0'
            if len(b)>1:
                for i in b:
                    chemin[i] += '1' #1 pour indiquer la branche de droite
            else:
                chemin[b]='1'
            clefs = sorted(dico.keys(), key=lambda t: -dico[t])
        for i in chemin:
            chemin[i] = chemin[i][::-1]
        return chemin 
        
    
class Codec:
    def __init__(self, binary_tree):
        self.binary_tree = binary_tree
        
    def encode(self, text):
        '''
        Remplace tous les caractères de text
        par leur valeur codée
        '''
        coded = ''
        for i in text:
            coded += self.binary_tree[i]
        return coded
        
    def decode(self, code):
        inv_d = {v: k for k, v in self.binary_tree.items()} #dico inversé avec comme clé la valeur codée et comme valeur le caractère
        inverted_on = []
        result = ''
        for i in code:
            inverted_on.append(i) #liste des caractères de code
        inverted = inverted_on[::-1] #On obtient une liste des caractères du code commencant par la fin
        cha = inverted.pop()
        while cha not in inv_d.keys(): #On cherche à retrouver dans code une clé du dictionnaire de code
            cha += inverted.pop() #tant que cha n'est pas une clé, on lui ajoute un caractère du code (c'est à dire un chiffre) 
        result += inv_d[cha] # on ajoute au résultat le caractère qui est la valeur de la clé cha dans le dico inv_d
        while len(inverted)>1:
            cha = inverted.pop()
            while cha not in inv_d.keys():
                cha += inverted.pop()
            result += inv_d[cha]
        return result