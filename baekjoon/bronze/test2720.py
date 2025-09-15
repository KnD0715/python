import sys

N = int(sys.stdin.readline())
for _ in range(N):
   money = int(sys.stdin.readline())
   change = [0] * 4

   while money > 0:
       if money >= 25:
           while money >= 25:
               money -= 25
               change[0] += 1

       elif 10 <= money < 25:
           while money >= 10:
               money -= 10
               change[1] += 1

       elif 5 <= money < 10:
           while money >= 5:
               money -= 5
               change[2] += 1

       else:
           while money > 0:
               money -= 1
               change[3] += 1

   print(*change)