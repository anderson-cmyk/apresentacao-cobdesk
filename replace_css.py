import re

# Ler o CSS da Parte 4
with open('parte4-style-only.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

def replace_css_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir tudo entre <style> e </style>
    content = re.sub(
        r'<style>.*?</style>',
        new_css,
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ CSS substituído em {filename}")

# Processar os 3 arquivos
replace_css_in_file('parte1-historia.html')
replace_css_in_file('parte2-solucao.html')
replace_css_in_file('parte3-ecossistema.html')

print("\n🎉 CSS padronizado em todas as partes!")
