from functools import reduce


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]


def room_area(room):
    return room["length"] * room["width"]


areas = list(map(room_area, rooms)) # список площадей комнат
total_area = reduce(lambda a, b: a + b, areas) # сумма площадей комнат

print(f"Площадь : {total_area} м^2")