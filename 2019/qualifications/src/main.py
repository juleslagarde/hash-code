import math
import random
import sys

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
#if len(sys.argv) < 1:
#	file_index = 2
#else:
#	file_index = int(sys.argv[1])

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

def tags_in_common(p0, p1):
    tags0 = p0.tags
    tags1 = p1.tags
    count = 0
    for t0 in tags0:
        for t1 in tags1:
            if t0 == t1:
                count += 1
    return count

#===========================

class Slide:
    def __init__(self, id1, id2=-1):
        self.id1 = id1
        self.id2 = id2
        self.tags = photos[id1].tags + photos[id2].tags
        self.lenTags = str(len(self.tags))

    def __str__(self):
        return str((self.id1, self.id2))+self.lenTags

    def scoreWith(self, slide):
        unique1Cpt = 0
        unique2Cpt = 0
        commonCpt = 0
        for tag in self.tags:
            if tag in slide.tags:
                commonCpt += 1
            else:
                unique1Cpt += 1

        for tag in slide.tags:
            if tag not in self.tags:
                unique2Cpt += 1

        return min(min(unique1Cpt, commonCpt), unique2Cpt)

def solve():
    slide = slides_tmp.pop()
    slides.append(slide)
    print("0 " + str(slide))
    while len(slides_tmp) != 0:
        best = 0
        bestScore = slide.scoreWith(slides_tmp[0])
        for j in range(1, min(1000, len(slides_tmp))):
            score = slide.scoreWith(slides_tmp[j])
            if bestScore < score:
                bestScore = score
                best = j
        slide = slides_tmp.pop(best)
        slides.append(slide)
        print(str(len(slides)) + " " + str(slide))

def solve3():
    while len(slides_tmp) != 0:
        slide = slides_tmp.pop()
        slides.append(slide)
        print(str(len(slides)) + " " + str(slide))

#========= INPUT ===========


f = open(in_file, "r")
photos_count = int(f.readline())
photos = []
photos_h = []
photos_v = []
slides = []
slides_tmp = []

for p in range(0, photos_count):
    photo = Photo(p, f)
    if photo.orientation == "H":
        photos_h.append(photo)
    else:
        photos_v.append(photo)
    photos.append(photo)

#===========================

def construct_slides():
    # Vertical photos with none tags in common
    photos_remaining = []
    while len(photos_v) != 0:
        photo = photos_v.pop()
        if len(photos_v) == 0:
            photos_remaining.append(photo)
            break
        found = False
        for other in photos_v:
            if tags_in_common(photo, other) == 0:
                slides_tmp.append(Slide(photo.id, other.id))
                photos_v.remove(other)
                found = True
                break
        if not found:
            photos_remaining.append(photo)
    # Vertical photos remaining
    while len(photos_remaining) != 0:
        photo = photos_remaining.pop()
        best = 1
        common_tags_count = tags_in_common(photo, photos_remaining[1])
        for i in range(2, len(photos_remaining)):
            other = photos_remaining[i]
            ctg = tags_in_common(photo, other)
            if ctg < common_tags_count:
                common_tags_count = ctg
                best = i
        other = photos_remaining.pop()
        slides_tmp.append(Slide(photo.id, other.id))

    # Horizontal photos
    for photo in photos_h:
        slides_tmp.append(Slide(photo.id))


#for photo in photos:
#    print(photo)
print(len(photos))
print(len(photos_v))
print(len(photos_h))

construct_slides()


def nbTags(slide):
    return len(slide.tags)


slides_tmp = sorted(slides_tmp, key=nbTags, reverse=True)
#random.shuffle(slides_tmp)
 # for slide in slides_tmp:
 #    print(slide)

solve()

file = open(out_file, "w")
file.write(str(len(slides)) + "\n")
for s in slides:
    if s.id2 == -1:
        file.write(str(s.id1) + "\n")
    else:
        file.write(str(s.id1) + " " + str(s.id2) + "\n")

print(len(slides))
#for slide in slides:
#    print(slide)
