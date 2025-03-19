#!/bin/bash

# Diretório da pasta Architecture
ARCH_DIR="Architecture"
CODE_DIR="Code"

# Verifica se há arquivos Excel novos na pasta Architecture
EXCEL_FILES=$(git diff --name-status HEAD~1 HEAD | grep "^A" | grep "$ARCH_DIR/.*\.xlsx" | awk '{print $2}')

if [ -z "$EXCEL_FILES" ]; then
    echo "Nenhum novo arquivo Excel adicionado. Encerrando script."
    exit 0
fi

echo "Novos arquivos Excel detectados:"
echo "$EXCEL_FILES"

# Executa o script Python para processar os arquivos
for FILE in $EXCEL_FILES; do
    python process_excel.py "$FILE"
done