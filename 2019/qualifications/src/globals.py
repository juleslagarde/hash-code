
photos = []
photos_h = []
photos_v = []
slides = []
slides_tmp = []


def tags_in_common(p0, p1):
    tags0 = p0.tags
    tags1 = p1.tags
    count = 0
    for t0 in tags0:
        for t1 in tags1:
            if t0 == t1:
                count += 1
    return count