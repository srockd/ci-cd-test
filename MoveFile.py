import shutil
import os

# Diretório base onde o script está rodando
BASE_DIR = os.getenv("TEAMCITY_BUILD_CHECKOUTDIR", "Z:/buildAgent/work/5481815137319f3c")

# Caminhos completos
arquiv_orig = os.path.join(BASE_DIR, "Architecture", "file.txt")
arquiv_dest = os.path.join(BASE_DIR, "Code", "file.txt")

# Verifica se o arquivo existe na pasta de origem
if os.path.exists(arquiv_orig):
    # Move o arquivo para a pasta de destino
    shutil.move(arquiv_orig, arquiv_dest)
    print(f'Arquivo {arquiv_orig} movido para {arquiv_dest}')
else:
    print(f'O arquivo {arquiv_orig} não existe.')