import os
import shutil

pasta = "/home/emers/Downloads/"
tipos = [".zip", ".iso", ".jpeg",".pdf"]

arquivo = os.listdir(pasta) #vai ate o caminho transforma os arquivos em uma lista


for arquivos in arquivo:
    for tipo in tipos:
        if arquivos.endswith(tipo):
            aux = tipo.replace(".", "")
            nova_pasta = pasta + aux
            os.makedirs(nova_pasta, exist_ok=True)
            origem = os.path.join(pasta,arquivos)
            shutil.move(origem, nova_pasta)



