class Registradores:

    def __init__(self, A=0, B=0, C=0, D=0):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def __str__(self):
        return f"A={self.A}, B={self.B}, C={self.C}, D={self.D}"


def executar_programa(instrucoes, registradores):
    pc = 1  # Contador de programa (PC)
    while pc <= len(instrucoes):
        instrucao = instrucoes[pc - 1].strip()  # Acessa a instrução atual
        partes = instrucao.split()
        rotulo, operacao = partes[0], partes[1]

        # Extrai os argumentos da instrução
        args = partes[2:]
        if len(args) == 1:
            destino = int(args[0])
        elif len(args) == 2:
            registro, destino = args
            destino = int(destino)
        else:
            registro = args[0]
            destino = int(args[1])

        # Exibe o estado atual dos registradores
        print(f"({registradores}), {rotulo}) {operacao} {' '.join(args)}")

        # Executa a operação da instrução
        if operacao == 'ADDC':
            setattr(registradores, registro,
                    getattr(registradores, registro) + destino)
        elif operacao == 'SUB':
            setattr(registradores, registro,
                    getattr(registradores, registro) - destino)
        elif operacao == 'ZER':
            if getattr(registradores, registro) == 0:
                pc = destino
                continue
        pc += 1


def main():
    # Inicializa os registradores
    registradores = Registradores(A=2, B=3, C=0, D=0)

    # Lê as instruções do arquivo de entrada
    with open('instrucoes.txt', 'r') as file:
        instrucoes = file.readlines()

    # Executa o programa
    print("Valor corrente dos registradores:", registradores)
    executar_programa(instrucoes, registradores)


if __name__ == "__main__":
    main()
