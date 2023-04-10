import io
import sys

_INPUT = """\
6
3 1 2
2 3 3
5 1 1
3 1 4 1 5
7 3 14
10 20 30 40 50 60 70
21 3 14
10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210
2 1 1
1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,L,R=map(int,input().split())
  A=list(map(int,input().split()))
  x=0
  for i in range(N):
    y=A[i]-(A[i]//(R+L))*(R+L)
    z=y//L
  print('First' if x!=0 else 'Second')