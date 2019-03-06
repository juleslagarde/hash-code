from data_structures import *


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
        best = 0
        common_tags_count = tags_in_common(photo, photos_remaining[0])
        for i in range(1, len(photos_remaining)):
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
