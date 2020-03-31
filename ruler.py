import numpy as np
from colorama import Fore, Style

penalite = 1

def green_text(text):
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"

def comparaison(a, b):
    if a == b:
        return 0
    #elif a == '-' or b == '-':
    #    return 1
    return 1

def matriceM(seq1, seq2):
    '''
    Renvoie la matrice de cout de passage entre les deux séquences en argument
    Elle permet de déterminer les modifications les moins couteuses pour superposer les deux mots
    '''
    m = len(seq1)
    n = len(seq2)
    M =  np.full((m,n),0)
    M[0][0] = comparaison(seq1[0], seq2[0])
    for i in range(1,m): #Les termes sur la première ligne et première colonne sont remplis automatiquement
        M[i][0] = M[i-1][0] + penalite
    for j in range(1,n):
        M[0][j] = M[0][j-1] + penalite
    for i in range(1,m):
        for j in range(1,n):
            poidsdiag = M[i-1][j-1] + comparaison(seq1[i],seq2[j])
            poidsverti = M[i-1][j] + penalite
            poidshoriz = M[i][j-1] + penalite
            M[i][j] = min(poidsdiag, poidsverti, poidshoriz) #si la pénalité est négative, il faudra maximiser le poids des chemins pris
    return M


class Ruler:
    def __init__(self, seq1, seq2, distance=0):
        self.seq1 = seq1
        self.seq2 = seq2
        self.distance = distance
        
    def compute(self):
        """
        Effectue la comparaison des deux mots de l'objet
        """
        m = len(self.seq1)
        n = len(self.seq2)
        if n == 0: #garde-fou s'il n'y a qu'un seul mot
            self.seq2 += m*'w'
            return(self.seq1,self.seq2)
        if m == 0:
            self.seq1 += n*'w'
            return(self.seq1,self.seq2)
        M = matriceM(self.seq1,self.seq2)
        seq1m = ''
        seq2m = ''
        i, j = m-1, n-1
        while i>0 and j>0: #On essaye d'emprunter le chemin le moins couteux en 'remontant' la matrice M
            if M[i][j] == M[i-1][j-1] + comparaison(self.seq1[i],self.seq2[j]):
                seq1m += self.seq1[i]
                seq2m += self.seq2[j]
                i-=1
                j-=1
            elif M[i][j] == M[i][j-1] + penalite:
                seq1m += '='
                seq2m += self.seq2[j]
                j-=1
            elif M[i][j] == M[i-1][j] + penalite:
                seq1m += self.seq1[i]
                seq2m += '='
                i-=1
        while i > 0:
            seq1m += self.seq1[i]
            seq2m += '='
            i -= 1
        while j > 0:
            seq1m += '='
            seq2m += self.seq2[j]
            j -= 1
        seq1m += self.seq1[0] #Pour les premiers termes de seq1 et seq2
        seq2m += self.seq2[0]
        seq1m = seq1m[::-1]
        seq2m = seq2m[::-1]
        self.seq1 = seq1m
        self.seq2 = seq2m
        
        n = len(self.seq1) #mise à jour de la distance
        for i in range(n):
            if self.seq1[i] != self.seq2[i]:
                self.distance +=1
        
    def report(self):
        '''
        Impression des deux séquences en mettant en évidence leurs différences avec des couleurs
        '''
        seq1f = ''
        seq2f = ''
        n = len(self.seq1)
        for i in range(n):
            if self.seq1[i] == self.seq1[i]:
                seq1f += self.seq1[i]
                seq2f += self.seq2[i]
            elif self.seq1[i] == '=':
                seq1f += green_text('=')
                seq2f += self.seq2[i]
            elif self.seq1[i] == '=':
                seq1f += self.seq1[i]
                seq2f += green_text('=')
            elif self.seq1[i] != self.seq1[i]:
                seq1f += green_text(self.seq1[i])
                seq2f += green_text(self.seq2[i])
        return(seq1f, seq2f)