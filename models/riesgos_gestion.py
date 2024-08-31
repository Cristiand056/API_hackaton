from sqlalchemy import MetaData, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine, Base

class GestionRiesgos(Base):
    __tablename__ = "riesgos_gestion"
    referencia = Column(Integer, primary_key=True, autoincrement=True)
    proceso = Column(String(255))
    objetivo = Column(String(255))
    alcance = Column(String(255))
    impacto = Column(String(255))
    causa = Column(String(255))
    descripcion_oportunidad = Column(String(255))
    accion = Column(String(255))
    responsable = Column(String(255))
    fecha_programada = Column(Date)
    fecha_seguimiento_primert = Column(Date)
    seguimiento_primer_trimestre = Column(String(255))
    fecha_seguimiento_segundot = Column(Date)
    seguimiento_segundo_trimestre = Column(String(255))
    fecha_seguimiento_tecerc = Column(Date)
    seguimiento_tercer_trimestre = Column(String(255))
    fecha_seguimiento_cuartot = Column(Date)
    seguimiento_cuarto_trimestre = Column(String(255))
    estado = Column(String(255))
    fecha_seguimiento_cys = Column(Date)
    seguimiento_controly_sportes = Column(String(255))
    seguimiento_plan_manejo_oportunidades_y_soportes = Column(String(255))
    fecha_seguimiento_plan_manejo = Column(Date)
    seguimento_plan_manejo_oportunidades = Column(String(255))
    estado_final = Column(String(255))

Base.metadata.create_all(bind=engine)

"""meta = MetaData()
riegosgestion = Table(
    "riegos_gestion", meta,
    Column("referencia", Integer, primary_key=True, autoincrement=True),
    Column("proceso", String(255)),
    Column("objetivo", String(255)),
    Column("alcance", String(255)),
    Column("impacto", String(255)),
    Column("causa", String(255)),
    Column("descripcion_oportunidad", String(255)),
    Column("accion", String(255)),
    Column("responsable", String(255)),
    Column("fecha_seguimiento_primert", Date),
    Column("seguimiento_primer_trimestre", String(255)),
    Column("fecha_seguimiento_segundot", Date),
    Column("seguimiento_segundo_trimestre", String(255)),
    Column("fecha_seguimiento_tecerc", Date),
    Column("seguimiento_tercer_trimestre", String(255)),
    Column("fecha_seguimiento_cuartot", Date),
    Column("seguimiento_cuarto_trimestre", String(255)),
    Column("estado", String(255)),
    Column("fecha_seguimiento_cys", Date),
    Column("seguimiento_controly_sportes", String(255)),
    Column("seguimiento_plan_manejo_oportunidades_y_soportes", String(255)),
    Column("fecha_seguimiento_plan_manejo", Date),
    Column("seguimento_plan_manejo_oportunidades", String(255)),
    Column("estado_final", String(255))
)
meta.create_all(engine)"""