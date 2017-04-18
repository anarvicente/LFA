

class AFN():
    
    def __init__(self,arquivo):
        
        try:
            arquivo = arquivo.argv[1]
            afn = open(arquivo, 'r')    
        except FileNotFoundError:
            print("Arquivo não existe!")
            exit(1)
        except IndexError:
            print("Arquivo não existe!")
            exit(1)
        
        
        self.transicoes = {}
        
        self.nome_arq = arquivo
        self.titulo = afn.readline()
        estados = afn.readline().strip("\n").split(" ")
        self.estados = int(estados[1])
        self.lista_estados = []
        
        alfabeto = afn.readline().strip("\n").split(" ")
        self.alfabeto = alfabeto[1:]
        
        inicial  = afn.readline().strip("\n").split(" ")
        self.inicial = frozenset(inicial[1:])
        
        final = afn.readline().strip("\n").split(" ")
        self.final = frozenset(final[1:])
        
        inicio_funcao_transicao = afn.readline()
        
        tr = afn.readline()
        while tr != "end":
            tr = tr.strip("\n").split()
            self.transicoes[tr[0],tr[1]] = frozenset(tr[2:]) 
            tr = afn.readline()
       
    
    def toAFD(self):
        afd = {}
        estados = [set(self.inicial)]
    
        for simbolo in self.alfabeto:
            for e in estados:
                for s in self.alfabeto:
                    conjunto = set()
                    for estado in e:
                        try:
                            elem = set(self.transicoes[estado, s]) 
                            conjunto.update(elem.copy()) 
                        except KeyError:
                            self.transicoes[estado, s] = frozenset([])
                    
                    if e.copy() != set() and conjunto.copy() != set():        
                        afd[tuple(e.copy()), s] = conjunto.copy()
                    
                    if conjunto.copy() not in estados and conjunto.copy() != set():
                        estados.append(conjunto.copy())
                        
        self.lista_estados = estados
        return afd
        
    
    def escreve_afd(self,sys,afd):
        
        import re
        
        try:
            arq = open(sys.argv[2],'w')
        except IndexError:
            arq = open(self.nome_arq.strip(".afn")+".afd",'w')
    
        texto = []
        texto.append("AFD version 1\n")
        texto.append("states " + str((2**self.estados)-1) + "\n")
        
        
        texto.append("alfabeth " + re.sub("\[|\]|'|,","",str([simbolo for simbolo in self.alfabeto])) + "\n")
        texto.append("init " + re.sub("\(|\)|,|'","",str(tuple(self.inicial))) + "\n")
        texto.append("finals")
        
        for estado in self.lista_estados:
            for final in self.final:
                if final in estado:
                    texto.append(" "+ re.sub("\'","",str(estado)))
                    
                    
        texto.append("\ntrans" + "\n")
        
        for simbolo in self.alfabeto:
            for estado in self.lista_estados:
                texto.append(re.sub("\{|\}|,|'","",str(estado)) + " " + re.sub("\{|\}|,|'","",str(simbolo)) + " " + re.sub("\{|\}|,|'","",str(afd[tuple(estado),simbolo])) +"\n")
        
        
        texto.append("end")
        arq.writelines(texto)
        arq.close()
        
        
    

import sys
class Main():
    
    automato = AFN(sys)
    
    afd = automato.toAFD()
    
    automato.escreve_afd(sys,afd)
    
    
    print(afd)
        
    
    
    
    
    
    
    
    