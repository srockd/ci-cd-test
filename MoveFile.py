import os
import subprocess

# ConfiguraÃ§Ãµes
GIT_REPO_URL = "https://github.com/srockd/ci-cd-test.git"  # Substitua com seu repositÃ³rio
REPO_DIR = os.getenv("TEAMCITY_BUILD_CHECKOUTDIR", "/home/teamcity/build")  # DiretÃ³rio do repositÃ³rio
BRANCH = "main"  # Branch a ser clonada
GITHUB_TOKEN = "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"  # Token de acesso pessoal (PAT) do GitHub

def run_command(command, cwd=None):
    """Executa um comando no shell e captura a saÃ­da."""
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout

def clone_or_pull_repo():
    """Clona ou atualiza o repositÃ³rio do GitHub via HTTPS com token."""
    if GITHUB_TOKEN is None:
        print("Erro: O token de acesso do GitHub nÃ£o foi encontrado!")
        exit(1)

    # Se o diretÃ³rio do repositÃ³rio jÃ¡ existe, apenas faz pull
    if os.path.exists(os.path.join(REPO_DIR, ".git")):
        print("RepositÃ³rio jÃ¡ existe. Fazendo pull das Ãºltimas mudanÃ§as...")
        run_command(f"git pull origin {BRANCH}", cwd=REPO_DIR)
    else:
        print("Clonando o repositÃ³rio...")
        git_clone_command = f"git clone https://{GITHUB_TOKEN}:x-oauth-basic@{GIT_REPO_URL[8:]}"
        run_command(git_clone_command, cwd=os.path.dirname(REPO_DIR))

    print("RepositÃ³rio atualizado com sucesso!")

if __name__ == "__main__":
    clone_or_pull_repo()
