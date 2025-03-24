import csv, random

MAP_WIDTH = 200
MAP_HEIGHT = 300

def gen_lake(height, map):
    lake = []
    top_bank = []
    bottom_bank = []

    for _ in range(MAP_WIDTH):
        bottom_bank.append(round(random.randint(-500, 100) / 100, 1))
    for _ in range(MAP_WIDTH):
        top_bank.append(round(random.randint(-500, 100) / 100, 1))

    for _ in range(height-2):
        row = []
        for _ in range(MAP_WIDTH):
            row.append(round(random.randint(-1000, 0) / 100, 1))
        lake.append(row)

    return map + [top_bank] + lake + [bottom_bank]


def gen_land(height, map):
    land = []

    for _ in range(height):
        row = []
        for _ in range(MAP_WIDTH):
            row.append(round(random.randint(0, 500) / 100, 1))
        land.append(row)

    return map + land
    

def gen_mountain(height, map):
    mountain_range = []
    top_mountain_foot = []
    bottom_mountain_foot = []  

    for _ in range(2):
        row = []
        for _ in range(MAP_WIDTH):
            row.append(round(random.randint(500, 1000) / 100, 1))
        top_mountain_foot.append(row)
    for _ in range(2):
        row = []
        for _ in range(MAP_WIDTH):
            row.append(round(random.randint(500, 1000) / 100, 1))
        bottom_mountain_foot.append(row)

    for _ in range(height-4):
        row = []
        while len(row) < MAP_WIDTH:
            tall_mountains = random.randint(1, 20)
            short_mountains = random.randint(1, 20)

            for _ in range(tall_mountains):
                row.append(round(random.randint(1200, 1600) / 100, 1))
            for _ in range(short_mountains):
                row.append(round(random.randint(800, 1300) / 100, 1))
            
        mountain_range.append(row[:MAP_WIDTH])
    
    return map + top_mountain_foot + mountain_range + bottom_mountain_foot


def gen_mine_field(height, map):
    mine_field = []

    for _ in range(height):
        row = []
        while len(row) < MAP_WIDTH:
            safe_zone = random.randint(1, 3)
            mine_zone = random.randint(1, 7)

            for _ in range(safe_zone):
                row.append(round(random.randint(0, 500) / 100, 1))
            for _ in range(mine_zone):
                row.append("x")
        
        mine_field.append(row[:MAP_WIDTH])
    
    return map + mine_field


def gen_map():
    map = []
    map = gen_mountain(10, map)

    while len(map) < MAP_HEIGHT:
        type_ = random.randint(1, 4)

        if type_ == 1:
            map = gen_lake(random.randint(10, 20), map)
        elif type_ == 2:
            map = gen_land(random.randint(10, 20), map)
        elif type_ == 3:
            map = gen_mountain(random.randint(20, 30), map)
        elif type_ == 4:
            map = gen_mine_field(random.randint(5, 10), map)
    
    map = map[:MAP_HEIGHT-10]
    map = gen_land(10, map)

    return map


def create_csv():
    map = gen_map()
    with open("map.csv", 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(map)

create_csv()