import re

def reduce_size(match):
    """Reduce font size by 20%"""
    value = float(match.group(1))
    unit = match.group(2)
    new_value = value * 0.8
    return f"{new_value:.1f}{unit}"

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reduce font-size
    content = re.sub(r'font-size:\s*(\d+\.?\d*)([a-z]+)', reduce_size, content)
    
    # Reduce padding
    content = re.sub(r'padding:\s*(\d+\.?\d*)([a-z]+)', reduce_size, content)
    
    # Reduce margin
    content = re.sub(r'margin:\s*(\d+\.?\d*)([a-z]+)', reduce_size, content)
    
    # Reduce gap
    content = re.sub(r'gap:\s*(\d+\.?\d*)([a-z]+)', reduce_size, content)
    
    # Reduce line-height (numeric values)
    content = re.sub(r'line-height:\s*(\d+\.?\d*)([a-z]+)', reduce_size, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filename} processado")

# Process all 3 parts
process_file('parte1-historia.html')
process_file('parte2-solucao.html')
process_file('parte3-ecossistema.html')

print("\n🎉 Redução de 20% aplicada em todas as partes!")
