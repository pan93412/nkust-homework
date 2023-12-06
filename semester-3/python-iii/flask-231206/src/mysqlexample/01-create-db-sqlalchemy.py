import os
from sqlalchemy import String, create_engine, select, text, func

# Create a connection to the database
engine = create_engine(f'mysql+mysqlconnector://root:{os.environ["MYSQL_PASSWORD"]}@localhost')

with engine.connect() as connection:
    # Get the current version of the MySQL server
    result = connection.execute(select(func.version(type_=String())))
    print(result.first())

    # Create a database if not exist.
    connection.execute(text("CREATE DATABASE IF NOT EXISTS example_sa DEFAULT CHARSET utf8 COLLATE utf8_general_ci"))
    connection.commit()
