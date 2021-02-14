from flask import render_template, request, redirect, json
from app import app
from app.mongo import MongoAPI

data = {
        "url": "YOUR_URL_MONGODB",
        "database": "YOUR DATABASE",
        "collection": "YOUR COLLECTION",
    }




@app.route('/')
@app.route('/index')
def index():

    entries = MongoAPI(data).read()
    return render_template('index.html',
                           entries=entries)


@app.route('/add', methods=['POST'])
def add():
    form = request.form
    fn = form.get('First_Name')
    ln = form.get('Last_Name')
    age = form.get('Age')

    if fn and ln and age:
        person = {'First_Name': fn,
                  'Last_Name': ln,
                  'Age': age}
        MongoAPI(data).insertOne(person)

    entries = MongoAPI(data).read()
    return render_template('index.html', entries=entries)


@app.route('/action/<updel>/<person>', methods=['GET'])
def get_person(updel=None, person=None):
    entries = MongoAPI(data).readOne(str(person))
    if str(updel) == 'update':
        return render_template('update.html', entries=entries)
    elif str(updel) == 'delete':
        return render_template('delete.html', entries=entries)
    else:
        entries = MongoAPI(data).read()
        return render_template('index.html', entries=entries)


@app.route('/save', methods=['POST'])
def save():
    form = request.form
    fn = form.get('First_Name')
    ln = form.get('Last_Name')
    age = form.get('Age')
    oid = form.get('oid')

    if fn and ln and age and oid:
        person = {'First_Name': fn,
                  'Last_Name': ln,
                  'Age': age}
        MongoAPI(data).updateOne(oid, person)
    entries = MongoAPI(data).read()
    return render_template('index.html', entries=entries)


@app.route('/delete', methods=['POST'])
def delete():
    form = request.form
    oid = form.get('oid')
    if oid:
        MongoAPI(data).deleteOne(oid)
    entries = MongoAPI(data).read()
    return render_template('index.html', entries=entries)