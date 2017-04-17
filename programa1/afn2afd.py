

class AFN():
    
    def __init__(self,arquivo):
        afn = open(arquivo, 'r')
        
        self.transicoes = {}
        
        self.nome_arq = arquivo
        self.titulo = afn.readline()
        estados = afn.readline().strip("\n").split(" ")
        self.estados = int(estados[1])
        
        
        alfabeto = afn.readline().strip("\n").split(" ")
        self.alfabeto = alfabeto[1:]
        
        inicial  = afn.readline().strip("\n").split(" ")
        self.inicial = frozenset([int(i) for i in inicial[1:]])
        
        final = afn.readline().strip("\n").split(" ")
        self.final = frozenset([int(i) for i in final[1:]])
        
        inicio_funcao_transicao = afn.readline()
        
        tr = afn.readline()
        while tr != "end":
            tr = tr.strip("\n").split()
            self.transicoes[(int(tr[0]),tr[1])] = frozenset([int(i) for i in tr[2:]]) #analisar isso
            tr = afn.readline()
       
    
    def toAFD(self):
        afd = {}
        estados = [set(self.inicial)]
    
        for simbolo in self.alfabeto:
            
            for e in estados:
                
                for s in self.alfabeto:
                    conjunto = set()
                    for estado in e:
                        elem = set(self.transicoes[estado, s]) 
                        conjunto.update(elem.copy()) 
                        
                        
                    afd[tuple(e.copy()), s] = conjunto.copy()
                    
                    if conjunto.copy() not in estados:
                        
                        estados.append(conjunto.copy())
        return afd
        
        
        

import sys
class Main():
    
    
    automato = AFN(sys.argv[1])
    
    afd = automato.toAFD()
    
    
    print(len(afd.keys()))
    
    print(afd)