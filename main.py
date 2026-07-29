import os
import shutil

pasta = "/home/emers/Downloads/"

extensoes = {
    #Imagens
    ".jpeg": "Imagens",
    ".jpg": "Imagens",
    ".png": "Imagens",

    #
    ".docx": "Documentos",
    ".pdf": "Documentos",
    ".txt": "Documentos",
    ".odt": "Documentos",

    #Compactados
    ".zip": "Compactados",
    ".tar": "Compactados",
    ".gz": "Compactados",

    #Executaveis
    ".exe": "Programas",
    ".deb": "Programas",
    ".AppImage": "Programas",

    #Imagens de disco
    ".iso": "ISO"
}
#Obtem uma lista com os arquivos da pasta
arquivos = os.listdir(pasta)

#percorre todos os arquivos da pasta
for arquivo in arquivos:
    #Monta o caminho completo do arquivo
    origem = os.path.join(pasta,arquivo)

    #Separa o caminho do arquivo e sua extensão
    nome_arquivo, extensao = os.path.splitext(origem)

    #Procura a extensão no dicionário e obtem o nome da pasta correspondente
    lista_caminho = extensoes.get(extensao)

    #Verifica se a extensão existe no dicionário
    if lista_caminho:

        #Variavel que recebe o caminho completo a ser criado
        nova_pasta = pasta + lista_caminho
        #Cria a pasta se ela nao existir
        os.makedirs(nova_pasta, exist_ok=True)
        #Move os arquivos para a pasta correspondente
        shutil.move(origem, nova_pasta)
        



