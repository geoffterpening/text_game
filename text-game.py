from Room import *


# ---------------Variables

player_lat = 2
player_lon = 2
player_exit = "n"
current_room_name = [room.name for room in room_list if room.lat == player_lat and room.lon == player_lon]
current_room_description = [room.desc for room in room_list if room.lat == player_lat and room.lon == player_lon]
test = ""


# --------------Functions

def south():
    global player_lat
    global current_room_description
    global current_room_name
    if player_lat < 3:
        player_lat += 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def north():
    global player_lat
    global current_room_description
    global current_room_name
    if player_lat > 1:
        player_lat -= 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def west():
    global player_lon
    global current_room_description
    global current_room_name
    if player_lon < 3:
        player_lon += 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def east():
    global player_lon
    global current_room_description
    global current_room_name
    if player_lon > 1:
        player_lon -= 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def look():
    global current_room_description
    print(current_room_description[0])


def exit_program():
    global player_exit
    player_exit = "y"



command_dict = {
    'north': north,
    'south': south,
    'east': east,
    'west': west,
    'look': look,
    'exit': exit_program
}

# -------------------game loop
while player_exit != "y":
    # Intro
    print("Welcome to Adventuretron you fucking bitch. It's the best game in the world!")
    print("You find yourself standing in a room. What the fuck do you do?")
    input("Press enter to begin:")
    print("\n Enter a command below:")

    while player_exit != "y":
        try:
            # input
            # print(current_room_name[0])
            command = input("> ")
            command_dict[command]()
            print(str(player_lat) + " Lat, " + str(player_lon) + " Lon")
            # find()
        except KeyError:
            print("I don't recognize that command.")



print("Goodbye!")
input('press any key to exit')