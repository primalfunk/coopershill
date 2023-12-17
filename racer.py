class Racer:
    def __init__(self, name, cheese_affinity, roundness, plungence):
        self.name = name
        self.cheese_affinity = cheese_affinity
        self.roundness = roundness
        self.plungence = plungence

    def __str__(self):
        return f'{self.name}: Affinity={self.cheese_affinity}, Roundness={self.roundness}, Plungence={self.plungence}'