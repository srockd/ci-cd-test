import os
import subprocess

# Configurações
GIT_REPO_URL = "https://github.com/srockd/ci-cd-test.git"  # Substitua com seu repositório
REPO_DIR = os.getenv("TEAMCITY_BUILD_CHECKOUTDIR", "Z:/buildAgent/work/5481815137319f3c/build")  # Diretório de destino absoluto
BRANCH = "main"  # Branch a ser clonada
GITHUB_TOKEN = "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"  # Token de acesso pessoal (PAT) do GitHub

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
    if GITHUB_TOKEN is None:
        print("Erro: O token de acesso do GitHub não foi encontrado!")
        exit(1)

    # Se o diretório do repositório já existe, apenas faz pull
    if os.path.exists(os.path.join(REPO_DIR, ".git")):
        print("Repositório já existe. Fazendo pull das últimas mudanças...")
        run_command(f"git pull origin {BRANCH}", cwd=REPO_DIR)
    else:
        print("Clonando o repositório...")
        git_clone_command = f"git clone https://{GITHUB_TOKEN}:x-oauth-basic@{GIT_REPO_URL[8:]}"
        run_command(git_clone_command, cwd=os.path.dirname(REPO_DIR))

    print("Repositório atualizado com sucesso!")

if __name__ == "__main__":
    clone_or_pull_repo()
