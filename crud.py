"""CRUD operations."""
import datetime
from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, 
                  release_date=release_date, poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """Allow user to view all movies in movies table"""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Return movie object by movie_id """
    movie = Movie.query.get(movie_id)

    return movie


def get_users():
    """View all users in users table"""

    return User.query.all()


def create_rating(user, movie, score):
    """Create and return a rating for a movie by a user"""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
