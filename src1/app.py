
import numpy as np
from src1.all_logic_gates import logic_gates
    

def insert_column_one(matrix):
    for row in matrix:
        row.insert(2, 1)
    return matrix

def switch_zero(matrix):
    """Recebe uma matriz e troca os valores 0 por -1

    Args:
        matrix (list): Uma matriz multidimensional com valores logicos 0 e 1

    Returns:
        list: Retorna uma matriz multidimensional com valores logicos -1 e 1
    """
    arr = np.asarray(matrix)
    np.place(arr, arr==0, [-1]) # substitui onde o valor for  0 por -1
    return arr
            
        
def modifying_weights(matrix):
    """Calcula o valor dos pesos seguindo a Lei de Hebb

    Args:
        matrix (list): Recebe uma matriz, com valores logicos e calcula o valor dos pesos 

    Returns:
        list: Retorna uma lista com os pesos calculados
    """
    row_aux = []
    old_row = [0,0,0]
    for row in matrix:
        # multiplica valores da 3 posicao da lista com cada elemento ate a posicao 3
        row_aux = [ value * row[3] for value in row[:3]]
        # soma do valor dos pesos antigos com os novos(calculados  pelo algoritmo de Hebb)
        sum_rows = [sum(ele) for ele in zip(old_row, row_aux)] 
        old_row.clear()
        # a lista antiga passa ser a lista com os pesos calculados neste ciclo
        old_row = sum_rows
    return old_row   
 

def main(logic_gates):
    
    """Recebe uma dicionario com cada chave sendo o nome e da funcao logica 
    e o valor uma matriz de os valores logicos, chamam as funcoes responsaveis por calcular a Lei de Hebb
    mostram o resultado da matriz e o valor dos pesos e cria um arquivo txt com os resultados"""
    
    with open("logic_gates.txt", 'w') as file:
        for count,gate in enumerate(logic_gates):
            print(f" {count + 1} - {gate.upper()} :" )
            file.writelines(f" {count + 1} - {gate.upper()} :\n")
            change_zero = switch_zero( insert_column_one(logic_gates[gate])[1:])
            
            for row in change_zero:
                print(f"\t{row}")
                file.writelines(f"\t{row}\n")
            
            print(f"\n=> calculated weights:{modifying_weights(change_zero)}\n")
            file.writelines(f"\t=> calculated weights: {modifying_weights(change_zero)}\n")
            file.writelines("\n")
        

if __name__ == "__main__":
    main(logic_gates)
    



