import io
import sys

_INPUT = """\
6
3 8
1234567890 1234567890
1597 987
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  ans=0
  while A!=B:
    x,y=max(A,B),min(A,B)
    if x%y==0:
      ans+=x//y-1
      A,B=x-(x//y-1)*y,y
    else:
      ans+=x//y
      x-=(x//y)*y
      A,B=x,y
  print(ans)