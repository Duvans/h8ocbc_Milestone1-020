from enum import unique
from os import name
from flask_marshmallow import sqla

from sqlalchemy.orm import backref
from config import db, ma
from marshmallow import fields

class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    gender = db.Column(db.Integer, nullable = False)
    uid = db.Column(db.Integer, unique = True)
    department = db.Column(db.String)
    movies = db.relationship(
        'Movie',
        backref='directors',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key = True)
    original_title = db.Column(db.String)
    budget = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    release_date = db.Column(db.String)
    revenue = db.Column(db.Integer)
    title = db.Column(db.String)
    vote_average = db.Column(db.REAL)
    vote_count = db.Column(db.Integer)
    overview = db.Column(db.String)
    tagline = db.Column(db.String)
    uid = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id')) 

class DirectorSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Director
        sqla_session = db.session
        load_instance = True

    movies = fields.Nested('DirectorMovieSchema', default=[], many=True)

class DirectorMovieSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    original_title = fields.Str()
    budget = fields.Int()
    popularity = fields.Int()
    release_date = fields.Str()
    revenue = fields.Int()
    title = fields.Str()
    vote_average = fields.Float()
    vote_count = fields.Int()
    overview = fields.Str()
    tagline = fields.Str()
    uid = fields.Int()
    director_id = fields.Int()

class MovieSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movie
        sqla_session = db.session
        load_instance = True

    directors = fields.Nested("MovieDirectorSchema", default=None)

class MovieDirectorSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursionn issue
    """ 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    name = fields.Str()
    gender = fields.Int()
    uid = fields.Int()
    department = fields.Str()
    movies = fields.Str()