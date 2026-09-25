import funcoes
                
#Status sistema
sistema = "on"

#Loop de Registro
while (sistema != "off"):
    print("""
    ---------| Menu Principal |---------
    | 1 - Adicionar Paciente           |
    | 2 - Verificar Pacientes          |
    | 3 - Consultar Paciente           |
    | 4 - Análise de informações       |
    | 5 - Finalizar Programa           |
    ------------------------------------
    """) 
    painel = int(input("Selecione um número: "))
    match painel:
        case 1:
            funcoes.adicionarPaciente()
        case 2:
            funcoes.verificarPaciente()
        case 3:
            funcoes.consultarPaciente()
        case 4:
            funcoes.analiseInformacoes()
        case 5:
            sistema = "off"
        case _:
            print("Opção inválida!!")