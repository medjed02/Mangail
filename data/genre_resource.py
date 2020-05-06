from flask_restful import abort, Resource
from data import db_session
from data.genres import Genre
from flask import jsonify


def abort_if_genre_not_found(genre_id):
    session = db_session.create_session()
    genre = session.query(Genre).get(genre_id)
    if not genre:
        abort(404, message=f"Genre {genre_id} not found")


def abort_if_genre_found(genre_id):
    session = db_session.create_session()
    genre = session.query(Genre).get(genre_id)
    if genre:
        abort(404, message=f"Genre {genre_id} already exists")


class GenresResource(Resource):
    def get(self, genre_id):
        abort_if_genre_not_found(genre_id)
        session = db_session.create_session()
        genre = session.query(Genre).get(genre_id)
        return jsonify(
            {
                "genre": genre.to_dict()
            }
        )


class GenresListResource(Resource):
    def get(self):
        session = db_session.create_session()
        genres = session.query(Genre).all()
        return jsonify(
            {
                'genres': [item.to_dict() for item in genres]
            }
        )