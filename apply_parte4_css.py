import re

# Ler o CSS completo da Parte 4
with open('parte4-clean-style.txt', 'r', encoding='utf-8') as f:
    parte4_css = f.read()

def replace_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir todo o bloco <style>...</style>
    new_content = re.sub(
        r'<style>.*?</style>',
        parte4_css,
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ CSS da Parte 4 aplicado em {filename}")

# Aplicar nas 3 partes
replace_css('parte1-historia.html')
replace_css('parte2-solucao.html')
replace_css('parte3-ecossistema.html')

print("\n🎉 CSS idêntico aplicado em todas as partes!")
