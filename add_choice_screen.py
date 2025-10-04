import re

# Template da tela de escolha
CHOICE_SCREEN = '''
    <!-- Slide: Escolha a Próxima Parte -->
    <div class="slide">
        <div class="slide-content">
            <h1 class="slide-title">Qual parte você quer ver agora?</h1>
            <p class="slide-subtitle">Escolha para onde ir ou volte ao início</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; margin-top: 48px; max-width: 900px; margin-left: auto; margin-right: auto;">
                <a href="parte1-historia.html" style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 32px; text-decoration: none; color: white; transition: all 0.3s; display: block;">
                    <div style="font-size: 2rem; margin-bottom: 8px;">📖</div>
                    <div style="font-size: 1.4rem; font-weight: 600;">Parte 1</div>
                    <div style="font-size: 0.9rem; color: #98989D; margin-top: 4px;">A Jornada de Calabró</div>
                </a>
                
                <a href="parte2-solucao.html" style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 32px; text-decoration: none; color: white; transition: all 0.3s; display: block;">
                    <div style="font-size: 2rem; margin-bottom: 8px;">🔍</div>
                    <div style="font-size: 1.4rem; font-weight: 600;">Parte 2</div>
                    <div style="font-size: 0.9rem; color: #98989D; margin-top: 4px;">A Busca pela Solução</div>
                </a>
                
                <a href="parte3-ecossistema.html" style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 32px; text-decoration: none; color: white; transition: all 0.3s; display: block;">
                    <div style="font-size: 2rem; margin-bottom: 8px;">🎯</div>
                    <div style="font-size: 1.4rem; font-weight: 600;">Parte 3</div>
                    <div style="font-size: 0.9rem; color: #98989D; margin-top: 4px;">O Ecossistema Cobdesk</div>
                </a>
                
                <a href="parte4-piloto.html" style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(255, 165, 0, 0.3); border-radius: 16px; padding: 32px; text-decoration: none; color: white; transition: all 0.3s; display: block;">
                    <div style="font-size: 2rem; margin-bottom: 8px;">🚀</div>
                    <div style="font-size: 1.4rem; font-weight: 600;">Parte 4</div>
                    <div style="font-size: 0.9rem; color: #98989D; margin-top: 4px;">Proposta de Piloto</div>
                </a>
                
                <a href="https://script.google.com/a/macros/aalima.com.br/s/AKfycbzS2Tofm-NQhO5BAspDlmHgXewmAkPvAzEB2uNEm1iD0BKrYzR9YfdmZirtGIznV4LVpw/exec" target="_blank" style="background: rgba(48, 209, 88, 0.1); border: 2px solid #30D158; border-radius: 16px; padding: 32px; text-decoration: none; color: white; transition: all 0.3s; display: block;">
                    <div style="font-size: 2rem; margin-bottom: 8px;">🚀</div>
                    <div style="font-size: 1.4rem; font-weight: 600; color: #30D158;">Cobdesk</div>
                    <div style="font-size: 0.9rem; color: #98989D; margin-top: 4px;">Experimentar ao vivo</div>
                </a>
                
                <a href="index.html" style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 32px; text-decoration: none; color: white; transition: all 0.3s; display: block;">
                    <div style="font-size: 2rem; margin-bottom: 8px;">🏠</div>
                    <div style="font-size: 1.4rem; font-weight: 600;">Início</div>
                    <div style="font-size: 0.9rem; color: #98989D; margin-top: 4px;">Voltar ao Caleidoscópio</div>
                </a>
            </div>
        </div>
    </div>
'''

def add_choice_to_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar o último slide antes do fechamento do script
    # Inserir a tela de escolha antes do </body>
    if '<!-- Slide: Escolha a Próxima Parte -->' not in content:
        content = content.replace('</body>', CHOICE_SCREEN + '\n</body>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Tela de escolha adicionada em {filename}")
    else:
        print(f"⚠️  {filename} já tem tela de escolha")

# Adicionar nas 4 partes
add_choice_to_file('parte1-historia.html')
add_choice_to_file('parte2-solucao.html')
add_choice_to_file('parte3-ecossistema.html')
add_choice_to_file('parte4-piloto.html')

print("\n🎉 Telas de escolha adicionadas em todas as partes!")
