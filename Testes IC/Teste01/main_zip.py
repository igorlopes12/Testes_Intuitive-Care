from zipfile import *
import zipfile

with ZipFile('Teste_1.zip',"w") as myzip:
    myzip.write("Lista_procedimentos.pdf")
    myzip.write("Lista_procedimentos.xlsx")
    myzip.write("Diretrizes_utilização.pdf")
    myzip.write("Diretrizes_clinicas.pdf")
    myzip.write("Protocolo_utilizacao.pdf")