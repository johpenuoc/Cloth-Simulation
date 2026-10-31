def init(obj):
    for id, layer in enumerate(obj):
        for id2, sub in enumerate(layer):
            for id3, p in enumerate(sub):
                # adding an 'applied force' vector (list)
                obj[id][id2][id3].append([0, 0, 0])

    return obj