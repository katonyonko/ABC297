import io
import sys

_INPUT = """\
6
2 2 2
10 10 1
314 159 2653
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W,K=map(int,input().split())
  mod=998244353
  F=[1]
  N=1000**2
  for i in range(N):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
    I.append(I[-1]*(N-i)%mod)
  I=I[::-1]
  dp=[0]*((H+1)*(W+1))
  def idx(i,j):
    return i*(W+1)+j
  def comb(n,k):
    if n<0 or k>n: return 0
    return F[n]*I[k]*I[n-k]%mod
  for i in range(1,H+1):
    for j in range(1,W+1):
      if i*j<K: continue
      dp[idx(i,j)]=comb(i*j,K)-2*comb((i-1)*j,K)-2*comb(i*(j-1),K)+4*comb((i-1)*(j-1),K)
      dp[idx(i,j)]%=mod
      if i>1:
        dp[idx(i,j)]+=comb((i-2)*j,K)-2*comb((i-2)*(j-1),K)
        dp[idx(i,j)]%=mod
      if j>1:
        dp[idx(i,j)]+=comb(i*(j-2),K)-2*comb((i-1)*(j-2),K)
        dp[idx(i,j)]%=mod
      if i>1 and j>1:
        dp[idx(i,j)]+=comb((i-2)*(j-2),K)
        dp[idx(i,j)]%=mod
  print(sum([dp[i]*(i//(W+1))*(i%(W+1))*(H+1-i//(W+1))*(W+1-i%(W+1)) for i in range((H+1)*(W+1))])*pow(comb(H*W,K),mod-2,mod)%mod)