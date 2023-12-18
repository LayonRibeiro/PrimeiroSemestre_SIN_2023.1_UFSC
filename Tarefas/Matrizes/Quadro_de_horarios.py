n_linhas = 1 
m_colunas = 6 # dias letivos da semana (segunda a a sabado)
matriz = [ {"0730": None,"0820": None, "0910": None, "1010": None, "1100": None, "1330": None, "1420": None, "1510": None, "1620": None, "1710": None, "1830": None, "1920": None, "2020": None, "2110": None} for _ in range(m_colunas) ] #um dicionario para cada dia da semana


num = int(input())
for i in range(num):
    
    entrada = input().split()
    if len(entrada) == 2:
        disciplina, aula1 = entrada
        aula2 = None 
    else:
        disciplina, aula1, aula2 = entrada
    
    for j in range(2):
        hor_req = []
        dia_semana = int(aula1[0])-2 #adptar o dia ao indice da matriz
        horario = (aula1[1:-1])
        qntd_aulas= int(aula1[-1])
 
#Coloca em uma lista todos os horários requeridos pela qtnd de aulas
        hor_req = [horario]
        for i in range(qntd_aulas-1):
            aula_seguinte = str((int(horario)+50))
            if int(aula_seguinte[-2::]) >= 60:
                aula_seguinte = str(int(aula_seguinte)+40)
                if int(aula_seguinte) == 2010:
                    aula_seguinte = "2020"
            horario = aula_seguinte
            hor_req.append(aula_seguinte)
   
#verifica se todos os horários requeridos estao disponiveis antes de marcar as aulas
        for horas in hor_req:
            if matriz[dia_semana][horas] == None:
                horario_vago = True
            else:
                horario_vago = False
                conflito = horas
                break
# Isere as aulas nos horários requeridos
        if horario_vago:
            for horas in hor_req:
                matriz[dia_semana][horas] = disciplina
        else:
            print(matriz[dia_semana][conflito], disciplina)
            
        aula1 = aula2 # repete para a aula do outro dia
