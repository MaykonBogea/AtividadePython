"""Sistema bancário didático para demonstrar programação orientada a objetos."""

from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


def converter_valor(valor):
    """Converte um número para Decimal e rejeita valores inválidos ou não positivos."""
    try:
        resultado = Decimal(str(valor))
    except (InvalidOperation, ValueError) as erro:
        raise ValueError("O valor deve ser numérico.") from erro

    if not resultado.is_finite() or resultado <= 0:
        raise ValueError("O valor deve ser um número positivo e finito.")

    return resultado.quantize(Decimal("0.01"))


class Cliente:
    """Representa um cliente do banco."""

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError("E-mail inválido.")
        self._email = valor.strip().lower()

    def __str__(self):
        return f"{self.nome} <{self.email}>"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Cliente):
            return NotImplemented
        return self.email == outro.email


class Conta(ABC):
    """Classe abstrata que define o contrato comum das contas bancárias."""

    def __init__(self, numero, cliente, saldo_inicial=0):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("O número da conta é obrigatório.")
        if not isinstance(cliente, Cliente):
            raise TypeError("cliente deve ser uma instância de Cliente.")

        saldo = Decimal(str(saldo_inicial))
        if not saldo.is_finite() or saldo < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")

        self.numero = numero.strip()
        self.cliente = cliente
        self._saldo = saldo.quantize(Decimal("0.01"))

    @property
    def saldo(self):
        """Saldo disponível, exposto sem setter público."""
        return self._saldo

    def depositar(self, valor):
        valor = converter_valor(valor)
        self._saldo += valor

    def sacar(self, valor):
        valor = converter_valor(valor)
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento da conta, conforme seu tipo."""

    def __str__(self):
        return (
            f"{self.__class__.__name__} nº {self.numero} | "
            f"Cliente: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(numero={self.numero!r}, "
            f"cliente={self.cliente!r}, saldo_inicial={self.saldo!r})"
        )

    def __lt__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.saldo < outra.saldo


class ContaCorrente(Conta):
    """Conta corrente que cobra uma tarifa fixa por saque."""

    def __init__(self, numero, cliente, saldo_inicial=0, tarifa_saque=2.50):
        super().__init__(numero, cliente, saldo_inicial)
        self.tarifa_saque = tarifa_saque

    @property
    def tarifa_saque(self):
        return self._tarifa_saque

    @tarifa_saque.setter
    def tarifa_saque(self, valor):
        try:
            tarifa = Decimal(str(valor))
        except (InvalidOperation, ValueError) as erro:
            raise ValueError("A tarifa deve ser numérica.") from erro
        if not tarifa.is_finite() or tarifa < 0:
            raise ValueError("A tarifa não pode ser negativa.")
        self._tarifa_saque = tarifa.quantize(Decimal("0.01"))

    def sacar(self, valor):
        valor = converter_valor(valor)
        total = valor + self.tarifa_saque
        if total > self.saldo:
            raise ValueError("Saldo insuficiente para saque e tarifa.")
        self._saldo -= total

    def calcular_rendimento(self):
        """Conta corrente não rende neste exemplo."""
        return Decimal("0.00")

    def __str__(self):
        return f"{super().__str__()} | Tarifa de saque: R$ {self.tarifa_saque:.2f}"


class ContaPoupanca(Conta):
    """Conta poupança que calcula rendimento percentual mensal."""

    def __init__(self, numero, cliente, saldo_inicial=0, taxa_mensal=Decimal("0.005")):
        super().__init__(numero, cliente, saldo_inicial)
        self.taxa_mensal = taxa_mensal

    @property
    def taxa_mensal(self):
        return self._taxa_mensal

    @taxa_mensal.setter
    def taxa_mensal(self, valor):
        try:
            taxa = Decimal(str(valor))
        except (InvalidOperation, ValueError) as erro:
            raise ValueError("A taxa deve ser numérica.") from erro
        if not taxa.is_finite() or taxa < 0 or taxa > 1:
            raise ValueError("A taxa deve estar entre 0 e 1 (0% a 100%).")
        self._taxa_mensal = taxa

    def calcular_rendimento(self):
        """Retorna o rendimento mensal estimado sem alterar o saldo."""
        return (self.saldo * self.taxa_mensal).quantize(Decimal("0.01"))

    def __str__(self):
        return f"{super().__str__()} | Rendimento estimado: R$ {self.calcular_rendimento():.2f}"


class Banco:
    """Agrega clientes e contas; usa composição para organizar os objetos."""

    def __init__(self, nome, contas=None):
        self.nome = nome
        self.contas = []
        if contas is not None:
            for conta in contas:
                self.adicionar_conta(conta)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do banco não pode ser vazio.")
        self._nome = valor.strip()

    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("Só é possível adicionar objetos do tipo Conta.")
        if any(item.numero == conta.numero for item in self.contas):
            raise ValueError(f"Já existe uma conta com o número {conta.numero}.")
        self.contas.append(conta)

    def __str__(self):
        return f"Banco {self.nome}: {len(self.contas)} conta(s)"

    def __repr__(self):
        return f"Banco(nome={self.nome!r}, contas={self.contas!r})"


def demonstrar():
    """Cria mais de 10 objetos e demonstra herança, polimorfismo e exceções."""
    clientes = [
        Cliente("Ana Silva", "ana@example.com"),
        Cliente("Bruno Costa", "bruno@example.com"),
        Cliente("Carla Souza", "carla@example.com"),
        Cliente("Diego Lima", "diego@example.com"),
        Cliente("Eva Rocha", "eva@example.com"),
    ]

    contas = [
        ContaCorrente("CC-001", clientes[0], 1200, 2.50),
        ContaPoupanca("CP-001", clientes[1], 2000, "0.005"),
        ContaCorrente("CC-002", clientes[2], 500, 3.00),
        ContaPoupanca("CP-002", clientes[3], 3500, "0.006"),
        ContaCorrente("CC-003", clientes[4], 800, 2.00),
        ContaPoupanca("CP-003", clientes[0], 1500, "0.004"),
        ContaCorrente("CC-004", clientes[1], 2200, 2.50),
        ContaPoupanca("CP-004", clientes[2], 900, "0.005"),
        ContaCorrente("CC-005", clientes[3], 450, 1.50),
        ContaPoupanca("CP-005", clientes[4], 2800, "0.007"),
    ]

    banco = Banco("Banco Exemplo", contas)

    print(f"=== {banco} ===")
    print("\n--- Polimorfismo: mesmo método, resultados diferentes ---")
    for conta in banco.contas:
        print(
            f"{conta.numero}: saldo = R$ {conta.saldo:.2f}; "
            f"rendimento = R$ {conta.calcular_rendimento():.2f}"
        )

    print("\n--- Contas ordenadas por saldo (menor para maior) ---")
    for conta in sorted(banco.contas):
        print(conta)

    print("\n--- Demonstração de repr() ---")
    print(repr(clientes[0]))
    print(repr(contas[0]))

    print("\n--- Operações bancárias ---")
    banco.contas[0].depositar("100.00")
    banco.contas[0].sacar("50.00")
    print(banco.contas[0])

    print("\n--- Tratamento de entradas inválidas ---")
    testes_invalidos = [
        ("E-mail inválido", lambda: Cliente("Teste", "email-sem-arroba")),
        ("Depósito negativo", lambda: banco.contas[0].depositar(-10)),
        ("Saque acima do saldo", lambda: banco.contas[0].sacar(999999)),
        ("Tarifa negativa", lambda: ContaCorrente("CC-X", clientes[0], 100, -1)),
        ("Conta duplicada", lambda: banco.adicionar_conta(contas[0])),
    ]

    for descricao, operacao in testes_invalidos:
        try:
            operacao()
        except (ValueError, TypeError) as erro:
            print(f"{descricao}: {erro}")
        else:
            print(f"{descricao}: operação aceita.")
        finally:
            print("  Teste finalizado.")


if __name__ == "__main__":
    demonstrar()
