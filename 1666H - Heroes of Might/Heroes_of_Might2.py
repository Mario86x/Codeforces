
import sys

import math
global active_comments
############ ---- Input Functions ---- ############
#integer inputs
def inp(input):
    return(int(input()))
#list inputs
def inlt(input):
    return(list(map(int,input().split())))
#string inputs
def insr(input):
    s = input()
    return(list(s[:len(s) - 1]))
#space separated variable inputs
def invr(input):
    return(map(int,input().split()))
def read_inputs(input):
    l=inlt(input)
    return l[0],l[1],l[2]
def read_output(output):
    return int(output())
def smartprint(*args):
    if active_comments:
        print(args)
    return None


active_comments=0

def main(input_file_txt,output_file_txt):
    input = open(input_file_txt,'r').readline
    output= open(output_file_txt,'r').readline
    n_tests=inp(input)
    count_wrong=0
    for test_n in range(n_tests):
        smartprint("test n:",test_n)
        n,d,hp=read_inputs(input)
        smartprint("n:",n,"d:",d,"hp:",hp)
        A=inlt(input)
        solution=read_output(output)
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
        if max(C)>0:
            V_factor=sum([math.floor((i+1)*d/hp) for i in range(max(0,math.floor(hp/d-2)),hp)])
            smartprint("V factor:",V_factor)
            N=int(sum(C)/hp)
            smartprint("N:",N)
            damage_killed_count=N*d
            damage_killed_cum=int(V_factor*N+d*hp*N*(N-1)/2)
            smartprint("Dam ALT: ",damage_killed_count)
            smartprint("Dam cum ALT: ",damage_killed_cum)
        #     damage_killed_count=0
        #     damage_killed_cum=0
        # for c in C:
        #     for i in range(c):
        #         damage_killed_count+=Vdnocum(i%hp)
        #         damage_killed_cum+=damage_killed_count
        smartprint("DAM:",damage_killed_count)
        smartprint("DAM CUM:",damage_killed_cum)
        D1=(sum(C)-1)*sum(A)-damage_killed_cum
        smartprint("D1:",D1)
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
            # base_power=max([max(i) for i in Attack_list])+1
            # def evaluate(attack,max_len):
            #     return -1 if not attack else sum([attack[i]*math.pow(base_power,max_len-i) for i in range(len(attack))])
            smartprint("maxlen: ",max([len(i) for i in Attack_list]))
            max_len=max([len(i) for i in Attack_list])
            while sum([len(i) for i in Attack_list])>1:
                # Value_attacks=[evaluate(a,max_len) for a in Attack_list]
                # max_val = max(Value_attacks)
                # max_idx = Value_attacks.index(max_val)
                max_idx=Attack_list.index(max(Attack_list))
                damage_killed_count+=Attack_list[max_idx][0]
                damage_killed_cum+=damage_killed_count
                n_attacks_stage2+=1
                Attack_list[max_idx].pop(0)
                smartprint("attack stage 2: ",n_attacks_stage2,"attacking stack n:",max_idx)
                smartprint(Attack_list)
        D2=(sum(C)+n_attacks_stage2)*sum(A)-damage_killed_cum        
        # print((sum(C)+len(M_pos)-1))
    #    write_output()
        smartprint("test n: ",test_n,"solution: ",solution,"calculated sol:",int(D2+1),"difference:",solution-D2-1)
        if solution-D2-1!=0:
            count_wrong+=1
    print("input_file:",input_file_txt," total wrong: ",count_wrong)
    return 0

def iterator(start,end):
    for j in range(start,end):
        input_file_txt="input"+str(j)+".txt"
        output_file_txt="output"+str(j)+".txt"
        #input = sys.stdin.readline
        main(input_file_txt,output_file_txt)
    return 0


iterator(1,12)
# main("input.txt","output.txt")
print("finito!")
    
