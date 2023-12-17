from animation import RacerIcon
from faker import Faker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from racer import Racer
from race import Race
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import random

class CheeseApp(MDApp):
    def build(self):
        self.colors = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1)]
        self.racers = self.generate_racers()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.result_label = MDLabel(
            text='Today is a fine day for running cheese.',
            halign='center',
            theme_text_color='Primary'
        )
        roll_button = MDRaisedButton(
            text='Roll Your Cheese',
            pos_hint={'center_x': .5},
            on_press=self.roll_cheese
        )
        icon_height = 5
        spacing = 2
        racetrack_height = len(self.racers) * (icon_height + spacing)
        self.racetrack_layout = FloatLayout(size_hint_y=None, height=racetrack_height)
        with self.racetrack_layout.canvas.before:
            Color(0, 0, 0, 1)  # Black color for the border
            self.border = Rectangle(pos=self.racetrack_layout.pos, size=self.racetrack_layout.size)
        self.racetrack_layout.bind(on_layout=self.position_racer_icons)
        layout.add_widget(self.racetrack_layout)
        self.racers_layout = GridLayout(cols=1, size_hint_y=None)
        self.racers_layout.bind(minimum_height=self.racers_layout.setter('height'))
        for i, racer in enumerate(self.racers):
            color = self.colors[i % len(self.colors)]  # Cycle through the colors
            racer_label = MDLabel(
                text=str(racer),
                halign='center',
                theme_text_color='Custom',
                text_color=color,
                size_hint_y=None,
                height=40
            )
            self.racers_layout.add_widget(racer_label)

        scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        scroll_view.add_widget(self.racers_layout)
        self.bet_spinner = Spinner(
            text='Choose a racer',
            values=[racer.name for racer in self.racers],
            size_hint=(None, None),
            size=(200, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        self.icon_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        layout.add_widget(self.icon_layout)
        self.racer_icons = []
        for i, racer in enumerate(self.racers):
            color = self.colors[i % len(self.colors)]
            icon = RacerIcon(color=color, size_hint=(None, None), size=(self.racetrack_layout.width, icon_height))
            icon.y = self.racetrack_layout.height - (i + 1) * (icon_height + spacing)  # Correct y position
            self.racetrack_layout.add_widget(icon)
            self.racer_icons.append(icon)
        layout.add_widget(self.bet_spinner)
        layout.add_widget(Label(text="The Cooper's Hill Cheese-Rolling and Wake Simulator"))
        layout.add_widget(scroll_view)
        layout.add_widget(roll_button)
        layout.add_widget(self.result_label)
        return layout

    def roll_cheese(self, instance):
        race = Race(self.racers)
        winner, injuries = race.simulate_race()
        race_end_width = self.racetrack_layout.width  # Full width of the racetrack

        for racer, icon in zip(self.racers, self.racer_icons):
            duration = 5 / race.calculate_performance_score(racer)
            icon.start_race(race_end_width, duration)
        injury_report = ' '.join([f'{racer.name} got injured!' for racer in injuries])
        bet_result = 'won' if self.bet_spinner.text == winner.name else 'lost'
        self.result_label.text = f'You {bet_result}. {winner.name} won the race. {injury_report}'

    def generate_racers(self, num_racers=6):
        fake = Faker()
        racers = []
        for _ in range(num_racers):
            name = fake.name()
            cheese_affinity = random.randint(1, 10)
            roundness = random.randint(1, 10)
            plungence = random.randint(1, 10)
            racers.append(Racer(name, cheese_affinity, roundness, plungence))
        return racers

    def update_border(self, *args):
        self.border.pos = self.racetrack_layout.pos
        self.border.size = self.racetrack_layout.size

    def position_racer_icons(self, *args):
        icon_height = 5
        spacing = 2
        for i, icon in enumerate(self.racer_icons):
            icon.size = (self.racetrack_layout.width, icon_height)
            icon.y = self.racetrack_layout.y + self.racetrack_layout.height - (i + 1) * (icon_height + spacing)
            icon.x = self.racetrack_layout.x

if __name__ == '__main__':
    CheeseApp().run()
