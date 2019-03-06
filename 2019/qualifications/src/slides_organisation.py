from data_structures import *


def solve1():
    slide = slides_tmp.pop()
    slides.append(slide)
    print("0 " + str(slide))
    while len(slides_tmp) != 0:
        best = 0
        bestScore = slide.scoreWith(slides_tmp[best])
        for j in range(1, min(100, len(slides_tmp))):
            score = slide.scoreWith(slides_tmp[j])
            if bestScore < score:
                bestScore = score
                best = j
        slide = slides_tmp.pop(best)
        slides.append(slide)
        print(str(len(slides)) + " " + str(best) + " " + str(slide))


def solve1bis():  # remove slides_tmp.pop(best) because O(n)  => after the tests, I found out that it was insignificant
    slide = slides_tmp.pop()
    slides.append(slide)
    print("0 " + str(slide))
    len_slides = len(slides_tmp)
    for i in range(-1, len_slides - 1):
        best = i + 1
        bestScore = slide.scoreWith(slides_tmp[best])
        for j in range(i + 1, min(i + 100, len_slides)):
            score = slide.scoreWith(slides_tmp[j])
            if bestScore < score:
                bestScore = score
                best = j
        slide = slides_tmp[best]
        slides.append(slide)
        slides_tmp[i], slides_tmp[best] = slides_tmp[best], slides_tmp[i]
        print(str(len(slides)) + " " + str(best - i) + " " + str(slide))


def solve3():
    while len(slides_tmp) != 0:
        slide = slides_tmp.pop()
        slides.append(slide)
        print(str(len(slides)) + " " + str(slide))
