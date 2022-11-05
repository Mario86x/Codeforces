import sys
#input = sys.stdin.readline
input = open('input.txt','r').readline
import math
global active_comments
############ ---- Input Functions ---- ############
#integer inputs
def inp():
    return(int(input()))
#list inputs
def inlt():
    return(list(map(int,input().split())))
#string inputs
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
#space separated variable inputs
def invr():
    return(map(int,input().split()))
def read_inputs():
    l=inlt()
    return l[0],l[1],l[2]
def smartprint(*args):
    if active_comments:
        print(args)
    return None

active_comments=0
n_tests=inp()

for i in range(n_tests):
    smartprint("test n:",i)
    n,d,hp=read_inputs()
    A=inlt()
    #normalize
    gcddhp=math.gcd(d,hp)
    d=int(d/gcddhp)
    hp=int(hp/gcddhp)
#   calculate
#   stage 1 attacks are fully effective
#   all attacks can be made in sequence one group after the other since there is no particular convenience
    #plim = hp of each group must be < plim in stage 1
    C=[math.floor(A[i]/d)*hp for i in range(n)]
    def Vdnocum(i):
        if i==0:
            return math.floor(d/hp)
        else:
            return math.floor((i+1)*d/hp)-math.floor(i*d/hp)
    damage_killed_count=0
    damage_killed_cum=0
    for c in C:
        for i in range(c):
            damage_killed_count+=Vdnocum(i%hp)
            damage_killed_cum+=damage_killed_count
    D1=(sum(C)-1)*sum(A)-damage_killed_cum
    smartprint(D1)
    smartprint("C:",C)
    smartprint("A:",A)
#   stage 2 attacks kill the groups still alive
#   if d<hp it's better to start from the biggest
    M=[A[i]*hp-C[i]*d for i in range(n)]
    M_pos=[m for m in M if m>0]
    M_pos.sort(reverse=True)
    smartprint("M_pos:",M_pos)
    n_attacks_stage2=0
    Attack_list=[[Vdnocum(i) for i in range(math.ceil(m/d))] for m in M_pos]
    for i in range(len(M_pos)):
        last_attack_correction=-math.floor((math.ceil(M_pos[i]/d)*d-M_pos[i])/hp)
        if not not Attack_list[i]:
            Attack_list[i][-1]+=last_attack_correction
            smartprint("corrected attack n: ",i," by: ",last_attack_correction)
    if not not Attack_list:
        smartprint("attack_list: ",Attack_list)
        def evaluate(attack,max_len):
            return -1 if not attack else sum([attack[i]*math.pow(2,max_len-i) for i in range(len(attack))])
        smartprint("maxlen: ",max([len(i) for i in Attack_list]))
        max_len=max([len(i) for i in Attack_list])
        while sum([len(i) for i in Attack_list])>1:
            Value_attacks=[evaluate(a,max_len) for a in Attack_list]
            max_val = max(Value_attacks)
            max_idx = Value_attacks.index(max_val)
            damage_killed_count+=Attack_list[max_idx][0]
            damage_killed_cum+=damage_killed_count
            n_attacks_stage2+=1
            Attack_list[max_idx].pop(0)
            smartprint("attack stage 2: ",n_attacks_stage2,"attacking stack n:",max_idx)
            smartprint(Attack_list)
    D2=(sum(C)+n_attacks_stage2)*sum(A)-damage_killed_cum        
    # print((sum(C)+len(M_pos)-1))
#    write_output()
    print(D2+1)



    
