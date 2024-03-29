import ast
from io import TextIOWrapper
import os
import http


tarefas = []


tarefas_salvas: TextIOWrapper
NOME_ARQUIVO = "tarefas.txt"

if os.path.exists(NOME_ARQUIVO):
    try:
        with open(NOME_ARQUIVO, "r", encoding='utf-8') as tarefas_salvas:
            conteudo = tarefas_salvas.read()
            tarefas = ast.literal_eval(conteudo)
    except:
        print("")
        quit()

else:
    print("Arquivo de tarefas não encontrado ! Criando um novo")
    # Cria um novo arquivo de tarefas vazio
    with open(NOME_ARQUIVO, "a") as tarefas_salvas:
        pass


def adicionar_tarefa(nome_tarefa):
    if nome_tarefa == "":
        print("A tarefa precisa de um título")
        return
    tarefa = {"título": nome_tarefa, "completa": False}
    tarefas.append(tarefa)
    print(tarefas)
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as tarefas_salvas:
        tarefas_salvas.write(str(tarefas))
    print(f"Tarefa {nome_tarefa} adicionada com sucesso !")
    return


def ver_tarefas():
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa['completa'] else "❌"
        print(f"tarefa {indice}: {status} {tarefa['título']}")
    return


def atualizar_nome_tarefa(indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = 0 if indice_tarefa == 0 else indice_tarefa - 1
    if indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['título'] = novo_nome_tarefa
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as tarefas_salvas:
            tarefas_salvas.write(str(tarefas))
        print(f"Tarefa {indice_tarefa_ajustado} atualizada para {
            novo_nome_tarefa}")
    else:
        print(f"Tarefa {indice_tarefa_ajustado} não encontrada")


def completar_tarefa(indice_tarefa):
    indice_tarefa_ajustado = 0 if indice_tarefa == 0 else indice_tarefa - 1
    if indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['completa'] = True
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as tarefas_salvas:
            tarefas_salvas.write(str(tarefas))
        print(f"Tarefa {indice_tarefa_ajustado} completada !")
    else:
        print(f"Tarefa {indice_tarefa_ajustado} não encontrada")


def deletar_tarefas_completadas():
    for tarefa in tarefas:
        if tarefa['completa'] == True:
            tarefas.remove(tarefa)
            continue
    ver_tarefas()
    return


while True:
    print('\n Menu do Gerenciador de Lista de Tarefas')
    print('1 - Adicionar tarefa')
    print('2 - Deletar tarefas completadas')
    print('3 - Ver tarefas')
    print('4 - Completar tarefa')
    print('5 - Atualizar tarefa')
    print('6 - Sair')

    try:
        escolha = int(input("Digite sua escolha: "))
    except:
        print("Escolha inválida")
        continue

    if escolha == 0 or escolha > 6:
        print("Escolha inválida")
        continue

    if escolha == 6:
        break

    if escolha == 1:
        nome_tarefa = input("Digite o título da tarefa: ")
        adicionar_tarefa(nome_tarefa)

    if escolha == 2:
        deletar_tarefas_completadas()

    if escolha == 3:
        ver_tarefas()

    if escolha == 4:
        ver_tarefas()
        try:
            indice_tarefa = int(input(
                "Digite o número da tarefa que deseja atualizar: "))
            completar_tarefa(indice_tarefa)
        except ValueError as e:
            print("Dados errados")
            continue

    if escolha == 5:
        ver_tarefas()
        try:
            indice_tarefa = int(input(
                "Digite o número da tarefa que deseja atualizar: "))
            novo_nome = input("Digite o novo título da tarefa: ")
            atualizar_nome_tarefa(indice_tarefa - 1, novo_nome)
        except ValueError as e:
            print("Dados errados")
            continue
