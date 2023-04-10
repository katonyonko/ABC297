import io
import sys

_INPUT = """\
6
4 6
20 25 30 100
2 10
2 1
10 200000
955277671 764071525 871653439 819642859 703677532 515827892 127889502 881462887 330802980 503797872
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop, heappush
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  h=[0]
  s=set()
  while len(s)<=K:
    while True:
      x=heappop(h)
      if x not in s: break
    s.add(x)
    for i in range(N):
      heappush(h,x+A[i])
  print(sorted(list(s))[-1])