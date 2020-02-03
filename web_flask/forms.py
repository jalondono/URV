#!/usr/bin/python3
from wtforms import Form, StringField, TextField, SelectField

""" Class to manage de forms"""


class CommentForms(Form):
    """ create the attributes """
    place = SelectField(
        'place',
        choices=[('Amazonas', 'Amazonas'), ('Antioquia', 'Antioquia'), ('Arauca', 'Arauca'),
                 ('Atlántico', 'Atlántico'), ('Bolívar', 'Bolívar'), ('Boyacá', 'Boyacá'),
                 ('Caldas', 'Caldas'), ('Caquetá', 'Caquetá'), ('Casanare', 'Casanare'),
                 ('Cauca', 'Cauca'), ('Cesar', 'Cesar'), ('Chocó', 'Chocó'),
                 ('Córdoba', 'Córdoba'), ('Cundinamarca', 'Cundinamarca'), ('Guainía', 'Guainía'),
                 ('Guaviare', 'Guaviare'), ('Huila', 'Huila'), ('La Guajira', 'La Guajira'),
                 ('Magdalena', 'Magdalena'), ('Meta', 'Meta'), ('Nariño', 'Nariño'),
                 ('Norte de Santander', 'Norte de Santander'), ('Putumayo', 'Putumayo'), ('Quindío', 'Quindío'),
                 ('Tolima', 'Tolima'), ('Valle del Cauca', 'Valle del Cauca'), ('Vaupés', 'Vaupés'),
                 ('Vichada', 'Vichada')]
    )

    """place = StringField('place')"""
    victims = StringField('victims')
