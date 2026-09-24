import funcoes
                
#Status sistema
sistema = "on"

#Loop de Registro
while (sistema != "off"):
    print(""""
    -------------| Painel |-------------
    | 1 - Criar Planilha               |
    | 2 - Adicionar Paciente           |
    | 3 - Verificar Pacientes          |
    | 4 - Consultar Paciente           |
    | 5 - Finalizar Programa           |
    ------------------------------------
    """) 
    painel = int(input())
    match painel:
        case 1:
            funcoes.criacaoPlanilha()
        case 2:
            funcoes.adicionarPaciente()
        case 3:
            funcoes.verificarPaciente()
        case 4:
            funcoes.consultarPaciente()
        case 5:
            sistema = "off"
        case _:
            print("Opção inválida!!")




