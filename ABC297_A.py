import io
import sys

_INPUT = """\
6
4 500
300 900 1300 1700
5 99
100 200 300 400 500
4 500
100 600 1100 1600
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,D=map(int,input().split())
  T=list(map(int,input().split()))
  ans=-1
  for i in range(N-1):
    if T[i+1]-T[i]<=D: ans=T[i+1]; break
  print(ans)