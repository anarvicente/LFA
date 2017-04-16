
class AFN():

    def __init__(self,arquivo):
        afn = open(arquivo, 'r')
        
        transicoes = {}
        
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
        
        transicao = afn.readline()
        while transicao != "end":
            transicao = transicao.strip("\n").split()
            transicoes[(int(transicao[0]),transicao[1])] = [int(i) for i in transicao[2:]] #analisar isso
            transicao = afn.readline()
        
        self.transicao = dict(transicoes)
       

#pegar elementos da linha de comando
import sys 

class Main():
    automato = AFN(sys.argv[1])
    
    afd = {}
    
    estados = []
    is_novo = []
    novo = []
    
    transicao = automato.transicao.copy()
    
    # inicio de tudo
    estados.append(list(automato.inicial)[0])
    
    tam = len(estados)
    
    novo.append(transicao[estados[tam-1],'a'])
    
    afd[(0,'a')] = list(novo)

    if novo not in estados and novo != automato.inicial:
        estados.append(list(novo[0])) #novo = [[0,1]]
        
    tam = len(estados) 
    
    is_novo.append(list(transicao[estados[tam-1][0], 'a'])) #is_novo = [[0,1]]
    
    is_novo[0].append(list(transicao[estados[tam-1][1], 'a'])[0]) # is_novo = [[0,1,2]]
    
    chave = tuple(estados[tam-1])
    afd[chave,'a'] = is_novo #como lista eh mutavel, nao pode ser chave
    
    novo = []
    
    novo.append(list(is_novo))
    
    if novo not in estados and novo != automato.inicial:
        estados.append(list(novo[0]))
    
    tam = len(estados)
    
    is_novo = []
    
    is_novo.append(list(transicao[estados[tam-1][0][0], 'a']))
    
    if list(transicao[estados[tam-1][0][1], 'a'])[0] not in is_novo:
        is_novo[0].append(list(transicao[estados[tam-1][0][1], 'a'])[0]) # is_novo=
    
    
    if list(transicao[estados[tam-1][0][1], 'a'])[0] not in is_novo[0]:
        is_novo[0].append(list(transicao[estados[tam-1][0][2], 'a'])[0]) # is_novo=
    
    print(is_novo)
    
    chave = tuple(estados[tam-1][0])
    
    afd[chave,'a'] = is_novo #como lista eh mutavel, nao pode ser chave
    
    
    #if type(chave) == tuple:
    print(afd)
    
        
    

    
    
    
    
    
    
    
    
    
    
    
            # for i in range(len(automato.transicao[(estado, caracter)])):
            #     temp.append(automato.transicao[(estado, caracter)][i])
                
                
            # if temp not in estado_temp:
            #     estado_temp.append(temp)
                                        
    # print(estado_temp)
    
    
    
    
    
    # for simbolo in automato.alfabeto:
    #     novo_estado = []
    #     for e in range(automato.estados):
    #         for t in automato.transicao[e, simbolo]:
    #             if t not in novo_estado:
    #                 novo_estado.append(t)
    #         print(novo_estado)       
    
    # while tem_estado_novo:
    #     for estado in range(automato.estados):
            
    #         for caracter in automato.alfabeto:
    #             temp = []
                
                
                
    #             for i in range(len(automato.transicao[(estado, caracter)])):
    #                 temp.append(automato.transicao[(estado, caracter)][i])
                
                
    #             if temp not in estado_temp:
    #                 estado_temp.append(temp)
                    
    #                 tam = len(estado_temp)
    #                 temp = []
    #                 for i in range(len(estado_temp[tam-1])):
    #                     temp.append(automato.transicao[(estado, caracter)][i])
                    
                     
                
    #                 for i in range(len(estado_temp[tam-1][0])):
    #                     temp.append(automato.transicao[(estado_temp[tam-1][0][i], caracter)])
                    
    #                 for i in range(len(estado_temp[tam-1][0])):
    #                     for estado in estado_temp[tam-1][i]:
    #                         print(estado)
                                
                # else:
                #     tem_estado_novo = False                        
            
                
    
    #print(estado_temp)

    #isso aqui eu tenho que verificar dentro da funcao para salvar 
    try:
        print(sys.argv[2])        
    except IndexError:
        pass

#-------------------------------------------#


        
        
        
        

