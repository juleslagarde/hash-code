IN_FOLDER = "../in/"
OUT_FOLDER = "../out/"
FILES = [
    "a_example",
    "b_lovely_landscapes"
    "c_memorable_moments"
    "d_pet_pictures"
    "e_shiny_selfies"
]
file_index = 0
in_file = IN_FOLDER + FILES[file_index] + ".txt"
out_file = OUT_FOLDER + FILES[file_index] + ".out"

class Photo:
    def __init__(self, id, file):
        line = file.readline().split()
        self.id = id
        self.orientation = line[0]
        self.tags_count = int(line[1])
        self.tags = line[2:]

    def __str__(self):
        return str((self.id, self.orientation, self.tags))

#===========================

f = open(in_file, "r")
photos_count = int(f.readline())
photos = []
photos_h = []
photos_v = []
slides = []

for p in range(0, photos_count):
    photo = Photo(p, f)
    if photo.orientation == "H":
        photos_h.append(photo)
    else:
        photos_v.append(photo)
    photos.append(photo)

#===========================

for photo in photos_v:
    print(photo)
