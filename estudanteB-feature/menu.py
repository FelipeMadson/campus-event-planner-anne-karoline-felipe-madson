# estudanteb.py - Módulo de Interação com Usuário e Relatórios (Anne - Estudante B)

import os
import sys

# adiciona estudanteA-feature ao sys.path de forma simples e direta (caminho absoluto)
_estudanteA = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "estudanteA-feature"))
if _estudanteA not in sys.path:
    sys.path.insert(0, _estudanteA)

import funcoes_eventos as funcoes

def display_menu(): 
    print("\n=== Planejador de Eventos ===") 
    print("1. Adicionar evento") 
    print("2. Ver todos os eventos") 
    print("3. Buscar evento por nome") 
    print("4. Deletar evento por ID") 
    print("5. Sair") 
def ler_inteiro(prompt):
    try:
        return int(input(prompt).strip())
    except (ValueError, TypeError):
        return None
def main(): 
     while True:
         display_menu() 
         escolha = ler_inteiro("Escolha (1-5): ") 
         if escolha == 1: 
             id_input = ler_inteiro("ID do evento: ")
             if id_input is None: 
                 print("ID inválido.") 
                 continue
             nome = input("Nome: ").strip() 
             data = input("Data (dd/mm/aaaa): ").strip() 
             if not funcoes.validar_data(data):
                 print("Data inválida.")
                 continue 
             local = input("Local: ").strip() 
             categoria = input("Categoria: ").strip() 
             participado = input("Participado? (s/N): ").strip().lower() in ("s","sim","y","yes") 
             funcoes.criar_evento(id_input, nome, data, local, categoria, participado) 
             print("Evento criado.")
         elif escolha == 2: 
             if not funcoes.eventos: 
                 print("Nenhum evento cadastrado.") 
             else: 
                 funcoes.listar_eventos()
         elif escolha == 3:
             termo = input("Nome (ou parte) para buscar: ").strip()
             encontrados = funcoes.buscar_nome_evento(termo, substring=True) 
             if encontrados: 
                 print("\nEventos encontrados:") 
                 for ev in encontrados: 
                     print(ev) 
             else:
                 print("Nenhum evento encontrado.") 
         elif escolha == 4: 
             id_del = ler_inteiro("ID do evento a deletar: ")
             if id_del is None: 
                 print("ID inválido.") 
                 continue 
             removido = funcoes.deletar_evento(id_del)
             if removido: 
                 print("Removido:", removido) 
             else: print("Nenhum evento com esse ID.") 
         elif escolha == 5: 
             print("Saindo.")
             break 
         else: 
             print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
        main()
