import os
import subprocess

# Definir nome e email do usuário Git usando variáveis de ambiente
GIT_USER_NAME = os.getenv("GIT_USER_NAME", "srockd")
GIT_USER_EMAIL = os.getenv("GIT_USER_EMAIL", "samuelrdiniz@outlook.com")
GIT_REPO_URL = os.getenv("GIT_REPO_URL", "github.com/srockd/ci-cd-test.git")
BRANCH = os.getenv("GIT_BRANCH", "main")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Token armazenado de forma segura

def run_command(command, cwd=None):
    """Executa um comando no shell e exibe a saída."""
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout

# Verificar se o token foi definido
if not GITHUB_TOKEN:
    print("Erro: O token do GitHub não está definido! Configure a variável GITHUB_TOKEN no TeamCity.")
    exit(1)

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

# Criar URL de autenticação segura
AUTH_GIT_URL = f"https://{GITHUB_TOKEN}@{GIT_REPO_URL}"

# Fazer push para o repositório
print("Enviando alterações para o GitHub...")
run_command(f"git push {AUTH_GIT_URL} {BRANCH}")

print("Processo concluído com sucesso!")
