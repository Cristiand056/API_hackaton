from sqlalchemy import Float, MetaData, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine, Base

class RiesgosSeguridad(Base):
    __tablename__ = "riesgos_seguridad"

    referencia = Column(Integer, primary_key=True, index=True)
    proceso = Column(String(255))
    objetivo = Column(String(255))
    alcance = Column(String(255))
    descripcion_riesgo = Column(String(255))
    descripcion_activos = Column(String(255))
    tipo_activos = Column(String(255))
    impacto = Column(String(255))
    amenaza = Column(String(255))
    vulnerabilidad = Column(String(255))
    clasificacion_riesgo = Column(String(255))
    tipo_riesgo_digital = Column(String(255))
    frecuencia_actividad = Column(String(255))
    probabilidad_inherente = Column(Float)
    porcentaje_inherente = Column(Float)
    criterios_impacto = Column(String(255))
    observacion_criterio = Column(String(255))
    impacto_inherente = Column(Float)
    porcentaje_2do_inherente = Column(Float)
    zona_riesgo_inherente = Column(String(255))
    no_control = Column(String(255))
    descripcion_control = Column(String(255))
    afectacion_control = Column(String(255))
    tiene_responsable_asignado = Column(String(255))
    autoridad_responsable = Column(String(255))
    fuente_informacion = Column(String(255))
    observaciones_resueltas = Column(String(255))
    tipo_atributos = Column(String(255))
    implementacion_atributos = Column(String(255))
    calificacion_atributos = Column(String(255))
    documentacion_atributos = Column(String(255))
    frecuencia_atributos = Column(String(255))
    evidencia_atributos = Column(String(255))
    probabilidad_residual = Column(Float)
    probabilidad_residual_final = Column(Float)
    porcentaje_residual = Column(Float)
    impacto_residual_final = Column(Float)
    porcentaje_2do_residual = Column(Float)
    zona_riesgo_final = Column(String(255))
    tratamiento_riesgo = Column(String(255))
    accion_plan_manejo_riesgos = Column(String(255))
    responsable_plan_manejo_riesgos = Column(String(255))
    fecha_programada_plan_manejo_riesgos = Column(Date)
    fecha_seguimiento_1 = Column(Date)
    seguimiento_primer_trimestre = Column(String(255))
    fecha_seguimiento_2 = Column(Date)
    seguimiento_segundo_trimestre = Column(String(255))
    fecha_seguimiento_3 = Column(Date)
    seguimiento_tercer_trimestre = Column(String(255))
    fecha_seguimiento_4 = Column(Date)
    seguimiento_cuarto_trimestre = Column(String(255))
    estado_plan_manejo_riesgos = Column(String(255))
    fecha_seguimiento_controles_1 = Column(Date)
    seguimiento_controles_1 = Column(String(255))
    responsable_controles_1 = Column(String(255))
    evidencia_controles_1 = Column(String(255))
    efectividad_controles_1 = Column(String(255))
    fecha_seguimiento_controles_2 = Column(Date)
    seguimiento_controles_2 = Column(String(255))
    responsable_controles_2 = Column(String(255))
    evidencia_controles_2 = Column(String(255))
    efectividad_controles_2 = Column(String(255))
    fecha_seguimiento_controles_3 = Column(Date)
    seguimiento_controles_3 = Column(String(255))
    responsable_controles_3 = Column(String(255))
    evidencia_controles_3 = Column(String(255))
    efectividad_controles_3 = Column(String(255))
    fecha_seguimiento_controles_4 = Column(Date)
    seguimiento_controles_4 = Column(String(255))
    responsable_controles_4 = Column(String(255))
    evidencia_controles_4 = Column(String(255))
    efectividad_controles_4 = Column(String(255))
    fecha_materializacion_riesgo = Column(Date)
    actividades_materializacion_riesgo = Column(String(255))
    causa_materializacion_riesgo = Column(String(255))
    seguimiento_plan_contingencia = Column(String(255))
    fecha_seguimiento_segunda_linea = Column(Date)
    seguimiento_control_soportes_segunda_linea = Column(String(255))
    seguimiento_plan_manejo_segunda_linea = Column(String(255))
    fecha_evaluacion_tercera_linea = Column(Date)
    evaluacion_control_tercera_linea = Column(String(255))
    efectividad_control_tercera_linea = Column(String(255))
    evaluacion_plan_manejo_riesgos_tercera_linea = Column(String(255))



Base.metadata.create_all(bind=engine)