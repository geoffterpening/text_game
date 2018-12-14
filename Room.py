class Room:
    def __init__(self, name, lat, lon, desc):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.desc = desc


def north():
    global player_lat
    if player_lat < 3:
        player_lat += 1
    else:
        print("There is no door there")


def south():
    global player_lat
    if player_lat > 1:
        player_lat -= 1
    else:
        print("There is no door there")


def east():
    global player_lat
    if player_lon < 3:
        player_lon += 1
    else:
        print("There is no door there")


def west():
    global player_lat
    if player_lon > 1:
        player_lon -= 1
    else:
        print("There is no door there")


def look():
    print("Bitch")


command_dict = {
    'north': north,
    'south': south,
    'east': east,
    'west': west,
    'look': look
}


room1 = Room("Room1", "1", "1", "You are standing in a room, the floor has a number 1 carved into it")
room2 = Room("Room2", "1", "2", "You are standing in a room, the floor has a number 2 carved into it")
room3 = Room("Room3", "1", "3", "You are standing in a room, the floor has a number 3 carved into it")
room4 = Room("Room4", "2", "1", "You are standing in a room, the floor has a number 4 carved into it")
room5 = Room("Room5", "2", "2", "You are standing in a room, the floor has a number 5 carved into it")
room6 = Room("Room6", "2", "3", "You are standing in a room, the floor has a number 6 carved into it")
room7 = Room("Room7", "3", "1", "You are standing in a room, the floor has a number 7 carved into it")
room8 = Room("Room8", "3", "2", "You are standing in a room, the floor has a number 8 carved into it")
room9 = Room("Room9", "3", "3", "You are standing in a room, the floor has a number 9 carved into it")

room_dict = {
    'room1': room1,
    'room2': room2,
    'room3': room3,
    'room4': room4,
    'room5': room5,
    'room6': room6,
    'room7': room7,
    'room8': room8,
    'room9': room9

}
#
# print(room1.lat)