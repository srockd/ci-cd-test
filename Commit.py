import os
import subprocess

# Definir nome e email do usuário Git
GIT_USER_NAME = "srockd"
GIT_USER_EMAIL = "samuelrdiniz@outlook.com"
GIT_REPO_URL = "github.com/srockd/ci-cd-test.git"
BRANCH = "main"

def run_command(command, cwd=None):
    """Executa um comando no shell e exibe a saída."""
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout

# Configurar identidade do Git no ambiente TeamCity
print("Configurando identidade do Git...")
run_command(f'git config --global user.name "{GIT_USER_NAME}"')
run_command(f'git config --global user.email "{GIT_USER_EMAIL}"')

# Adicionar mudanças ao Git
print("Adicionando arquivos ao Git...")
run_command("git add .")

# Fazer commit das mudanças
print("Fazendo commit...")
run_command('git commit -m "Atualização automática via TeamCity"')

# Obter token do GitHub a partir da variável de ambiente
GITHUB_TOKEN = "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"

if not GITHUB_TOKEN:
    print("Erro: O token do GitHub não está definido.")
    exit(1)

# Criar URL de autenticação com token
REPO_WITH_AUTH = f"https://{GITHUB_TOKEN}@{GIT_REPO_URL}"

# Fazer push para o repositório
print("Enviando alterações para o GitHub...")
run_command(f"git push {REPO_WITH_AUTH} {BRANCH}")

print("Processo concluído com sucesso!")