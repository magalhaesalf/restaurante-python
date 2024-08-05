import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo': True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo': False}]

def exibir_nome_do_programa():
      ''' Exibe o nome do restaurante '''

      print(""" 𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼 🍵""")
def exibir_opcoes():
      ''' Exibe as opções disponíveis. '''

      print('1. Cadastrar restaurante ')
      print('2. Listar restaurante ')
      print('3. Alternar estado do restaurante ')
      print('4. Sair  ')
      print('\n')

def voltar_ao_menu_principal():
      ''' pede ao usuário para selecionar uma teclar para voltar ao menu '''

      input(' Digite uma tecla para voltar ao menu principal ')
      main()

def opcao_invalida():
      ''' Exibe a mensagem opção inválida e retorna ao menu principal'''

      print(' Opção inválida! \n')
      voltar_ao_menu_principal()

def exibir_subtitulos(texto):
      ''' Exibe um subtítulo estilizado na tela 
Inputs:
-texto: str - Texto do subtitulo 
'''

      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      ''' Cadastra novos restaurante 
      Inputs:
      Nome do restaurante
      Categoria

      Outputs:
      Novo restaurante adicionado
      '''
      exibir_subtitulos('Cadastro de novos restaurantes')
     
      nome_do_restaurante = input( 'Informe o nome do restaurante que você deseja cadastrar: \n')
      categoria = input(f' Digite o nome da categoria do restaurante: {nome_do_restaurante}.')
      dados_do_restaurante = {'nome':nome_do_restaurante, 
                              'categoria':categoria, 'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f' O restaurante {nome_do_restaurante} foi cadastrado com sucesso !')
      voltar_ao_menu_principal()

def listar_restaurantes():
      ''' Exibe uma tabela com os dados dos restaurantes cadastrados 
      Outputrs:
      Exibe a tabela de restaurantes.
      '''
      exibir_subtitulos(' Listando restaurantes ')
      print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      ''' Altera o status do restaurante
      Output:
      - Exibe mensagem indicando o sucesso da operação.

      '''
      exibir_subtitulos('Alternando estado do restaurante')

      nome_restaurante = input('Digite o nome do restaurante que desejas alternar o estado: ')
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante: {nome_restaurante}. Foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante: {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)

      if not restaurante_encontrado:
            print('O restaurante não foi encontrado ')

      voltar_ao_menu_principal()

def escolher_opcao():
      ''' Solicita uma opção do usuário 
      Output:
      - Executa a opção escolhida.

      '''
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_novo_restaurante()
                        print('Adicionar restaurante')
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado_restaurante()
                  case 4:
                        print('Finalizar app')
                  case _:
                        opcao_invalida()
      except:
            print(' Opção Inválida')

def finalizar_app():
    ''' Exibe mensagem de finalização do app'''
    exibir_subtitulos('Finalizando app...')

def main():
    ''' Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()