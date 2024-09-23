from datetime import datetime

#Cria arquivo de texto com conteúdo inicial
def criarArquivo(): 
    with open("ArquivoDeTexto.txt", "w") as arquivo:
        arquivo.write("Conteúdo inicial.\n")
    print("Arquivo criado e conteúdo escrito com sucesso!") 

#Acrescenta item e data fornecidos pelo usuário ao arquivo
def acrescentarConteudo(item, data): 
    with open("ArquivoDeTexto.txt", "a") as arquivo:
        arquivo.write(f"Item: {item}, Data: {data}\n")
    print("Item e data adicionados com sucesso!")

#Lê e exibe o conteúdo do arquivo linha por linha
def leituraConteudoLinha(): 
    print("Conteúdo do arquivo:")
    with open("ArquivoDeTexto.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())

#Exibe conteúdo atual do arquivo
print("ToDo - List")
print("ToDo - List Atual")
print("-" * 30)
leituraConteudoLinha()
print("-" * 30)

#Solicita o item e valida se tem mais de um caractere
while True:
    itemLista = input("Item: ")
    if len(itemLista) < 2:
        print("Erro: O item deve conter pelo menos dois caracteres.")
    else:
        print(f"Item aceito: {itemLista}")
        break

#Solicita a data e valida se é futura ou igual ao dia atual
while True:
    dataInput = input("Digite a data (formato: DD-MM): ")
    try:
        anoAtual = datetime.now().year
        dataItem = datetime.strptime(dataInput + f"-{anoAtual}", "%d-%m-%Y")
        
        dataAtual = datetime.now()
        dataVerificacao = datetime(year=anoAtual, month=dataAtual.month, day=dataAtual.day)
        
        if dataItem >= dataVerificacao:
            print(f"Data aceita: {dataItem.strftime('%d-%m-%Y')}")
            break
        else:
            print("Erro: A data deve ser futura ou igual ao dia atual.")
    
    except ValueError:
        print("Erro: Formato de data inválido. Use DD-MM.")

#Acrescenta Item + Data
acrescentarConteudo(itemLista, dataItem.strftime('%d-%m-%Y'))

print("-" * 30)
print("Conteúdo atualizado do arquivo")
leituraConteudoLinha()
print("-" * 30)
