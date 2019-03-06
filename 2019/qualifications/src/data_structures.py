from globals import *


class Photo:
    def __init__(self, id, file):
        line = file.readline().split()
        self.id = id
        self.orientation = line[0]
        self.tags_count = int(line[1])
        self.tags = line[2:]

    def __str__(self):
        return str((self.id, self.orientation, self.tags))


class Slide:
    def __init__(self, id1, id2=-1):
        self.id1 = id1
        self.id2 = id2
        self.tags = [] + photos[id1].tags
        if id2 != -1:
            for tag in photos[id2].tags:
                if tag not in self.tags:
                    self.tags.append(tag)
        self.lenTags = str(len(self.tags))

    def __str__(self):
        return str((self.id1, self.id2)) + self.lenTags

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
