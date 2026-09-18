class Cachorro:
    """Representa um cachorro."""

    pass


rex = Cachorro()
bob = Cachorro()

print("Tipo de rex:", type(rex))
print("Objeto rex:", rex)
print("Tipo de bob:", type(bob))
print("Objeto bob:", bob)
print("Rex e Bob sao o mesmo objeto?", rex is bob)

