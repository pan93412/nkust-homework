import math
from tkinter import Tk, Canvas
from datetime import datetime
from typing import TypedDict


class HandAttribute(TypedDict):
    color: str
    stroke_width: int
    length: int


class Clock:
    def __init__(self, root, canvas_width=640, canvas_height=480):
        self.root = root
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas = Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='skyblue')
        self.canvas.pack()

        self.clock_center_x = self.canvas_width // 2
        self.clock_center_y = self.canvas_height // 2
        self.clock_radius = self.clock_center_x // 2
        self.outline_width = 8

        # define properties for each clock hand
        self.hand_attributes: dict[str, HandAttribute] = \
            {"hour": {"color": "brown", "stroke_width": 5, "length": 70},
             "minute": {"color": "blue", "stroke_width": 4, "length": 110},
             "second": {"color": "red", "stroke_width": 2, "length": 130}}

    def draw_clock(self):
        self._draw_circle()
        self._draw_scales_and_numerals()
        self._draw_hands_and_center()
        self.update_hands_positions()

    def _draw_circle(self):
        self.canvas.create_oval(
            self.clock_center_x - self.clock_radius,
            self.clock_center_y - self.clock_radius,
            self.clock_center_x + self.clock_radius,
            self.clock_center_y + self.clock_radius,
            outline='darkblue', fill='lightgray', width=self.outline_width)

    def _draw_scales_and_numerals(self):
        for i in range(0, 360):
            self._draw_scale(i)
            if i % 30 == 0:
                self._draw_numeral(i)

    def _draw_scale(self, angle):
        start_radius = self.clock_radius - self.outline_width // 2
        end_radius = self.clock_radius - 10

        scale_coordinates = [
            self.clock_center_x + start_radius * math.cos(math.radians(angle)),
            self.clock_center_y + start_radius * math.sin(math.radians(angle)),
            self.clock_center_x + end_radius * math.cos(math.radians(angle)),
            self.clock_center_y + end_radius * math.sin(math.radians(angle))
        ]

        if angle % 6 == 0:
            self.canvas.create_line(*scale_coordinates, fill="black", width=2 if angle % 30 else 5)

    def _draw_numeral(self, angle):
        numeral_font_size = 18
        numeral_radius = self.clock_radius - numeral_font_size // 2 - 10
        numeral_coordinates = [
            self.clock_center_x + numeral_radius * math.cos(math.radians(angle)),
            self.clock_center_y + numeral_radius * math.sin(math.radians(angle))
        ]

        numeral = (angle // 30 + 3) % 12 or 12
        self.canvas.create_text(*numeral_coordinates, text=numeral, fill="black",
                                font=("Times", numeral_font_size, "bold"))

    def _draw_hands_and_center(self):
        self.hands = {}
        for hand, attributes in self.hand_attributes.items():
            self.hands[hand] = self.canvas.create_line(
                self.clock_center_x,
                self.clock_center_y,
                self.clock_center_x + attributes['length'] * int(math.cos(
                    math.radians(-90))),
                self.clock_center_y + attributes['length'] * int(math.sin(
                    math.radians(-90))),
                fill=attributes["color"],
                width=attributes["stroke_width"])

        dot_radius = 3
        self.canvas.create_oval(self.clock_center_x - dot_radius, self.clock_center_y - dot_radius,
                                self.clock_center_x + dot_radius, self.clock_center_y + dot_radius,
                                fill="black", width=0)

    def update_hands_positions(self):
        now = datetime.now()
        time_values = {"hour": now.hour % 12, "minute": now.minute, "second": now.second}

        for hand, hand_value in time_values.items():
            hand_item = self.hands[hand]
            hand_length = self.hand_attributes[hand]['length']
            self.canvas.coords(
                hand_item,
                self.clock_center_x,
                self.clock_center_y,
                self.clock_center_x + hand_length * math.cos(math.radians(hand_value * 6 - 90)),
                self.clock_center_y + hand_length * math.sin(math.radians(hand_value * 6 - 90)))

        self.canvas.after(200, self.update_hands_positions)  # refresh every 200 ms


if __name__ == "__main__":
    my_window = Tk()
    my_clock = Clock(my_window)
    my_clock.draw_clock()
    my_window.mainloop()
