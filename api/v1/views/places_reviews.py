#!/usr/bin/python3
"""
Creates a new view for objects for all default API actions
"""
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


def getreview(review):
    """Get object"""
    return (review.to_dict(), 200)


def putreview(review):
    """Update object"""
    if not request.is_json:
        abort(400, "Not a JSON")
    new = request.get_json()
    for (k, v) in new.items():
        if k != 'id' and \
                k != 'created_at' and \
                k != 'updated_at' and \
                k != 'user_id' and \
                k != 'place_id':
            setattr(review, k, v)
    storage.save()
    return (review.to_dict(), 200)


def deletereview(review):
    """Delete object"""
    storage.delete(review)
    storage.save()
    return ({}, 200)


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def reviews(place_id):
    """Retrieves list of all objects"""
    place = None
    for c in storage.all('Place').values():
        if c.id == place_id:
            place = c
    if place is None:
        abort(404)
    if request.method == 'GET':
        all_reviews = []
        for x in storage.all('Review').values():
            if x.place_id == place_id:
                all_reviews.append(x.to_dict())
        return (jsonify(all_reviews), 200)
    elif request.method == 'POST':
        if not request.is_json:
            abort(400, "Not a JSON")
        new = request.get_json()
        if 'name' not in new.keys():
            return ({"error": "Missing name"}, 400)
        if 'user_id' not in new.keys():
            return ({"error": "Missing user_id"}, 400)
        user_id = new['user_id']
        y = [x.id for x in storage.all('User').values()]
        if user_id not in y:
            abort(404)
        if 'text' not in new.keys():
            return ({"error": "Missing text"}, 400)
        x = Review()
        for (k, v) in new.items():
            setattr(x, k, v)
        setattr(x, 'place_id', place_id)
        x.save()
        return (x.to_dict(), 201)


@app_views.route('/reviews/<ident>', methods=['GET', 'PUT', 'DELETE'])
def reviews_id(ident):
    """Retrieves a specific object"""
    reviews = storage.all("Review").values()
    for p in reviews:
        if p.id == ident:
            if request.method == 'GET':
                return getreview(p)
            elif request.method == 'PUT':
                return putreview(p)
            elif request.method == 'DELETE':
                return deletereview(p)
    abort(404, 'Not found')
