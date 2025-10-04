import re

def fix_navigation(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir a função goToSlide para não fazer loop
    old_pattern = r'currentSlide = \(n \+ totalSlides\) % totalSlides;'
    new_code = '''// Limitar navegação sem loop
            if (n < 0) {
                currentSlide = 0;
            } else if (n >= totalSlides) {
                currentSlide = totalSlides - 1;
            } else {
                currentSlide = n;
            }'''
    
    content = re.sub(old_pattern, new_code, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Loop removido de {filename}")

# Aplicar nas 4 partes
fix_navigation('parte1-historia.html')
fix_navigation('parte2-solucao.html')
fix_navigation('parte3-ecossistema.html')
fix_navigation('parte4-piloto.html')

print("\n🎉 Loop automático removido de todas as partes!")
