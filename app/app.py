from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


def read_sql_file(filename):
    with open(filename, 'r') as file:
        sql_commands = file.read()
        
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bogda765",
        database="booking"
    )
    cursor = db.cursor()

    for command in sql_commands.split(';'):
        try:
            if command.strip() != '':
                cursor.execute(command)
        except Exception as e:
            print(f"Command skipped: {str(e)}")
    db.commit()
    cursor.close()
    db.close()


read_sql_file('data.sql')

if __name__ == '__main__':
    app.run()
