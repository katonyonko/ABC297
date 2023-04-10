import io
import sys

_INPUT = """\
6
2 3
TTT
T.T
3 5
TTT..
.TTT.
TTTTT
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  for i in range(H):
    print(S[i].replace('TT','PC'))