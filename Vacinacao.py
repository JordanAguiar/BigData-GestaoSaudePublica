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
    | 5 - Análise de informações       |
    | 6 - Finalizar Programa           |
    ------------------------------------
    """) 
    painel = int(input("Selecione um número: "))
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
            funcoes.analiseInformacoes()
        case 6:
            sistema = "off"
        case _:
            print("Opção inválida!!")




