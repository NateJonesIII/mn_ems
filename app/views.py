# app/views.py
from flask import request, jsonify
from app import app, db
from app.models import User, Event, RSVP

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    user = User.query.get(data['user_id'])
    if user:
        new_event = Event(title=data['title'], description=data.get('description'), date=data['date'], user_id=data['user_id'])
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully'}), 201
    return jsonify({'message': 'User not found'}), 404

@app.route('/events/<int:event_id>/rsvp', methods=['POST'])
def rsvp_event(event_id):
    data = request.get_json()
    user = User.query.get(data['user_id'])
    event = Event.query.get(event_id)
    if user and event:
        rsvp = RSVP(user_id=data['user_id'], event_id=event_id, status=data['status'])
        db.session.add(rsvp)
        db.session.commit()
        return jsonify({'message': 'RSVP created successfully'}), 201
    return jsonify({'message': 'User or Event not found'}), 404
