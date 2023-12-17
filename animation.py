from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty

class RacerIcon(Widget):
    race_width = NumericProperty(5)

    def __init__(self, color, **kwargs):
        super(RacerIcon, self).__init__(**kwargs)
        self.size = (self.race_width, 5)  # Initial size
        with self.canvas:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(race_width=self.update_rect_width, pos=self.update_rect_pos)

    def start_race(self, end_width, duration):
        anim = Animation(race_width=end_width, duration=duration)
        anim.start(self)

    def update_rect_width(self, instance, value):
        self.rect.size = (self.race_width, 5)

    def update_rect_pos(self, instance, value):
        self.rect.pos = self.pos