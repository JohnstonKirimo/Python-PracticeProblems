"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
 Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...].
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
"""
#Solution
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = [0] # initially max height is 0

        coords = []

        for l, r, h in buildings:
            coords.append((l, -h)) # -h represents start of building
            coords.append((r, +h)) # +h represents end of building

        coords.sort() # sort by x coord followed by y coord (height)
        result = []

        for coord, h in coords:
            prev_max = heap[0] # keep track of prev max to see whether there is any change due to new building's ending or starting
            if h > 0: # if a building ends at this point
                heap.remove(-h) # we should remove it from heap
                heapify(heap)
            else:
                heappush(heap, h)

            if prev_max != heap[0]: # if max has changed in heap
                result.append((coord, -heap[0])) # we should add this to result

        return result
