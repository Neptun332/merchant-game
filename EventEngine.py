from Event import Event


class EventEngine:

    def __init__(self):
        self.events = []

    def register_event(self, event: Event):
        self.events.append(event)
