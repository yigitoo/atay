class Coordinates:
    def __init__(self, coordinate: tuple[float] = None):
        self.coordinate = coordinate if coordinate is not None else (0, 0)

        self.x = coordinate[0]
        self.y = coordinate[1]

        self.lat = self.x
        self.latitude = self.x
        self.enlem = self.x

        self.lng = self.y
        self.longitude = self.y
        self.boylam = self.y

    def set(self, coordinate: tuple[float] = None):
        self.coordinate = coordinate if coordinate is not None else self.coordinate

        self.x = coordinate[0]
        self.y = coordinate[1]

        self.lat = self.x
        self.latitude = self.x
        self.enlem = self.x

        self.lng = self.y
        self.longitude = self.y
        self.boylam = self.y

    def get(self):
        return self.coordinate

    def set_x(self, value: float = None):
        self.coordinate = self.coordinate.set(
            value, self.coordinate[1]
        ) if value is not None else self.coordinate

    def set_y(self, value: float = None):
        self.coordinate = self.coordinate.set(
            self.coordinate[0], value
        ) if value is not None else self.coordinate

    def get_x(self):
        return self.coordinate[0]

    def get_y(self):
        return self.coordinate[1]

class Map:
    pass
    # Unimplemented Class

# Some tests
if __name__ == '__main__':
    pass
