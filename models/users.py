from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

users = Table("users", meta, 
              Column("id", Integer, primary_key=True), 
              Column("name", String(255)), 
              Column("password_hashed", String(255)),
              Column("email", String(255)),
              Column("role",String(255)),
              Column("disabled", Boolean, default=False)
            )

meta.create_all(engine)
