#!/usr/bin/python3
from wtforms import Form, StringField, TextField

""" Class to manage de forms"""


class CommentForms(Form):
    """ create the attributes """
    place = StringField('place')
    victims = StringField('victims')
