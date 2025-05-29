import os
import datetime
import shutil

path = r"caso-1\Arquivo_de_Teste.md"

# Pegando o nome do arquivo
nome_arquivo = os.path.basename(path)
nome_sem_ext = os.path.splitext(nome_arquivo)[0]

# Backup
os.makedirs("caso-1/backup", exist_ok=True)
shutil.copy(path, f"caso-1/backup/{nome_sem_ext}.md")

# Pegando a data
data_criacao = os.path.getctime(path)
formatar_data = datetime.datetime.fromtimestamp(data_criacao)
apenas_data = str(formatar_data).split()[0]

# Juntando o nome e a data
os.makedirs("caso-1/posts", exist_ok=True)
novo_nome = f"caso-1/posts/{apenas_data}-{nome_sem_ext}.md"

# Salva novo arquivo com a data
shutil.copy(path, novo_nome)

