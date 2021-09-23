from models.event import *

event1 = Event("02/01/23", "Wedding", 40, "Dornoch", "j + l wedding", False)
event2 = Event("24/09/21", "buisness meeting", 10, "B40", "codeclan weeekly planning meeting", True )

events=[event1, event2]

def add_new_event(event):
    events.append(event)