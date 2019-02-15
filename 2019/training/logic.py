from pizza import PizzaPart

class Cell:
    def __init__(self, x, y, inside):
        self.x = x
        self.y = y
        self.inside = inside
        self.part_id = -1


def createsParts(pizza, parts):
    print("createParts...")
    # tab initialisation
    tab = []
    for x in range(pizza.w):
        tab.append([])
        for y in range(pizza.h):
            tab[x].append(Cell(x, y, pizza.tab[x][y]))
    # stats
    tomatoes = 0
    mushrooms = 0
    for col in pizza.tab:
        for c in col:
            if c == 'T':
                tomatoes += 1
            elif c == 'M':
                mushrooms += 1
            else:
                print("error:" + c)
    print("T:" + str(tomatoes))
    print("M:" + str(mushrooms))

    data = {
        "tab": tab,
        "parts": parts,
        "min": pizza.min,
        "max": pizza.max,
        "nextId": 0
    }
    fillRegion(data, 0, 0, pizza.w, pizza.h)


def fillRegion(data, min_x, min_y, dx, dy):
    if dx == 1 and dy == 1:
        findPart(data, min_x, min_y)
    else:
        fillRegion(data, min_x, min_y, max(1, dx // 2), max(1, dy // 2))
        if dx == 1:
            fillRegion(data, min_x, min_y + dy // 2, max(1, dx // 2), dy - (dy // 2))
        elif dy == 1:
            fillRegion(data, min_x + dx // 2, min_y, dx - (dx // 2), max(1, dy // 2))
        else:
            fillRegion(data, min_x, min_y + dy // 2, max(1, dx // 2), dy - (dy // 2))
            fillRegion(data, min_x + dx // 2, min_y, dx - (dx // 2), max(1, dy // 2))
            fillRegion(data, min_x + dx // 2, min_y + dy // 2, dx - (dx // 2), dy - (dy // 2))


def findPart(data, x, y):
    max_c = data["max"]
    min_c = data["min"]
    for i in range(max_c)[::-1]:  # todo: optimize biggest area first
        for j in range(max_c)[::-1]:
            if (i+1)*(j+1) > max_c or (i+1)*(j+1) < 2*min_c:  # if there to much cell or if there is not enough
                continue
            if checkPart(data,   x-i, y-j, i+1, j+1):
                createPart(data, x-i, y-j, i+1, j+1)
            # if checkPart(data,   x-j, y-i, j+1, i+1): # not necessary ?
            #     createPart(data, x-j, y-i, j+1, i+1)


def checkPart(data, x, y, dx, dy):
    tab = data["tab"]
    min_c = data["min"]
    tomatoes = 0
    mushrooms = 0
    tmp_parts = {}
    if x < 0 or y < 0:
        return False  # if any Part not inside the pizza return false
    for rel_x in range(dx):
        for rel_y in range(dy):
            cell = tab[x + rel_x][y + rel_y]
            if cell.inside == 'T':
                tomatoes += 1
            else:
                mushrooms += 1
            part_id = cell.part_id
            if part_id != -1:
                if part_id in tmp_parts.keys():
                    tmp_parts[part_id].append([x+rel_x, y+rel_y])
                else:
                    tmp_parts[part_id] = [[x+rel_x, y+rel_y]]
    if mushrooms < min_c or tomatoes < min_c:
        return False

    parts = data["parts"]
    for part_id in tmp_parts.keys():
        if parts[part_id].count() != len(tmp_parts[part_id]):
            return False  # the new part does cover all older part
        assert parts[part_id].count() >= len(tmp_parts[part_id])

    # the part is valid and bigger, so delete old ones
    for part_id in tmp_parts.keys():
        parts.pop(part_id)

    return True


def createPart(data, x, y, dx, dy):
    tab = data["tab"]
    parts = data["parts"]
    parts[data["nextId"]] = PizzaPart(x, y, dx, dy)
    for rel_x in range(dx):
        for rel_y in range(dy):
            tab[x+rel_x][y+rel_y].part_id = data["nextId"]
    data["nextId"] += 1
