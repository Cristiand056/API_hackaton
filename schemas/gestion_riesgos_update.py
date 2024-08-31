from pydantic import BaseModel
from datetime import date

class GestionRiesgosSchemaUpdate(BaseModel):
    proceso: str | None = None
    objetivo: str | None = None
    alcance: str | None = None
    impacto: str | None = None
    causa: str | None = None
    descripcion_oportunidad: str | None = None
    accion: str | None = None
    responsable: str | None = None
    fecha_programada: date | None = None
    fecha_seguimiento_primert: date | None = None
    seguimiento_primer_trimestre: str | None = None
    fecha_seguimiento_segundot: date | None = None
    seguimiento_segundo_trimestre: str | None = None
    fecha_seguimiento_tecerc: date | None = None
    seguimiento_tercer_trimestre: str | None = None
    fecha_seguimiento_cuartot: date | None = None
    seguimiento_cuarto_trimestre: str | None = None
    estado: str | None = None
    fecha_seguimiento_cys: date | None = None
    seguimiento_controly_sportes: str | None = None
    seguimiento_plan_manejo_oportunidades_y_soportes: str | None = None
    fecha_seguimiento_plan_manejo: date | None = None
    seguimento_plan_manejo_oportunidades: str | None = None
    estado_final: str | None = None