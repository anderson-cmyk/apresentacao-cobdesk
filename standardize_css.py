import re

# Padrões da Parte 4 (referência)
STANDARDS = {
    'padding_slide': '64px',
    'max_width': '1120px',
    'title_size': '4.8rem',
    'title_weight': '900',
    'title_spacing': '-2.4px',
    'subtitle_size': '2rem',
    'section_title_size': '3.2rem',
    'section_title_weight': '800',
    'text_size': '1.6rem',
    'small_text_size': '1.28rem',
    'card_padding': '32px',
    'card_border': '1.6px',
    'card_radius': '20.8px',
    'gap': '24px',
    'margin': '32px',
}

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Atualizar padding do slide
    content = re.sub(r'padding:\s*[\d.]+px;', f'padding: {STANDARDS["padding_slide"]};', content, count=5)
    
    # Atualizar max-width
    content = re.sub(r'max-width:\s*[\d.]+px;', f'max-width: {STANDARDS["max_width"]};', content, count=3)
    
    # Salvar
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filename} atualizado")

# Processar arquivos
update_file('parte1-historia.html')
update_file('parte2-solucao.html')
update_file('parte3-ecossistema.html')

print("\n🎉 Padronização concluída!")
