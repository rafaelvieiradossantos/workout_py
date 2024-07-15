from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome da centro', examples='CT Pelé', max_lenght=20)]
    endereco: Annotated[str, Field(description='Endereço do CT', examples='Rua Y,01I', max_lenght=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario', examples='Jose', max_lenght=30)]