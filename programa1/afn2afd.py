""" @package docstring
    Autor: Ana Rubia R. V """

class AFN():
    """ Classe para carregar o automato """    
    def __init__(self,arquivo):
        """ recebe o arquivo no formato de um af """
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
        """ metodo para transformar o afn em afd """
        afd = {}
        estados = [list(self.inicial)]
    
        for simbolo in self.alfabeto:
            for e in estados:
                for s in self.alfabeto:
                    conjunto = set()
                    for estado in e:
                        """ tratamento para transicoes nao completas """
                        try:      
                            elem = set(self.transicoes[estado, s]) 
                            conjunto.update(elem.copy()) 
                        except KeyError:
                            self.transicoes[estado, s] = frozenset([])
                    
                    conjunto = conjunto.copy()
                    e = e[:]
                    
                    if conjunto != set():
                        """ordenacao necessaria para renomear os estados posteriormente"""
                        conjunto = list(conjunto)
                        conjunto.sort()   
                        afd[tuple(e), s] = conjunto
                    
                    if conjunto not in estados and conjunto != set():
                        estados.append(conjunto)
                        
        self.lista_estados = estados
        
        return afd
    
    
    def get_lista_estados(self,arquivo):
    
        arq = open(arquivo,'r')
        lista_estados = []
        estados = []
        
        for i in range(6):
            linha = arq.readline()
        
        while linha != "end":
            lista = linha.split(" ")
            lista_estados.append(lista[0])
            lista_estados.append(lista[1:])
            linha = arq.readline()
        
        for estado in lista_estados:
            if estado not in estados:
                estados.append(estado)
        
        return estados
        
        
    
    def renomear(self,afd):
        """ metodo para renomear os estados para facilitar a escrita do arquivo dot """
        renome = {}
        afd_renomeado = {}
        es = 0
        estados_finais = []
        
        for estado in self.lista_estados:
            renome[tuple(estado)] = str(es)
            es+=1
        
        for estado in self.lista_estados:
            for final in self.final:
                if final in estado:
                    estados_finais.append(renome[tuple(estado)])
        
        for chave in afd.keys():
            afd_renomeado[renome[chave[0]],chave[1]] = renome[tuple(afd[chave])]
    
        """ retorno de uma tupla com o novo afd e estados finais porque  preciso saber quem sao os estados finais depois da renomeacao """
        return afd_renomeado,estados_finais 
        
    
    
    def escreve_afd(self,afd,sys):
        """ metodo que escreve num arquivo na formatacao de um afd  """
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
        texto.append("finals " + re.sub("\[|\]|,|\'","",str([estados for estados in afd[1]])))
        
        texto.append("\ntrans" + "\n")
        
        for chave in afd[0].keys():
            texto.append(re.sub("\'","",chave[0]) + " " + re.sub("\'","",chave[1]) + " " + re.sub("\'","",afd[0][chave]) +"\n")
        
        
        texto.append("end")
        arq.writelines(texto)
        arq.close()
        
    
import sys
class Main():
    """ classe main para teste """
    automato = AFN(sys)
    
    afd = automato.toAFD()
    
    r = automato.renomear(afd)
    
    automato.escreve_afd(r,sys)        
    
    
        
    
    
    
    
    
    
    
    