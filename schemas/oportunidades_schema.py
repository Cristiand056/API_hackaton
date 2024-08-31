from pydantic import BaseModel
from datetime import date
from typing import Optional

class OportunidadSchema(BaseModel):
    referencia: int | None = None
    proceso_identificacion: str | None = None
    objetivo_identificacion: str | None = None
    alcance_identificacion: str | None = None
    impacto_identificacion: str | None = None
    causa_identificacion: str | None = None
    descripcion_oportunidad_identificacion: str | None = None
    accion_plan_manejo: str | None = None
    responsable_plan_manejo: str | None = None 
    fecha_programada_plan_manejo: str | None = None
    fecha_seguimiento_1_plan_manejo: str | None = None
    seguimiento_primer_trimestre_plan_manejo: str | None = None
    fecha_seguimiento_2_plan_manejo: str | None = None
    seguimiento_segundo_trimestre_plan_manejo: str | None = None 
    fecha_seguimiento_3_plan_manejo: str | None = None
    seguimiento_tercer_trimestre_plan_manejo: str | None = None
    fecha_seguimiento_4_plan_manejo: str | None = None
    seguimiento_cuarto_trimestre_plan_manejo: str | None = None
    estado_plan_manejo: str | None = None
    fecha_seguimiento_2da_linea_defensa: str | None = None
    seguimiento_control_soportes_2da_linea_defensa: str | None = None
    seguimiento_plan_manejo_soportes_2da_linea_defensa: str | None = None
    fecha_seguimiento_3ra_linea_defensa: str | None = None
    seguimiento_plan_manejo_3ra_linea_defensa: str | None = None
    estado_seguimiento_3ra_linea_defensa: str | None = None
