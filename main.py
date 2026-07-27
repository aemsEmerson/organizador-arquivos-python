import os
import shutil

pasta = "/home/emers/Downloads/"

arquivo = os.listdir(pasta) #vai ate o caminho transforma os arquivos em uma lista

#Percorre todos os arquivos da pasta
for arquivos in arquivo:
    #Monta o caminho completo do arquivo
    origem = os.path.join(pasta,arquivos)

    #separa o nome da extensão
    arquivo_ext = os.path.splitext(origem)

    #Testa se o arquivo possui extensão
    if arquivo_ext[1]:
        #Remove o ponto da extensão (.pdf -> pdf)
        nova_pasta = pasta + arquivo_ext[1].replace('.',"")

        #Cria a pasta caso ela nao exista
        os.makedirs(nova_pasta, exist_ok=True)

        #Move o arquivo para a pasta correspondente 
        shutil.move(origem, nova_pasta)



