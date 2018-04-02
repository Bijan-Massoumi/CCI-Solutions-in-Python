



def find_greatest_well(rods):
    if len(rods) <= 1:
        return 0
    elif len(rods) == 2:
        return min(rods[0],rods[1])
    else:
        rod_tuples = []
        for i,val in enumerate(rods):
            rod_tuples.append((i,val))

        rod_tuples_sorted = sorted(rod_tuples,key=lambda x: x[1])[::-1]
        first,sec = rod_tuples_sorted[0], rod_tuples_sorted[1]
        return_coords = [first[0],sec[0]]
        max_area = min(first[1],sec[1]) * abs(first[0] - sec[0])
        exclusion_bounds = [first[0],sec[0]]

        for tup in rod_tuples_sorted[2:]:

            if tup[0] < exclusion_bounds[0]:
                exclusion_bounds[0] = tup[0]
                A1 = min(rod_tuples[return_coords[0]][1],tup[1]) * abs(return_coords[0] - tup[0])
                A2 = min(rod_tuples[return_coords[1]][1],tup[1]) * abs(return_coords[1] - tup[0])

                if A1 > max_area:
                    return_coords = (tup[0], return_coords[0])
                    max_area = A1
                if A2 > max_area:
                    return_coords = (tup[0],return_coords[1])
                    max_area = A2

            elif tup[0] > exclusion_bounds[1]:
                exclusion_bounds[1] = tup[0]
                A1 = min(rod_tuples[return_coords[0]][1],tup[1]) * abs(return_coords[0] - tup[0])
                A2 = min(rod_tuples[return_coords[1]][1],tup[1]) * abs(return_coords[1] - tup[0])

                if A1 > max_area:
                    return_coords = (return_coords[0],tup[0])
                    max_area = A1
                if A2 > max_area:
                    return_coords = (return_coords[1],tup[0])
                    max_area = A2

        return max_area, return_coords


if __name__ == "__main__":
    test = [7,6,7,8,9,88,88]
    print(find_greatest_well(test))
