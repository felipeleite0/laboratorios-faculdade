class Aluno:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.notas: list[float] = []

    def adicionar_nota(self, nota: float) -> None:
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("A nota deve estar entre 0 e 10.")

    def calcular_media(self) -> float:
        """Calcula a media das notas cadastradas."""
        return sum(self.notas) / len(self.notas) if self.notas else 0.0

    def situacao(self) -> str:
        """Retorna a situacao de aprovacao do aluno."""
        return "Aprovado" if self.calcular_media() >= 7.0 else "Reprovado"


aluno1 = Aluno("Fulano", 20)
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(9)
aluno1.adicionar_nota(10)

print(
    f"{aluno1.nome}: media {aluno1.calcular_media():.1f} "
    f"- {aluno1.situacao()}"
)

aluno2 = Aluno("Beltrano", 40)
aluno2.adicionar_nota(0)
aluno2.adicionar_nota(1)
aluno2.adicionar_nota(0.5)

print(
    f"{aluno2.nome}: media {aluno2.calcular_media():.1f} "
    f"- {aluno2.situacao()}"
)

