import sys
from slides_creation import *
from slides_organisation import *
from data_structures import *

IN_FOLDER = "../in/"
OUT_FOLDER = "../out/"
FILES = [
    "a_example",
    "b_lovely_landscapes",
    "c_memorable_moments",
    "d_pet_pictures",
    "e_shiny_selfies"
]
file_index = 2
if len(sys.argv) > 1:
    file_index = int(sys.argv[1])

in_file = IN_FOLDER + FILES[file_index] + ".txt"
out_file = OUT_FOLDER + FILES[file_index] + ".out"

# ========= INPUT ===========

f = open(in_file, "r")

photos_count = int(f.readline())

for p in range(0, photos_count):
    photo = Photo(p, f)
    if photo.orientation == "H":
        photos_h.append(photo)
    else:
        photos_v.append(photo)
    photos.append(photo)

# ===========================

# for photo in photos:
#    print(photo)
print(len(photos))
print(len(photos_v))
print(len(photos_h))

construct_slides()

slides_tmp = sorted(slides_tmp, key=lambda slide: len(slide.tags), reverse=True)
# random.shuffle(slides_tmp)

solve1()

file = open(out_file, "w")
file.write(str(len(slides)) + "\n")
for s in slides:
    if s.id2 == -1:
        file.write(str(s.id1) + "\n")
    else:
        file.write(str(s.id1) + " " + str(s.id2) + "\n")

print(len(slides))
print("score + " + str(calcScore()))
# for slide in slides:
#    print(slide)
