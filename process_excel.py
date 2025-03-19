import os
import shutil
import sys

# Verifica se um arquivo foi passado como argumento
if len(sys.argv) < 2:
    print("Erro: Nenhum arquivo Excel especificado.")
    sys.exit(1)

file_path = sys.argv[1]

# Definição dos diretórios
architecture_dir = "Architecture"
code_dir = "Code"

# Verifica se o arquivo existe
if not os.path.exists(file_path):
    print(f"Erro: O arquivo {file_path} não foi encontrado.")
    sys.exit(1)

# Nome do arquivo sem o caminho
file_name = os.path.basename(file_path)

# Caminho final para mover o arquivo
destination_path = os.path.join(code_dir, file_name)

print(f"Processando arquivo: {file_path}")

# Simula processamento (adicione sua lógica aqui)
print("Lendo arquivo Excel...")
# Aqui você pode usar pandas para processar o arquivo se necessário

# Move o arquivo para Code/
shutil.move(file_path, destination_path)
print(f"Arquivo movido para: {destination_path}")

# Confirmação final
print("Processamento concluído.")