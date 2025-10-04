#!/bin/bash

# Backup dos arquivos originais
cp parte1-historia.html parte1-historia.html.bak
cp parte2-solucao.html parte2-solucao.html.bak
cp parte3-ecossistema.html parte3-ecossistema.html.bak

# Reduzir fontes em 20% (multiplicar por 0.8)
for file in parte1-historia.html parte2-solucao.html parte3-ecossistema.html; do
    # Reduzir font-size
    sed -i 's/font-size: \([0-9.]*\)rem/font-size: \1rem/g' "$file"
    sed -i 's/\([0-9.]*\)rem/echo "scale=2; \1 * 0.8" | bc/ge' "$file"
    
    # Reduzir padding
    sed -i 's/padding: \([0-9]*\)px/padding: $(echo "scale=0; \1 * 0.8 / 1" | bc)px/ge' "$file"
done

echo "Ajustes aplicados!"
