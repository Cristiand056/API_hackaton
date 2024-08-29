from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Sp5Qz2L077#0_4@localhost:3306/dbuaesp")

meta = MetaData()

conn = engine.connect()