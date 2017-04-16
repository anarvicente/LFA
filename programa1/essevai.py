
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
       

#pegar elementos da linha de comando
import sys 

class Main():
    automato = AFN(sys.argv[1])
    
    afd = {}
    estados = []
    
    novo = set(automato.transicoes[0,'a'])
    if novo not in estados:
        estados.append(novo.copy())
        
        afd[0,'a'] = novo.copy()
        
        conjunto = set()
        for estado in novo:
            elem = set(automato.transicoes[estado, 'a'])
            conjunto.update(elem.copy())
        
        afd[tuple(novo.copy()), 'a'] = conjunto.copy()
        
        conjunto = set()
        for estado in novo:
            elem = set(automato.transicoes[estado, 'b'])
            conjunto.update(elem.copy())
        
    
        afd[tuple(novo.copy()), 'b'] = conjunto.copy()
        
        if novo not in estados:
            estados.append(novo.copy())
        
        valor_anterior = novo.copy()
        #------------------------------------------------
        novo = afd[tuple(valor_anterior.copy()), 'a'].copy()
        
        conjunto = set()
        for estado in novo:
            elem = set(automato.transicoes[estado, 'a'])
            conjunto.update(elem.copy())
        
        afd[tuple(novo.copy()), 'a'] = conjunto.copy()
        
        if novo not in estados:
            estados.append(novo.copy())
        
        conjunto = set()
        for estado in novo:
            elem = set(automato.transicoes[estado, 'b'])
            conjunto.update(elem.copy())
        
        afd[tuple(novo.copy()), 'b'] = conjunto.copy()
        
        if novo not in estados:
            estados.append(novo.copy())
        
            #------------------------------------------------------
        
    
    #lembrando de colocar o estado inicial depois, caso isso dê certo
            
            #acabou aqui os estados novos de transicao em a
                
        novo = set(automato.transicoes[0,'b'])
        
        if novo not in estados:
            estados.append(novo.copy())
            
            afd[0,'b'] = novo.copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'b'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'a'])
                conjunto.update(elem.copy())
            
        
            afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            valor_anterior = novo.copy()
            #------------------------------------------------
            novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'b'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'a'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            #------------------------------------------------------
            
            novo = afd[tuple(valor_anterior.copy()), 'a'].copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'a'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'b'])
                conjunto.update(elem.copy())
            
            
            afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            
            novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
            
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'b'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            #---------------------------------------------------------
            
            valor_anterior = novo.copy()
            #------------------------------------------------
            novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'b'])
                conjunto.update(elem.copy())
                
            
            afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'a'])
                conjunto.update(elem.copy())
            
            
            afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            
            #------------------------------------------------------
            
            novo = afd[tuple(valor_anterior.copy()), 'a'].copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'a'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'a'] = conjunto.copy()
            
            
            if novo not in estados:
                estados.append(novo.copy())
            
            
            novo = afd[tuple(valor_anterior.copy()), 'b'].copy()
            
            conjunto = set()
            for estado in novo:
                elem = set(automato.transicoes[estado, 'b'])
                conjunto.update(elem.copy())
            
            afd[tuple(novo.copy()), 'b'] = conjunto.copy()
            
            if novo not in estados:
                estados.append(novo.copy())
            #---------------------------------------------------------
            
            
            
            
        
    print(afd.items())        
        
            
            
        
        
        
        
        
        
    
    
    
    
    
    
    
    try:
        print(sys.argv[2])        
    except IndexError:
        pass