import re

def increase_size(match):
    """Increase size by 35%"""
    value = float(match.group(1))
    unit = match.group(2)
    new_value = value * 1.35
    return f"{new_value:.1f}{unit}"

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Increase font-size
    content = re.sub(r'font-size:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    
    # Increase padding
    content = re.sub(r'padding:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    
    # Increase margin
    content = re.sub(r'margin:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    
    # Increase gap
    content = re.sub(r'gap:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    
    # Increase border-radius
    content = re.sub(r'border-radius:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    
    # Increase width/height (for dots, icons, etc)
    content = re.sub(r'width:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    content = re.sub(r'height:\s*(\d+\.?\d*)([a-z]+)', increase_size, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filename} aumentado em 35%")

# Process all 3 parts
process_file('parte1-historia.html')
process_file('parte2-solucao.html')
process_file('parte3-ecossistema.html')

print("\n🎉 Aumento de 35% aplicado em todas as partes!")
