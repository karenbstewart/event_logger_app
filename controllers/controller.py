from flask import render_template, request
from app import app
from models.events_list import events, add_new_event
from models.event import Event


@app.route('/event-list')
def index():
    return render_template('index.html',title="Home", events=events )

@app.route('/event-list', methods=['POST'])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_num_of_guests = request.form["num_of_guests"]
    event_room_location = request.form["room_location"]
    event_description = request.form["description"]
    if "recurring" in request.form:
        event_recurring = True
    else:
        event_recurring = False

    # event_recurring = request.form["recurring"]
    # print(event_recurring)
    new_event = Event(event_date, event_name, event_num_of_guests, event_room_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template("index.html", title="Home", events=events)



    # print(request.form)
    # return "Done"
