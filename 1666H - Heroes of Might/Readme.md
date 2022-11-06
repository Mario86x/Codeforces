My first attempt on Heroes of might problem https://codeforces.com/problemset/problem/1666/H

I tried to run some tests manually, as for this problem the website does not accept virtual submissions

The code seems to work, but it is slow on some cases. I don't think this is due to python, I think I should work on a math
formula that avoids some cycles

To do list:
1) write a closed formula to avoid this cycle to be too long:

    for c in C:
        for i in range(c):
            damage_killed_count+=Vdnocum(i%hp)
            damage_killed_cum+=damage_killed_count
            
2) Gather all available inputs and solutions from codeforces website and check performances
4) Understand best solutions in C++
