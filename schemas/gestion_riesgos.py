from typing import Optional
from pydantic import BaseModel
from datetime import date

class GestionRiesgosSchema(BaseModel):
    referencia:int|None=None
    proceso:str
    objetivo:str
    alcance:str
    impacto:str
    causa:str
    descripcion_oportunidad:str
    accion:str
    responsable:str
    fecha_seguimiento_primert:date
    seguimiento_primer_trimestre:str
    fecha_seguimiento_segundot:date
    seguimiento_segundo_trimestre:str
    fecha_seguimiento_tecerc:date
    seguimiento_tercer_trimestre:str
    fecha_seguimiento_cuartot:date
    seguimiento_cuarto_trimestre:str
    estado:str
    fecha_seguimiento_cys:date
    seguimiento_controly_sportes:date
    seguimiento_plan_manejo_oportunidades_y_soportes:str
    fecha_seguimiento_plan_manejo:date
    seguimento_plan_manejo_oportunidades:str
    estado_final:str
    
