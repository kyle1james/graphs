# http://web.cs.ucdavis.edu/~bai/ECS122A/Closestpair.pdf
# https://www.youtube.com/watch?v=xi-WF07rAQw
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec23.pdf
# http://web.cs.ucdavis.edu/~bai/ECS122A/Closestpair.pdf
# https://www.youtube.com/watch?v=xi-WF07rAQw
import big_num

big_guy = big_num.points# todo o nlogn time
# Done: merge sort
import math
def brute_force(points):
    if len(points) == 2:
        return points
    best = (points[0], points[1])
    past_score = 100
    count = 1
    for x,y in points[count-1:]:
        for i,j in points[count:-1]:
            # manhattan distance
            score = abs(x - i) + abs(y -j)
            # euclidean distance
            #score = math.sqrt( (x-i)**2 + (y-j)**2 )
            if score < past_score:
                best = ((x,y), (i,j))
                past_score = score
                #print(best)
        count +=1
    return(best)

def merge_sort(arr, pos):
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]

        merge_sort(l_half, pos)
        merge_sort(r_half, pos)

        li = ri = k = 0
        # two pointers to stitch together new array
        while li < len(l_half) and ri < len(r_half):
            if l_half[li][pos] < r_half[ri][pos]:
                arr[k] = l_half[li]
                li +=1
            else:
                arr[k] = r_half[ri]
                ri +=1
            k+=1
        # the invarient is that you merge two sorted lists
        # so, this makes sure you merge both lists brah
        while li < len(l_half):
            arr[k] = l_half[li]
            li+=1
            k+=1
        while ri < len(r_half):
            arr[k] = r_half[ri]
            ri+=1
            k+=1

    return arr

def cp_helper(X,Y):
  length = len(X)
  # base case
  if length <= 3:
    return brute_force(X)

  # get median
  mid = (length)//2
  # sort x cords by pos to median
  xl = X[:mid]
  xr = X[mid:]
  # sort y cords of the sorted x cords
  yl = [x for x in Y if x in xl]
  yr = [x for x in Y if x in xr]

  # divide recursively
  (pl, ql) = cp_helper(xl,yl)
  (pr,qr) = cp_helper(xr,yr)


  # distance
  dl = math.sqrt((pl[0]- ql[0])**2 + (pl[1] - ql[1])**2)
  dr = math.sqrt((pr[0]- qr[0])**2 + (pr[1] - qr[1])**2)

  # finding min points for left and right halves
  d = min(dl,dr)

  # points in y where x-cord is within d of mid
  ys = [x for x in Y if x[0] - d <= X[mid][0]]

  # checking points that cross left/right line for min
  e = float('Inf')

  for i in range(len(ys)-1):
    p = ys[i]
    new_min = min(i+7, len(ys))
    new_loop = ys[i+1:new_min]
    for q in new_loop:
      loop_dist = math.sqrt( ( p[0]- q[0] )**2 + ( p[1] - q[1] )**2 )
      if e > loop_dist:
        e = loop_dist
        pp = p
        qq = q

  if e < d:
    return(pp,qq)
  elif dr < dl:
    return(pr,qr)
  else:
    return(pl,ql)



def closest_pair(points):
    if len(points) <= 3:
        # no need for divide_conquer if n < 3
        return brute_force(points)
    else:
        # preprocess arrays to make life easier and faster

        # sort by x cords & sort by y cords
        arr_x = list(points)
        arr_y = list(points)
        # Do everything yourself because otherwise what do you learn?
        # Run merge sort as it is O(nlogn)
        # pass in arr and pos of where to sort, e.g. x or y
        sorted_x = merge_sort(arr_x,0)
        sorted_y = merge_sort(arr_y,1)

        # the pythonic way
        #sorted_x.sort(key=lambda x: x[0])
        #sorted_y.sort(key=lambda x: x[1])

        # Basic visual test passes
        # print(sorted_x)
        # print(sorted_y)

        # pass the dirty work to
        return cp_helper(sorted_x,sorted_y)






points = (
            (2, 2), # A
            (2, 3), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
        )
#expected = ((6, 3), (7, 4))

points2 =(
                (2, 2), # A
                (2, 8), # B
                (5, 5), # C
                (5, 5), # C
                (6, 3), # D
                (6, 7), # E
                (7, 4), # F
                (7, 9)  # G
        )
#expected =((5, 5), (5, 5))

points3 =((523.5139692759321, -296.7442311708965), (-133.05821275435656, -425.43580429241126), (317.2449514411967, -360.8834782870809), (409.2591050707605, -110.19926849874086), (-55.77620609750431, 11.666782902636495), (207.05573000407796, -166.29872475550832), (86.95274797772912, 15.417411093001775), (-0.5426634713212408, -421.11205060411714), (-107.81856221322658, -124.05310216790309), (290.93360338461116, -510.01037111229937), (175.58073583784568, -297.6878118765567), (174.5281500180918, 164.3521715375582), (-98.04792032251606, -232.56592836443747), (49.08553172409406, -142.01881337746335), (466.51898654331836, 55.4641076875605), (630.8648958305262, 45.266420798565974), (219.72144506224996, -57.249191371286855), (590.1807567592095, -92.06517641397801), (182.52130748170026, -477.34102479503906), (478.7286538716342, -442.028554044102), (-44.2541695361207, 39.679626039299194), (444.1327604995383, -524.928399501247), (39.738421016527425, 196.71103703844148), (28.993426535260376, -308.33020858219453), (396.98561227882897, -203.05641477727266), (262.79917111151826, 98.50239375327888))



print(closest_pair(big_guy))
