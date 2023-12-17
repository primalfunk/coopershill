import random

class Race:
    def __init__(self, racers):
        self.racers = racers

    def simulate_race(self):
        injuries = self.calculate_injuries()
        healthy_racers = [racer for racer in self.racers if racer not in injuries]
        winner = max(healthy_racers, key=self.calculate_performance_score)
        return winner, injuries

    def calculate_performance_score(self, racer):
        return (racer.cheese_affinity + racer.roundness + racer.plungence) * random.uniform(0.8, 1.2)

    def calculate_injuries(self):
        injuries = []
        for racer in self.racers:
            if random.random() < self.calculate_injury_chance(racer):
                injuries.append(racer)
        return injuries

    def calculate_injury_chance(self, racer):
        return max(0, 0.2 - racer.roundness * 0.02)