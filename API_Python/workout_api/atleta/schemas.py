from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Joao', max_lenght=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='111.222.333-44', max_lenght=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=10)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=70.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.80)]
    sexo: Annotated[str, Field(description='sexo do atleta', examples='M', max_lenght=1)]
    