import json #salva e carrega tarefas em um arquivo json (leve e fácil de ler)
from datetime import datetime #vai lidar com as datas

#arquivo para salvar as tarefas
task_file = "tasks.json"

def load_tasks():
    try: #tenta abrir o arquivo task.json e lê o conteudo usando json.load()
        with open(task_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[] #se o arquivo não existir, vai retornar uma lista vazia
    
def save_tasks(tasks):
    with open(task_file, "w") as file: #abre o arquivo no modo escrita "w"
        json.dump(tasks, file, indent=4) #usa o json.dump() para gravar a lista de tarefas no arquivo, formatada com ident=4 para facilitar leitura
        
def add_task(tasks): #vai solicitar a tarefa + data de vencimento
    #cria um dicionário com os dados da tarefa
    title = input("Tarefa: ")
    due_date = input("Vencimento (DD-MM-AAAA): ") 
    task = {"title": title, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks(tasks) #salva a lista atualizada no arquivo JSON
    print("Tarefa adicionada com sucesso :)") #aviso de tarefa adicionada 
    
def list_tasks(tasks): #mostra a lista de tarefas
    print("\nSuas tarefas:")
    for idx, task in enumerate(tasks): #indice de tarefas
        status = "Concluída" if task ["completed"] else "Pendente"
        print(f"{idx + 1}. {task["title"]} - {task["due_date"]} [{status}]") 
        
def complete_task(tasks):
    list_tasks(tasks) #mostra todas as tarefas numeradas
    try:
        task_number = int(input("\nDigite o número da tarefa que deseja marcar como concluída"))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Tarefa concluída! :)")
        else:
            print("Opção inválida")
    except ValueError:
        print("Insira um número válido")
        
def edit_task(tasks):
    list_tasks(tasks)
    try:
        task_number = int(input("\nDigite o número da tarefa que deseja editar"))
        if 1 <= len(tasks):
            task = tasks[task_number - 1]
            print(f"Editando tarefa {task['title']}")
            
            new_title = input("Nome da tarefa (pressione Enter para manter o atual): ")
            new_due_date = input("Nova data de vencimento (pressione Enter para manter a atual): ")
            
            if new_title.strip():  #vai removr os caracteres existentes para adicionar os novos da edção
                task['title'] = new_title
            if new_due_date.strip():
                task['due_date'] = new_due_date
                
            save_tasks(tasks)
            print("Tarefa editada com sucesso :)")
        else:
            print("Numero inválido")
    except ValueError:
        print("Insira um número válido.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_number = int(input("\nDigite o número da tarefa que deseja excluir"))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1) #task.pop exclui a tarefa no JSON e o -1 muda o numero da tarefa posterior
            save_tasks(tasks)
            print(f"Tarefa '{removed_task["title"]}' excluída com sucesso :)")
        else:
            print("Opção inválida")
    except ValueError:
        print("Insira um numero válido")
            

#menu para comandos de adicionar, listar ou sair        
def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Adicionar tarefa como concluída")
        print("4. Editar tarefa")
        print("5. Excluir tarefa")
        print("6. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            break
        else:
            print("Opção inválida")
            
if __name__ == "__main__":
    main() #garante que o código principal só seja executado quando o arquivo for executado diretamente (e não importado como módulo).
