def find_house_1():
	min_dist = lambda x, d : min(int((x)%d), int(d - (x)%d))
	def find_close(a, d):
		global min_dist
		pr_res = [min_dist(x, d) for x in a]
		return a[pr_res.index(min(pr_res))]

	a, b, d = tuple([int(i) for i in input().split()])
	if (a + b)/2 == int((a + b)/2):
		print(int((a + b)/2), min_dist((a + b)/2, d))
	else:
		if abs(a - b) > 1:
			x = [int((a + b)/2), int((a + b)/2) + 1]
			res = find_close(x, d)
			print(res, min_dist(res, d))	
		else:
			x = [a - 1, b + 1]
			res = find_close(x, d)
			print(res, min_dist(res, d))

def find_house_2():
    school, club, ice_interval = map(int, input().split())

    school_club_dist = abs(school - club)

    if school_club_dist > 1:
        first = school_club_dist // 2
        second = school_club_dist - first
    else:
        first = -1
        second = 2 

    leftest_point = min(school, club)

    point_1 = leftest_point + first
    point_2 = leftest_point + second

    remainder_1 = point_1 % ice_interval
    remainder_2 = point_2 % ice_interval

    dist_to_ice_1 = min(remainder_1, ice_interval - remainder_1)
    dist_to_ice_2 = min(remainder_2, ice_interval - remainder_2)

    res = (point_1, dist_to_ice_1) if dist_to_ice_1 <= dist_to_ice_2 else (point_2, dist_to_ice_2)

    print(res[0], res[1])			