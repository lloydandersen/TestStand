class MissionProfile:
    """Creates a container object for a mission
    profile."""

    def __init__(self, name: str, vehicle: str) -> None:
        self.profile = []
        self.name = name
        self.vehicle = vehicle

    def make_graph(self):
        pass

