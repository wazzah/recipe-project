import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    task = mongo.db.tasks
    task.insert
    tasks.insert_one(request.form.to_dict)
    return redirect(url_for('gets_tasks'))





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)