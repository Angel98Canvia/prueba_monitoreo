from sqlalchemy import create_engine, MetaData

db_uri = 'mssql+pyodbc://usradm@srvdbmonitoreo:$yp%9mQ4pV3knSqAWR@srvdbmonitoreo.database.windows.net/dbmastermonitor?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(db_uri, echo=True)
query = '''
    SELECT schema_name
    FROM information_schema.schemata
    WHERE schema_name NOT LIKE 'db_%' AND schema_name NOT IN ('guest', 'sys', 'INFORMATION_SCHEMA')
'''

result = engine.execute(query)

schemas = ["dbo"]
print(schemas)


from sqlacodegen.codegen import CodeGenerator
from pathlib import Path

for schema in schemas:
    db_uri = 'mssql+pyodbc://usradm@srvdbmonitoreo:$yp%9mQ4pV3knSqAWR@srvdbmonitoreo.database.windows.net/dbmastermonitor?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(db_uri)
    metadata = MetaData(bind=engine, schema=schema)
    metadata.reflect()
    models = CodeGenerator(metadata, noindexes=True).render()
    with open(f'model_{schema}.py', 'w') as f:
        f.write(models)


