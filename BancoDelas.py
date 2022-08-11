class Cliente:
    def __init__(self, nome, telefone, renda_mensal, sexo):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
        self.sexo = sexo

    def __str__(self) -> str:
        return f'Cliente: {self.nome}, telefone: {self.telefone}, renda mensal: {self.renda_mensal}, sexo: {self.sexo}'


class ContaCorrente(Cliente):
    def __init__(self, nome, telefone, renda_mensal, sexo):
        super().__init__(nome, telefone, renda_mensal, sexo)
        self.saldo = 0
        self.limite = self.renda_mensal
    
    def saque(self, valorSaque):
        if self.sexo == "F" or "f":
            if self.saldo >= valorSaque:
                if valorSaque <= self.limite: 
                    self.saldo -= valorSaque
                    print(f'Sr(a) {self.nome}, o seu saque foi de R$ {valorSaque}, seu saldo atual é de {self.saldo}')
        elif self.sexo == "M" or "m":
            if self.saldo >= valorSaque:
                print("Cliente não possui conta especial")
            else: 
                print(f'Sr(a) {self.nome}, o seu saque foi de R$ {valorSaque}, seu saldo atual é de {self.saldo}') 
        else: 
            print("Operação Inválida")

    def deposito(self, valorDeposito):
        self.saldo += valorDeposito
        print(f'Sr(a) {self.nome}, o seu deposito foi de R$ {valorDeposito}, seu saldo atual é de {self.saldo}')

    def __str__(self) -> str:
        return f'Cliente: {self.nome}, telefone: {self.telefone}, renda mensal: {self.renda_mensal}, sexo: {self.sexo}, saldo {self.saldo}'
