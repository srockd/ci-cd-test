import os
import subprocess

# Configurações obtidas das variáveis de ambiente do TeamCity
GIT_REPO_URL = os.getenv("GIT_REPO_URL", "github.com/srockd/ci-cd-test.git")  # Substitua com seu repositório
REPO_DIR = os.getenv("TEAMCITY_BUILD_CHECKOUTDIR", "Z:/buildAgent/work/5481815137319f3c/build")  # Diretório de destino absoluto
BRANCH = os.getenv("GIT_BRANCH", "main")  # Branch a ser clonada
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Token de acesso pessoal (PAT) do GitHub

def run_command(command, cwd=None):
    """Executa um comando no shell e captura a saída."""
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout

def clone_or_pull_repo():
    """Clona ou atualiza o repositório do GitHub via HTTPS com token."""
    if not GITHUB_TOKEN:
        print("Erro: O token de acesso do GitHub não foi encontrado! Configure GITHUB_TOKEN no TeamCity.")
        exit(1)

    # URL de autenticação com token
    AUTH_GIT_URL = f"https://{GITHUB_TOKEN}@{GIT_REPO_URL}"

    # Se o diretório do repositório já existe, apenas faz pull
    if os.path.exists(os.path.join(REPO_DIR, ".git")):
        print("Repositório já existe. Fazendo pull das últimas mudanças...")
        run_command(f"git pull origin {BRANCH}", cwd=REPO_DIR)
    else:
        print("Clonando o repositório...")
        git_clone_command = f"git clone {AUTH_GIT_URL}"
        run_command(git_clone_command, cwd=os.path.dirname(REPO_DIR))

    print("Repositório atualizado com sucesso!")

if __name__ == "__main__":
    clone_or_pull_repo()
