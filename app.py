import os 
#inserir 2 restaurantes na list
# restaurantes=['Bife Sujo', 'Saco de Feijão'] 
restaurantes=[{'nome':'Bife Sujo','categoria':'prato-feito','ativo':True},
              {'nome':'Saco de Feijão','categoria':'feijoada', 'ativo':False},
              {'nome':'Pé de Banha','categoria':'pastelaria','ativo':True},]


def mostrar_subtitulo(texto):
    os.system('cls')
    print (texto)
    print()
    
def finalizar_app():
    # os.system('cls')
    # print ('Finalizando app\n')
    mostrar_subtitulo()

def chamar_nome_do_app():
     print (''' 
            r̲e̲s̲t̲a̲u̲r̲a̲n̲t̲e̲ e̲x̲p̲r̲e̲s̲s̲o̲
    ''') 

def voltar_ao_menu_principal():
     input("\n Digite uma tecla para voltar ao menu principal: \n")
     main() 

def opcao_invalida():
    print('Opção invalida\n')
    # input('Digite uma tecla para voltar ao menu principal: ')
    # main() 
    voltar_ao_menu_principal()

def exibir_opcoes():
    print('1-Cadastrar um restaurante')
    print('2-Listar restaurantes')
    print('3-Ativar um restaurante')
    print('4-Sair do programa')

def cadastrar_novo_restaurante():
     os.system('cls')
     nome_do_restaurante=input('Digite o nome do novo restaurante: \n')
     categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
     dados_do_restaurante={'nome':nome_do_restaurante, 'categoria':categoria,'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
     voltar_ao_menu_principal()

def listar_restaurantes():
    os. system('cls')
    mostrar_subtitulo('Listando os restaurantes \n')
    #em português
    for restaurante in restaurantes:
        # print(f'-{restaurante}')
    #modificando a maneira de listar restaurante
    #para manipular o dicionário
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        ativo=restaurante ['ativo']
        print(f'-{nome_restaurante} |- {categoria} |-{ativo}')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    mostrar_subtitulo("Alternar os estados do restaurante")

    nome_restaurante=input('Digite o nome do restaurante que desejas alterar o estado: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            if not restaurante_encontrado:
             print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcoes(): 
    try:
        opcao_digitada=(int(input('Escolha uma opção: ')))
        print('Você selecionou a opção: ',opcao_digitada,'\n')
        if(opcao_digitada==1):
            print('Você escolheu cadastrar um restaurante\n')
            cadastrar_novo_restaurante()
            finalizar_app()
        elif (opcao_digitada==2):
            # print('Você escolheu listar os restaurantes do app\n')
            listar_restaurantes()
            finalizar_app()
        elif (opcao_digitada==3):
            # print('Você escolheu ativar um restaurante\n')
            alterar_estado_restaurante()
            finalizar_app()
        elif (opcao_digitada==4):
            print('Você escolheu sair do programa\n')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida() 

def main():
    os.system('cls') 

    chamar_nome_do_app() 

    exibir_opcoes() 

    escolher_opcoes() 


if(__name__=='__main__'):
    main()