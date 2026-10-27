import statistics
# note: due to zero-based list indexing, if your vectors
# are of dimension d, dim = d - 1
def dom(r: list, b: list, dim: int) -> list:
    completeList = r + b
    n = len(completeList)

    if n <= 1:
        print(f"complete list: {completeList}")
        print("nothing returned\n")
        return []
    elif dim == -1:
        out = []
        for redPoint in r:
            for bluePoint in b:
                out.append((redPoint,bluePoint))
        print("============")
        print(f"all points: {out}\n")
        return out
    else:
        print(f"red:  {r}")
        print(f"blue: {b}")
        coordsDimList = []
        # coordsDimList is the list of the dim-th 
        # coordinates of all points (0 based indexing)
        for i in range(n):
            coordsDimList.append(completeList[i][dim]) 
        median      = statistics.median(coordsDimList)
        leftRed     = []
        rightRed    = []
        leftBlue    = []
        rightBlue   = []
        for redPoint in r:
            if redPoint[dim] <= median:
                leftRed.append(redPoint)
            else:
                rightRed.append(redPoint)

        for bluePoint in b:
            if bluePoint[dim] <= median:
                leftBlue.append(bluePoint)
            else:
                rightBlue.append(bluePoint)
        print(f"median: {median}") 
        print(f"dim: {dim}")
        print(f"left red  : {leftRed}")
        print(f"right red : {rightRed}")
        print(f"left blue : {leftBlue}")
        print(f"right blue: {rightBlue}")
        print()
        
        if r == leftRed and b == leftBlue:
            return dom(leftRed, leftBlue, dim - 1) + dom(rightRed, rightBlue, dim) + dom(leftRed, rightBlue, dim - 1)
        return dom(leftRed, leftBlue, dim) + dom(rightRed, rightBlue, dim) + dom(leftRed, rightBlue, dim - 1)

# sample inputs

#r = [ (1.1,1.01,0.99), (1.000001,1.999,3.1), (3.2,4.3,2.01) ]
#b = [ (3.01,3.00,3.11), (1.22,0.98,2.1), (0.11,1.11,1.001) ]

r = [ (1,1,1), (1,2,3), (3,4,2) ]
b = [ (3,3,3), (1,1,2), (0,1,1) ]

#r = [ (0,1,2,3), (1,2,3,4), (2,3,4,5) ]
#b = [ (2,3,4,5), (1,3,3,4), (3,4,5,6) ]


#r = [ (0,1,2,3), (1,2,3,4), (2,3,4,5), (2,2,1,1), (0,0,0,0) ]
#b = [ (1.9,3.1,4.3,5.0001), (1.1,1.5,3.01,4.12), (3.9,4.22,5.21,6.7) ]


d = dom(r,b,2)

print("Inputs:")
print(f"R: {r}")
print(f"B: {b}")

print("\nOutput:")
for pair in d:
    print(pair)
