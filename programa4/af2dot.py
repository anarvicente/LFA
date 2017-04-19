""" @package docstring
    Autor: Ana Rubia R. V """

def af2dot(sys):
    """ metodo para escrever um af em um arquivo no formato dot """
    import re
    
    arq = open(sys.argv[1],'r')
    
    try:
        arq_saida = open(sys.argv[2],'w' )
    except IndexError:
        arq_saida = open(sys.argv[1].strip(".afd")+".dot",'w')
    
        
    linha = []
    
    linha.append("digraph finite_state_machine {\n")
    linha.append("size=\"8,5\"" + "\n")
    linha.append("node [shape = doublecircle];")
    
    for i in range(5):
        l = arq.readline()
    
    final = l.split(" ")
    
    for estado_final in final[1:]:
        linha.append(" "+str(estado_final.strip("\n")))
    
    linha.append(";")
    
    linha.append("\nnode [shape = circle]\n")
    
    for i in range(2):
        l = arq.readline()
    
    while l != "end":
        trans = l.split(" ")
        linha.append(str(trans[0])+" -> "+str(trans[2].strip("\n")) + " [label = " + trans[1] + "]\n")
        l = arq.readline()
    linha.append("}")
    
    
    arq_saida.writelines(linha)
    arq_saida.close()



import sys
af2dot(sys)

