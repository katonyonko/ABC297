import io
import sys

_INPUT = """\
6
RNBQKBNR
KRRBBNNQ
BRKRBQNN
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  S=input()
  ans='Yes'
  d=defaultdict(list)
  for i in range(8):
    d[S[i]].append(i)
  if d['B'][0]%2==d['B'][1]%2: ans='No'
  x,y=sorted(d['R'])
  z=d['K'][0]
  if z<x or y<z: ans='No'
  print(ans)