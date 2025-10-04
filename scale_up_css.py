import re

# Ler CSS da Parte 4
with open('parte4-clean-style.txt', 'r', encoding='utf-8') as f:
    css_content = f.read()

def scale_up(match):
    """Aumenta valores em 50%"""
    value = float(match.group(1))
    unit = match.group(2)
    new_value = value * 1.5
    return f"{new_value:.1f}{unit}"

# Aumentar todos os tamanhos em 50%
css_content = re.sub(r'(\d+\.?\d*)(rem|px|em)', scale_up, css_content)

# Salvar CSS aumentado
with open('parte4-scaled-up.txt', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ CSS da Parte 4 aumentado em 50%")

# Aplicar nas Partes 1, 2 e 3
def apply_scaled_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(
        r'<style>.*?</style>',
        css_content,
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ CSS aumentado aplicado em {filename}")

apply_scaled_css('parte1-historia.html')
apply_scaled_css('parte2-solucao.html')
apply_scaled_css('parte3-ecossistema.html')

print("\n🎉 CSS aumentado em 50% aplicado nas Partes 1, 2 e 3!")
