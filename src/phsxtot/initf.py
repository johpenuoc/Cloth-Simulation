def initialise(obj):

    points = obj[0]
    for id, layer in enumerate(points):
        for id2, p in enumerate(layer):
            # this is to keep track of the previous position
            obj[0][id][id2].append(p[3])

    print(obj[0])

    return obj