from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine

riegosgestion = Table("riegos-gestion", meta, 
                      Column("referencia", Integer, primary_key=True),
                      Column("proceso", String(255)),
                      Column("objetivo", String(255)),
                      Column("alcance", String(255)),
                      Column("impacto", String(255)),
                      Column("causa", String(255)),
                      Column("descripcionOportunidad", String(255)),
                      Column("accion", String(255)),
                      Column("responsable", String(255)),
                      Column("fechaSeguimiento", Date),
                      Column("seguimientoPrimerTrimestre", String(255)),
                      Column("fechaSeguimiento", Date),
                      Column("seguimientoSegundoTrimestre", String(255)),
                      Column("fechaSeguimiento", Date),
                      Column("seguimientoTercerTrimestre", String(255)),
                      Column("fechaSeguimiento", Date),
                      Column("seguimientoCuartoTrimestre", String(255)),
                      Column("Estado", String(255)),
                      Column("fechaSeguimiento", Date),
                      Column("SeguimientoControlySportes", String(255)),
                      Column("SeguimientoPlanManejoOportunidadesySoportes", String(255)),
                      Column("fechaSeguimiento", Date),
                      Column("SeguimentoPlanManejoOportunidades", String(255)),
                      Column("Estado", String(255))
                      )

meta.create_all(engine)