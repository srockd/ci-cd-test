import shutil
import os

# Obtém o diretório base do script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos absolutos das pastas e do arquivo
arquiv_orig = os.path.join(base_dir, 'Architecture', 'file.txt')
arquiv_dest = os.path.join(base_dir, 'Code', 'file.txt')

# Verifica se o arquivo existe na pasta de origem
if os.path.exists(arquiv_orig):
    # Move o arquivo para a pasta de destino
    shutil.move(arquiv_orig, arquiv_dest)
    print(f'Arquivo {arquiv_orig} movido para {arquiv_dest}')
else:
    print(f'O arquivo {arquiv_orig} não existe. Diretório atual: {base_dir}')