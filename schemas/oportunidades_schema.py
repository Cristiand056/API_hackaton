from pydantic import BaseModel
from datetime import date
from typing import Optional

class OportunidadSchema(BaseModel):
    referencia_identificacion: int | None = None
    proceso_identificacion: str
    objetivo_identificacion: str
    alcance_identificacion: str
    impacto_identificacion: str
    causa_identificacion: str
    descripcion_oportunidad_identificacion: str
    accion_plan_manejo: str
    responsable_plan_manejo: str
    fecha_programada_plan_manejo: str
    fecha_seguimiento_1_plan_manejo: str
    seguimiento_primer_trimestre_plan_manejo: str
    fecha_seguimiento_2_plan_manejo: str
    seguimiento_segundo_trimestre_plan_manejo: str
    fecha_seguimiento_3_plan_manejo: str
    seguimiento_tercer_trimestre_plan_manejo: str
    fecha_seguimiento_4_plan_manejo: str
    seguimiento_cuarto_trimestre_plan_manejo: str
    estado_plan_manejo: str
    fecha_seguimiento_2da_linea_defensa: str
    seguimiento_control_soportes_2da_linea_defensa: str
    seguimiento_plan_manejo_soportes_2da_linea_defensa: str
    fecha_seguimiento_3ra_linea_defensa: str
    seguimiento_plan_manejo_3ra_linea_defensa: str
    estado_seguimiento_3ra_linea_defensa: str
