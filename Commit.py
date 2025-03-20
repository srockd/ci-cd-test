import subprocess
import os

# Configurar usuário do Git
GIT_USER = "srockd"
GIT_EMAIL = "samuelrdiniz@outlook.com"
REPO_DIR = os.getenv("TEAMCITY_BUILD_CHECKOUTDIR", ".")  # Diretório do repositório
BRANCH = "main"  # Nome da branch
GITHUB_TOKEN = "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"  # Use um token do GitHub para autenticação
GITHUB_REPO = "https://github.com/srockd/ci-cd-test.git"  # Substitua com seu repositório

def run_command(command, cwd=None):
    """Executa um comando no shell e retorna a saída."""
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout

def git_commit_and_push():
    """Faz commit e push das mudanças no GitHub."""
    os.chdir(REPO_DIR)  # Muda para o diretório do repositório

    # Configurar nome e e-mail do Git
    run_command(f'git config --global user.name "{GIT_USER}"')
    run_command(f'git config --global user.email "{GIT_EMAIL}"')

    # Adicionar mudanças
    run_command("git add .")

    # Verificar se há mudanças para commit
    status = run_command("git status --porcelain")
    if not status.strip():
        print("Nenhuma mudança para commit.")
        return

    # Criar commit
    run_command('git commit -m "Atualização automática via TeamCity"')

    # Configurar URL remota com autenticação via token
    remote_url = f"https://{GITHUB_TOKEN}@{GITHUB_REPO}"
    run_command(f"git remote set-url origin {remote_url}")

    # Fazer push
    run_command(f"git push origin {BRANCH}")
    print("Mudanças enviadas com sucesso!")

if __name__ == "__main__":
    git_commit_and_push()