#!/usr/bin/python3
"""flask app - handle the the routes to HTTP request"""
from flask import Flask, render_template, request
from web_flask.forms import CommentForms
from models.disaster import Disaster
from models import storage
from models.word_to_number import word_to_number


""" Application """
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """Return not found when doesn't exist the route"""
    return "Not Found"


@app.route("/", methods=['POST', 'GET'])
def index():
    """Handle the HTTP method, either POST or GET"""
    comment_form = CommentForms(request.form)
    total = 0
    if request.method == 'GET':
        storage.reload()
        data = storage.all()
        for item in data.values():
            total = int(item.victims) + total
        return render_template("index.html", title='test', form=comment_form, reports=data, total=total)
    if request.method == 'POST':
        find_obj = storage.get(comment_form.place.data)
        victims_int = word_to_number(comment_form.victims.data)
        if find_obj is None:
            if victims_int != 0:
                event = Disaster(place=comment_form.place.data, victims=victims_int)
                storage.new(event)
                storage.save()
        else:
            storage.reload()
            data = storage.all()
            obj_to_change = data["Disaster." + find_obj]
            if victims_int == 0:
                obj_to_change.delete()
            else:
                obj_to_change.victims = victims_int
                storage.save()
    return render_template("index.html", title='test', form=comment_form, reports={}, total=0)


if __name__ == "__main__":
    app.run(debug=False)
