from sqlalchemy import Float, MetaData, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine, Base


class Oportunidad(Base):
    __tablename__ = 'oportunidades'

    referencia = Column(Integer, primary_key=True, autoincrement=True)
    proceso_identificacion = Column(String(255))
    objetivo_identificacion = Column(String(255))
    alcance_identificacion = Column(String(255))
    impacto_identificacion = Column(String(255))
    causa_identificacion = Column(String(255))
    descripcion_oportunidad_identificacion = Column(String(255))
    accion_plan_manejo = Column(String(255))
    responsable_plan_manejo = Column(String(255))
    fecha_programada_plan_manejo = Column(String(255))
    fecha_seguimiento_1_plan_manejo = Column(String(255))
    seguimiento_primer_trimestre_plan_manejo = Column(String(255))
    fecha_seguimiento_2_plan_manejo = Column(String(255))
    seguimiento_segundo_trimestre_plan_manejo = Column(String(255))
    fecha_seguimiento_3_plan_manejo = Column(String(255))
    seguimiento_tercer_trimestre_plan_manejo = Column(String(255))
    fecha_seguimiento_4_plan_manejo = Column(String(255))
    seguimiento_cuarto_trimestre_plan_manejo = Column(String(255))
    estado_plan_manejo = Column(String(255))
    fecha_seguimiento_2da_linea_defensa = Column(String(255))
    seguimiento_control_soportes_2da_linea_defensa = Column(String(255))
    seguimiento_plan_manejo_soportes_2da_linea_defensa = Column(String(255))
    fecha_seguimiento_3ra_linea_defensa = Column(String(255))
    seguimiento_plan_manejo_3ra_linea_defensa = Column(String(255))
    estado_seguimiento_3ra_linea_defensa = Column(String(255))


Base.metadata.create_all(bind=engine)