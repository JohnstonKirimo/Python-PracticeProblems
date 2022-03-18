""

""
#Solution

if __name__ == '__main__':
    xr = range(int(input())+1)
    yr = range(int(input())+1)
    zr = range(int(input())+1)
    n = int(input())

arr = [[x, y, z] for x in xr for y in yr for z in zr if x+y+z != n]
print(arr)
