import os
import subprocess

GIT_REPO_URL = "github.com/srockd/ci-cd-test.git"
GITHUB_TOKEN = "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"  # Pegando o token do ambiente
BRANCH = "main"

if not GITHUB_TOKEN:
    print("Erro: O token do GitHub não está definido.")
    exit(1)

def run_command(command, cwd=None):
    """Executa um comando e exibe a saída."""
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout

def git_push():
    """Faz commit e push no GitHub."""
    print("Adicionando arquivos ao Git...")
    run_command("git add .")

    print("Fazendo commit...")
    run_command('git commit -m "Atualização automática via TeamCity"')

    print("Enviando alterações para o GitHub...")
    push_command = f"git push https://{GITHUB_TOKEN}:x-oauth-basic@{GIT_REPO_URL} {BRANCH}"
    run_command(push_command)

if __name__ == "__main__":
    git_push()