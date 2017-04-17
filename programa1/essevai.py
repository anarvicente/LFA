
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
            
    #--------------------------------------------------------        
        
        
        
#pegar elementos da linha de comando
import sys 

class Main():

    
    # novo = set(automato.transicoes[0,'a'])
    # if novo not in estados:
    #     estados.append(novo.copy())
        
    #     afd[0,'a'] = novo.copy()
        
    #     conjunto = set()
    #     for estado in novo:
    #         elem = set(automato.transicoes[estado, 'a'])
    #         conjunto.update(elem.copy())
        
    #     afd[tuple(novo.copy()), 'a'] = conjunto.copy()
        
    #     conjunto = set()
    #     for estado in novo:
    #         elem = set(automato.transicoes[estado, 'b'])
    #         conjunto.update(elem.copy())
        
    
    #     afd[tuple(novo.copy()), 'b'] = conjunto.copy()
        
    #     if novo not in estados:
    #         estados.append(novo.copy())
        
    #     valor_anterior = novo.copy()
    #     #--
    #     novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
    #     conjunto = set()
    #     for estado in novo:
    #         elem = set(automato.transicoes[estado, 'b'])
    #         conjunto.update(elem.copy())
            
        
    #     afd[tuple(novo.copy()), 'b'] = conjunto.copy()
        
    #     if novo not in estados:
    #         estados.append(novo.copy())
        
    #     conjunto = set()
    #     for estado in novo:
    #         elem = set(automato.transicoes[estado, 'a'])
    #         conjunto.update(elem.copy())
        
        
    #     afd[tuple(novo.copy()), 'a'] = conjunto.copy()
        
    #     if novo not in estados:
    #         estados.append(novo.copy())
        
        
    #     novo = afd[tuple(valor_anterior.copy()), 'a'].copy()
        
    #     conjunto = set()
    #     for estado in novo:
    #         elem = set(automato.transicoes[estado, 'a'])
    #         conjunto.update(elem.copy())
        
    #     afd[tuple(novo.copy()), 'a'] = conjunto.copy()
        
        
    #     if novo not in estados:
    #         estados.append(novo.copy())
        
        
    #     novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
        
    #     conjunto = set()
    #     for estado in novo:
    #         elem = set(automato.transicoes[estado, 'b'])
    #         conjunto.update(elem.copy())
        
    #     afd[tuple(novo.copy()), 'b'] = conjunto.copy()
        
    #     if novo not in estados:
    #         estados.append(novo.copy())
        #---------------------------------------------------------
        
        
        
        
        
        # #------------------------------------------------
        # novo = afd[tuple(valor_anterior.copy()), 'a'].copy()
        
        # conjunto = set()
        # for estado in novo:
        #     elem = set(automato.transicoes[estado, 'a'])
        #     conjunto.update(elem.copy())
        
        # afd[tuple(novo.copy()), 'a'] = conjunto.copy()
        
        # if novo not in estados:
        #     estados.append(novo.copy())
        
        # conjunto = set()
        # for estado in novo:
        #     elem = set(automato.transicoes[estado, 'b'])
        #     conjunto.update(elem.copy())
        
        # afd[tuple(novo.copy()), 'b'] = conjunto.copy()
        
        # if novo not in estados:
        #     estados.append(novo.copy())
        
        # #------------------------------------------------------
        
    
    #lembrando de colocar o estado inicial depois, caso isso dê certo
            
            #acabou aqui os estados novos de transicao em a
        
    #----------------------------------------------------    
    #maximo = ((2**(automato.estados))-1)*len(automato.alfabeto)-12 #analisar essa conta
    
    automato = AFN(sys.argv[1])
    
    afd = automato.toAFD()
    # estados = [set(automato.inicial)]

    # for simbolo in automato.alfabeto:
        
        # for init in automato.inicial:
        #     novo = set(automato.transicoes[init,simbolo])
        #     #estados.append(novo.copy())
        #     afd[init,simbolo] = novo.copy()
        
       
        # for si in automato.alfabeto:
        #     conjunto = set()
        #     for estado in novo:
        #         elem = set(automato.transicoes[estado, si])
        #         conjunto.update(elem.copy()) 
            
        #     afd[tuple(novo.copy()), si] = conjunto.copy() 
        
        # valor_anterior = novo.copy()
        
        #for i in range(maximo): #na verdade essa condicao tem que ser -> ENQUANTO HOUVER ESTADOS NOVOS
        
        #for si in automato.alfabeto:
        #   novo = afd[tuple(valor_anterior.copy()), si].copy()     
            
        # for e in estados:
            
        #     for s in automato.alfabeto:
        #         conjunto = set()
        #         for estado in e:
        #             elem = set(automato.transicoes[estado, s]) 
        #             conjunto.update(elem.copy()) 
                    
                    
        #         afd[tuple(e.copy()), s] = conjunto.copy()
                
        #         if conjunto.copy() not in estados:
                    
        #             estados.append(conjunto.copy())
       
        
    #--------------------------------------------------------    
                
        # novo = set(automato.transicoes[0,'b'])
        
        # if novo not in estados:
        #     estados.append(novo.copy())
            
        #     afd[0,'b'] = novo.copy() #{1}
            
        #     conjunto = set()
            
        #     for estado in novo:
        #         elem = set(automato.transicoes[estado, 'b'])
        #         conjunto.update(elem.copy()) #{0,2}
            
        #     afd[tuple(novo.copy()), 'b'] = conjunto.copy() #({1},b) = {0,2}
            
            
        #     conjunto = set()
        #     for estado in novo:
        #         elem = set(automato.transicoes[estado, 'a'])
        #         conjunto.update(elem.copy()) #{2}
            
        
        #     afd[tuple(novo.copy()), 'a'] = conjunto.copy() #({1},a) = {2}
            
        #     if novo not in estados:
        #         estados.append(novo.copy())
            
            # valor_anterior = novo.copy()
            
            # #inicio_loop_estados
            # novo = afd[tuple(valor_anterior.copy()), 'b'].copy() #{0,2}
            
            # #inicio_loop2_em_estados
            # conjunto = set()
            # for estado in novo: # 0,2
            #     elem = set(automato.transicoes[estado, 'b']) 
            #     conjunto.update(elem.copy()) # {1,2}
            
            
            # afd[tuple(novo.copy()), 'b'] = conjunto.copy() #({0,2},b) = {1,2}
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            # conjunto = set()
            # for estado in novo: # 0,2
            #     elem = set(automato.transicoes[estado, 'a']) 
            #     conjunto.update(elem.copy()) #{0,1,2}
            
            
            # afd[tuple(novo.copy()), 'a'] = conjunto.copy() #({0,2},a) = {0,1,2}
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            # #fim_loop2_em_estados
            
            
            # novo = afd[tuple(valor_anterior.copy()), 'a'].copy() #{2}
            
            # conjunto = set()
            # for estado in novo:
            #     elem = set(automato.transicoes[estado, 'a'])
            #     conjunto.update(elem.copy()) #{1,2}
            
            # afd[tuple(novo.copy()), 'a'] = conjunto.copy() #({2},a) = {1,2}
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            # conjunto = set()
            
            
            # for estado in novo: #{2}
            #     elem = set(automato.transicoes[estado, 'b'])
            #     conjunto.update(elem.copy()) #{2}
            
            
            # afd[tuple(novo.copy()), 'b'] = conjunto.copy() #({2},b) = {2}
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            # #fim_loop_estados
            
            # novo = afd[tuple(valor_anterior.copy()), 'b'].copy() #{0,2}
            
            
            # # conjunto = set()
            # # for estado in novo:
            # #     elem = set(automato.transicoes[estado, 'b'])
            # #     conjunto.update(elem.copy()) #{1,2}
            
            # # afd[tuple(novo.copy()), 'b'] = conjunto.copy() #({0,2},b) = {1,2}
            
            # # if novo not in estados:
            # #     estados.append(novo.copy())
                
            
            # valor_anterior = novo.copy()
            # #------------------------------------------------
            # novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
            
            # conjunto = set()
            # for estado in novo:
            #     elem = set(automato.transicoes[estado, 'b'])
            #     conjunto.update(elem.copy())
                
            
            # afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            # conjunto = set()
            # for estado in novo:
            #     elem = set(automato.transicoes[estado, 'a'])
            #     conjunto.update(elem.copy())
            
            
            # afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            
            # novo = afd[tuple(valor_anterior.copy()), 'a'].copy()
            
            # conjunto = set()
            # for estado in novo:
            #     elem = set(automato.transicoes[estado, 'a'])
            #     conjunto.update(elem.copy())
            
            # afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            
            
            # novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
            
            # conjunto = set()
            # for estado in novo:
            #     elem = set(automato.transicoes[estado, 'b'])
            #     conjunto.update(elem.copy())
            
            # afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            # if novo not in estados:
            #     estados.append(novo.copy())
            #---------------------------------------------------------
            
            
            
            
        
    print(len(afd.keys()))        
    print(afd)    
    
    
    try:
        print(sys.argv[2])        
    except IndexError:
        pass