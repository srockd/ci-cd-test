import shutil
import os

# Caminhos das pastas e do arquivo
arquiv_orig = 'Architecture/file.txt'
arquiv_dest = 'Code/file.txt'

# Verifica se o arquivo existe na pasta de origem
if os.path.exists(arquiv_orig):
    # Move o arquivo para a pasta de destino
    shutil.move(arquiv_orig, arquiv_dest)
    print(f'Arquivo {arquiv_orig} movido para {arquiv_dest}')
else:
    print(f'O arquivo {arquiv_orig} não existe.')