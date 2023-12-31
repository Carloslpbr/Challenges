"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança) ok
    Pessoa tem nome e idade (com getters) ok
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca) ok
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta ok
    ContaCorrente deve ter um limite extra ok 
    Contas têm agência, número da conta e saldo ok
    Contas devem ter método para depósito ok
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)ok
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação) ok 
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco ok
    * Checar se o cliente é daquele banco ok
    * Checar se a conta é daquele banco ok 
Só será possível sacar se passar na autenticação do banco (descrita acima) ok
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

def compare(criteria_1, criteria_2):
    validation = False
    if criteria_1 == criteria_2:
        validation = True
    return validation 
 
class Person:
    def __init__(self, person, age):
        self.name = person
        self.age = age 

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Client(Person):
    def __init__(self, person, age):
        super().__init__(person,age)
        self.account = None
        self.bank = None

    def set_account(self, account):
        self.account = account

    def set_bank(self,bank):
        self.bank = bank


class Bank:
    def __init__(self, bank_name, bank_num) :
        self.bank_name = bank_name
        self.bank_num = bank_num

    def validation(self, account, withdraw_amount, account_balance, account_limit, client_name, client_bank, client_account, \
                   client_withdraw, bank_withdraw, bank_account_num):
        criteria_1 = False
        criteria_2 = False
        criteria_3 = False   


        criteria_1 = compare(client_name,client_withdraw)
        criteria_2 = compare(client_bank,bank_withdraw)
        criteria_3 = compare(client_account,bank_account_num)
    
        if criteria_1 and criteria_2 and criteria_3 == True:
            account.check_balance(account, withdraw_amount, account_balance,account_limit)
            return print(f"Seu saldo atual é {account.balance}")
        else:
            print("Operação inválida!")


class Account(ABC):
    def __init__(self, bank, bank_num, num):
        self.account_bank = bank
        self.account_bank_num = bank_num
        self.account_num = num
        #self.account_type = None
        self.balance = 0
    
    def set_type(self, type):
        self.account_type = type

    def deposit(self, amount):
        self.balance += amount
        print(f"Depósito de {amount} realizado, seu novo saldo é {self.balance}")
        print("")

    @abstractmethod
    def withdraw(self, balance, withdraw):
        pass
    
    @abstractmethod
    def check_balance(self, account, amount, balance, limit_w):
        pass


class Account_Normal(Account):
    def __init__(self, bank, bank_num,num):
        super().__init__(bank,bank_num, num)
        self.account_limit = 0    

    def withdraw(self, balance, withdraw):
        self.balance -= withdraw
        print(f"Saque de {withdraw} realizado, seu novo saldo é {self.balance}")
        print("")


    def check_balance(self, account, amount, balance, limit_w):
        if (balance - amount ) >= limit_w:
            account.withdraw(account, amount)
            print("Operação válida!")
        else:
            print("Operação inválida!")
            print("Saldo Insuficiente")

class Account_Special(Account):
    def __init__(self, bank, bank_num,num):
        super().__init__(bank,bank_num, num)
        self.account_limit = -50

    def withdraw(self, balance, withdraw):
        self.balance -= withdraw
        print(f"Saque de {withdraw} realizado, seu novo saldo é {self.balance}")
        print("")

    def check_balance(self, account, amount, balance, limit_w):
        if (balance - amount ) >= limit_w:
            account.withdraw(account, amount)
            print("Operação válida!")
        else:            
            print("Operação inválida.")
            print("Saque excede o limite permitido")


person_1 = Person("Carlos", 30)
bank_1 = Bank("Banco do Brasil", 1)
client_1 = Client(person_1.name,person_1.age)
account_1 = Account_Special("Banco do Brasil", 1, 481)
client_1.set_bank("Banco do Brasil")
client_1.set_account(account_1.account_num)
#account_1.set_type("Special")


client_withdraw = "Carlos"
bank_withdraw = "Banco do Brasil"
bank_account_num = 481
deposit_1 = account_1.deposit(200)
withdraw_amount = 240
account_balance = account_1.balance



bank_1.validation(account_1, withdraw_amount, account_balance, account_1.account_limit, \
                      client_1.name, client_1.bank, client_1.account, \
                      client_withdraw, bank_withdraw, bank_account_num)















