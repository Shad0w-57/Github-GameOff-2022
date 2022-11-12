import pygame

# settings
WIDTH = 1024  # window width
HEIGHT = 640  # window height
TITLE = "Cliché"  # window title

SHAKING_VALUE = 30

MIN_SCORE_GAIN = 3  # minimum random score gain
MAX_SCORE_GAIN = 12  # maximum random score gain

FOOD_FALLING_TIME = 1875  # milliseconds
FOOD_TRANSFORMATION_VALUE = 1  # falling food transformation speed

FONT_SIZE = 16

TIME_X = WIDTH / 2.5
TIME_Y = HEIGHT * 0.96


BORDER_WIDTH = 4
RECT_ROUNDNESS = 15

BACKGROUND_COLOUR = "#0e071b"
BORDER_COLOUR = "#ffeb57"
TEXT_COLOUR = "#edab50"
SCORE_COLOUR = "#5ac54f"

MAP_X = 0
MAP_Y = HEIGHT / 12
MAP_WIDTH = WIDTH
MAP_HEIGHT = WIDTH / 2

SCORE_X = MAP_Y * 3
SCORE_Y = MAP_Y / 8
SCORE_WIDTH = WIDTH - SCORE_X
SCORE_HEIGHT = MAP_Y / 1.25

FOOD_DATA = {
    "bread": "data/images/food/bread.png",
    "donut": "data/images/food/donut.png",
    "croissant": "data/images/food/croissant.png",
    "python": "data/images/food/python.png"
}

CONTINENT_DATA = {
    "north_america": {"food": ["donut", "python"], "min_coords": (11, 7), "max_coords": (87, 55)},
    "south_america": {"food": ["donut", "python"], "min_coords": (67, 57), "max_coords": (100, 101)},
    "europe": {"food": ["bread", "croissant", "python"], "min_coords": (121, 15), "max_coords": (152, 40)},
    "africa": {"food": ["bread", "python"], "min_coords": (113, 38), "max_coords": (163, 90)},
    "asia": {"food": ["bread", "python"], "min_coords": (160, 16), "max_coords": (245, 55)},
    "australia": {"food": ["bread", "python"], "min_coords": (202, 71), "max_coords": (239, 94)},
    "antarctica": {"food": ["bread", "python"], "min_coords": (0, 112), "max_coords": (256, 128)},
}