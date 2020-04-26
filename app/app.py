import calendar
from datetime import date
import mysql.connector
from flask import Flask, render_template

mydb = mysql.connector.connect(
    host='db',
    user='root',
    password='maartinsh123',
    database='elektrum',
    port='3306'
)

app = Flask(__name__)

my_cursor = mydb.cursor()

#################### VARIABLES BLOCK  #####################

my_date = date.today()
date = date.today().strftime("%d-%m-%Y")
day = calendar.day_name[my_date.weekday()]

select_queries = {
    '1_uzdevums': "SELECT * FROM METER_A WHERE STATUS = 3 AND TML_ID IS NULL;",
    '2_uzdevums': "SELECT METER_ID, KWH_IMPORT+KWH_EXPORT as HOURS FROM DATA_E WHERE DATA_TIME = '2020-04-16'",
    '3_uzdevums': "SELECT * FROM PROFILI",
    '4_uzdevums': "SELECT * FROM PROFILI_4_DIENAS;",
    '5_uzdevums': "SELECT * FROM PROFILI_4_DIENAS_MSNO;"
}


####################### FLASK ROUTES #######################

@app.route('/')
@app.route('/1_uzdevums')
def _1_uzdevums():
    my_cursor.execute(select_queries.get('1_uzdevums'))
    results = my_cursor.fetchall()
    return render_template('1_uzdevums.html', results=results)


@app.route('/2_uzdevums')
def _2_uzdevums():
    my_cursor.execute(select_queries.get('2_uzdevums'))
    results = my_cursor.fetchall()
    return render_template('2_uzdevums.html', results=results)


@app.route('/3_uzdevums')
def _3_uzdevums():
    my_cursor.execute(select_queries.get('3_uzdevums'))
    results = my_cursor.fetchall()
    return render_template('3_uzdevums.html', results=results)


@app.route('/4_uzdevums')
def _4_uzdevums():
    my_cursor.execute(select_queries.get('4_uzdevums'))
    results = my_cursor.fetchall()
    return render_template('4_uzdevums.html', results=results)


@app.route('/5_uzdevums')
def _5_uzdevums():
    my_cursor.execute(select_queries.get('5_uzdevums'))
    results = my_cursor.fetchall()
    return render_template('5_uzdevums.html', results=results)


####################### FLASK CONFIG #######################

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
