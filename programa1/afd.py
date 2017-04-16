
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
        self.inicial = [int(i) for i in inicial[1:]]
        
        final = afn.readline().strip("\n").split(" ")
        self.final = [int(i) for i in final[1:]]
        
        inicio_funcao_transicao = afn.readline()
        
        tr = afn.readline()
        while tr != "end":
            tr = tr.strip("\n").split()
            self.transicoes[(int(tr[0]),tr[1])] = frozenset([int(i) for i in tr[2:]]) #analisar isso
            tr = afn.readline()
        
        
       

#pegar elementos da linha de comando
import sys 

class Main():
    automato = AFN(sys.argv[1])
    afd = {}
    #primeira iteracao
    estados = []
    # novo = set(automato.transicoes[0,'a'])
    # estados.append(novo.copy())
    
    for simbolo in automato.alfabeto:
        novo = set(automato.transicoes[0,simbolo]).copy()
        afd[0,simbolo] = novo.copy()
        if novo not in estados:
            estados.append(novo.copy())
    
        tam = len(estados)
        novo.clear()
        conjunto = set()
        
        for i in range(tam):
            for estado in estados[i]:
                for s in automato.alfabeto:
                    elem = set(automato.transicoes[estado, s]).copy()
                    conjunto.update(elem)
            
                afd[tuple(list(estados[i])), s] = conjunto.copy()
                novo = conjunto.copy()
                if novo not in estados:
                    estados.append(novo.copy())
                
                print(estados)
                
            conjunto.clear()
        
        
        # #segunda iteracao
        # if novo not in estados:
        #     estados.append(novo.copy())
        
        # tam = len(estados)
        
        # for estado in estados[tam-1]:
        #     elem = set(automato.transicoes[estado, 'a']).copy()
        #     conjunto.update(elem)
        
        # afd[tuple(list(estados[tam-1])), 'a'] = conjunto.copy()
        
    #muda para b agora
    # conjunto.clear()
    
    # if novo not in estados:
    #     estados.append(novo.copy())
    
    # tam = len(estados)
    # for i in range(tam):
    #     if type(estados[i]) != int:
    #         for estado in estados[i]:
    #             elem = set(automato.transicoes[estado,'b']).copy()
    #             conjunto.update(elem)
            
    #         afd[tuple(list(estados[i])), 'b'] = conjunto.copy()
    #         conjunto.clear()
    #     else:
    #         elem = set(automato.transicoes[0,'b']).copy()
    #         afd[0, 'b'] = elem.copy()
    
    
    print(afd)
    #print(automato.transicoes)
    #isso aqui eu tenho que verificar dentro da funcao para salvar 
    try:
        print(sys.argv[2])        
    except IndexError:
        pass

#-------------------------------------------#


        
        
        
        

