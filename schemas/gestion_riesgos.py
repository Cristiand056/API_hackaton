from typing import Optional
from pydantic import BaseModel
from datetime import date

class GestionRiegos(BaseModel):
    referencia: Optional[str]
    proceso: str
    objetivo: str
    alcance: str
    impacto: str
    causa: str
    descripcionOportunidad: str
    accion: str
    responsable: str
    fechaSeguimientoPrimerT: date
    seguimientoPrimerTrimestre: str
    fechaSeguimientoSegundoT: date
    seguimientoSegundoTrimestre: str
    fechaSeguimientoTecerT: date
    seguimientoTercerTrimestre: str
    fechaSeguimientoCuartoT: date
    seguimientoCuartoTrimestre: str
    Estado: str
    fechaSeguimientoCyS: date
    SeguimientoControlySportes: str
    SeguimientoPlanManejoOportunidadesySoportes: str
    fechaSeguimientoPlanManejo: date
    SeguimentoPlanManejoOportunidades: str
    EstadoFinal: str