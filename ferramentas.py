ferramentas = []
menu = -1 
while (menu != 0 ):
    menu = int(input("""=== OFICINA — FERRAMENTAS ===
1 - Adicionar ferramenta
2 - Visualizar ferramentas
3 - Ver quantidade de ferramentas
4 - Verificar se uma ferramenta está cadastrada
5 - Remover ferramenta
0 - Sair 
Digite a opção desejada: """))
    
    match menu:
        case 1:
            nova_ferramenta = input("Qual ferramenta adcionar? ").lower().strip().title()
            if nova_ferramenta in ferramentas:
                print(f"A ferramenta {nova_ferramenta} já foi adicionada ! ")
            else:
                ferramentas.append(nova_ferramenta)
                print(f"A ferramenta {nova_ferramenta} foi adicionada com sucesso ! ")
                
        case 2:
            if len(ferramentas) == 0:
                print("Não há ferramentas cadastradas")
            else:
                print(f"Ferramentas cadastradas {ferramentas}")
            
        case 3:
            print(f"O controle possui {len(ferramentas)} ferramentas cadastradas.")
        
        case 4:
            encontrar_ferramenta = input("Qual ferramenta deseja procurar ? ").lower().strip().title()
            if encontrar_ferramenta not in ferramentas:
                print(f"Ferramenta {encontrar_ferramenta} não foi cadastrada.")
            else:
                print(f"A ferramenta: {encontrar_ferramenta} já foi cadastrada.")
                
        case 5:
            excluir_ferramenta = input("Qual ferramenta você deseja remover ?").lower().strip().title()
            if excluir_ferramenta in ferramentas:
                ferramentas.remove(excluir_ferramenta)
                print(f"A {excluir_ferramenta} foi removida com sucesso !")
            else:
                print(f"A ferramenta {excluir_ferramenta} não foi cadastrada.")
                
        case 0:
            print("Programa encerrado..")
            
        case _:
            print("Opção inválida !!")