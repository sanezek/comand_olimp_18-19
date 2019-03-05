n,m = list(map(int,input().split()))
loops = list(map(int,input().split()))
members = [0 for i in range(n)]
first = -1
max_ = -1
for i in loops:
	members[i-1] += 1
	if max_ < members[i-1]:
		first = i
		max_ =  members[i-1]

print(first)