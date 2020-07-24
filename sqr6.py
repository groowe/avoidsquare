from row import Row
import re
from tqdm import tqdm
import numpy as np
import time
allcount = 0
alllen = 0
allones = 0
side = 0

def show(items):
    string = ''.join(str(i) for i in items)
    try:
        a = np.asarray([int(i) for i in string]).reshape([side,side])
    except:
        return
    print('*'*30)
    print(a)
    print('*'*30)
    return

def recheck(items = []):
    """generalized recheck with regular expression"""
    litems = len(items)
    global comb
    if litems <= 2:
        return True
    string = ''.join(str(i) for i in items)
    if log and (aaa:=''.join([str(item) for item in items])) in comb[litems].keys():
        return comb[litems][aaa]

    for l in range(3,litems+1):
        teststring = string[-side*l:]
        if log and teststring in comb[l].keys():
            if comb[l][teststring] == False:
                return False
            continue
        #print(teststring)
        for i in range(2):
            if l % 2 != 0:
                # 45 square possible
                # 3
                # a = f'^.{{1,{side-2}}}{i}.{{{side-2}}}{i}.{{1}}{i}.{{{side-2}}}{i}'
                # 5
                # c = f'^.{{2,{side-3}}}{i}.{{{side*2-3}}}{i}.{{3}}{i}.{{{side*2-3}}}{i}'
                # 7
                # e = f'^.{{3,{side-4}}}{i}.{{{side*3-4}}}{i}.{{{5}}}{i}.{{{side*3-4}}}{i}'
                a = int(l/2)
                b = side - (a+1)
                c = side * a - (a+1)
                d = l - 2
                if re.search(f'^.{{{a},{b}}}{i}.{{{c}}}{i}.{{{d}}}{i}.{{{c}}}{i}',teststring):
                    if debug:
                        print(f'^.{{{a},{b}}}{i}.{{{c}}}{i}.{{{d}}}{i}.{{{c}}}{i}')
                        show(string)
                    #print(len(comb),len(comb[l]))
                    #print(l,int(teststring,2))
                    if log:
                        #print(a)
                        comb[l][teststring] = False
                    return False
                # 5
                # b = f'^.{{1,{side-4}}}{i}.{{{side+2}}}{i}.{{{side*2-5}}}{i}.{{{side+2}}}{i}'
                # 7
                # a = f'^.{{1,{side-6}}}{i}.{{{side+4}}}{i}.{{{side*4-7}}}{i}.{{{side+4}}}{i}'
                for t in range(1,l-1):
                    if int(l/2) == t:
                        continue
                    # this works with 1
                    b = l - t
                    c = side - b
                    if t*2 < l:
                        #b = l - t #    7 - 1 = 6    7 - 2  = 5  5 - 1 = 4
                        #c = side - b #  7 - (7 - 6) = 1   7 - 5 = 2   5 - 4 = 1
                        d = side * t  + l - 2 - t
                        e = side * (t+1) - l
#                        if re.search(f'^.{{{t},{c}}}{i}.{{{d}}}{i}.{{{e}}}{i}.{{{d}}}{i}',teststring):
#                            return False
                    # 5
                    # b = f'^.{{1,{side-4}}}{i}.{{{side+2}}}{i}.{{{side*2-5}}}{i}.{{{side+2}}}{i}'
                    # this 2 (5 has the exception with 2 value)
                    #a = f'^.{{1,{side-6}}}{i}.{{{side+4}}}{i}.{{{side*4-7}}}{i}.{{{side+4}}}{i}'
                    #c = f'^.{{2,{side-5}}}{i}.{{{side*2+3}}}{i}.{{{side*2-7}}}{i}.{{{side*2+3}}}{i}'
                    else:
                        # 5
                        # a = f'^.{{3,{side-2}}}{i}.{{{side-4}}}{i}.{{{side*2+3}}}{i}.{{{side-4}}}{i}'
                        # 7
                        #d = f'^.{{4,{side-3}}}{i}.{{{side*2-5}}}{i}.{{{side*2+4}}}{i}.{{{side*2-5}}}{i}'
                        #b = f'^.{{5,{side-2}}}{i}.{{{side-6}}}{i}.{{{side*3+4}}}{i}.{{{side-6}}}{i}'
                        #b = l - t
                        #c = side -
                        dd = int(t/2) if t % 2 ==0 else int(t/2)+1
                        d = side * (l-(t+1)) - (t+1)
                        e = side * dd  +int(l/2)+1
                    if re.search(f'^.{{{t},{c}}}{i}.{{{d}}}{i}.{{{e}}}{i}.{{{d}}}{i}',teststring):
                        if log:
                            comb[l][teststring] = False
                        return False

            else:
                for t in range(1,l-1):
                    b = l - t
                    c = side - b
                    if t*2 < l:
                        # 4
                        # b = f'^.{{1,{side-3}}}{i}.{{{side+1}}}{i}.{{{side-4}}}{i}.{{{side+1}}}{i}'
                        # 6
                        # a = f'^.{{1,{side-5}}}{i}.{{{side+3}}}{i}.{{{side*3-6}}}{i}.{{{side+3}}}{i}'
                        # b = f'^.{{2,{side-4}}}{i}.{{{side*2+2}}}{i}.{{{side-6}}}{i}.{{{side*2+2}}}{i}'
                        d = side*t + (b-2)
                        e = side * (b-t-1) - l

                    else:
                        # 4
                        # a = f'^.{{2,{side-2}}}{i}.{{{side-3}}}{i}.{{{side+2}}}{i}.{{{side-3}}}{i}'
                        # 6
                        # d = f'^.{{3,{side-3}}}{i}.{{{side*2-4}}}{i}.{{{side+4}}}{i}.{{{side*2-4}}}{i}'
                        # c = f'^.{{4,{side-2}}}{i}.{{{side-5}}}{i}.{{{side*3+4}}}{i}.{{{side-5}}}{i}'
                        d = side * (l-(t+1)) - (l - (l - (t+1)))
                        e = side * (1 if t * 2 == l else int(l/2))  +l-2
                    if re.search(f'^.{{{t},{c}}}{i}.{{{d}}}{i}.{{{e}}}{i}.{{{d}}}{i}',teststring):
                        if log:
                            #print(a)
                            comb[l][teststring] = False

                        return False
        if log:
            comb[l][teststring] = True
    if log:
        comb[litems][aaa] = True
    return True

def mainsolve(item,count=0,rownum=0,items = []):
    # if not enough ones , abort
    global decsolutions
    global allcount
    if side > 5 and rownum == 0:
        a = f'{int(str(item),2)+1:>{len(str(int("1"*side,2)+1))}}'
        print(a,'/',int('1'*side,2)+1)
    if count + ( side * (side-1-rownum)) < allones:
        return
    if count > allones:
        #print(items,count,allones)
        return
    if rownum +1 >= side and count != allones:
        #print(items,count,allones)
        return
    if not recheck(items):
        return
    #if rownum >= 2 and not recheck(items):
    #    return
    if count == allones and rownum +1 == side:
    #    print(items,count,allones)
        show(items)
        allcount+=1
        decsolutions.append(int(''.join(str(i) for i in items),2))
        return

    if not items:
        items = [item]
    p = item.poss()[0]
    li = len(items)
    for i in p:
        if any(not items[c].isin(i,li-c-1) for c in range(li)):
            continue
        mainsolve(i,i.ones+count,rownum+1,items+[i])
    return
decsolutions = []
comb = []
gsl= 0
combcomb = 0
def main(sidelen = 4):
    global alllen
    global allones
    global side
    global comb
    global gsl
    global r
    global combcomb

    alllen = sidelen**2
    allones = int(alllen/2)
    side = sidelen
    if log and combcomb != sidelen:
        print('creating log')
        comb = [{} for i in range(sidelen+1)]
        combcomb = sidelen
        print('done')
    if gsl != sidelen:


        r = []
        print('generating rows:')
        for i in tqdm(range(2**sidelen)):
            num = f'{bin(i)[2:]:>{sidelen}}'.replace(' ','0')
            r.append(Row(num))
        print('combinating rows:')
        for item in tqdm(r):
            for i in range(2**sidelen):
                item.combine(r[i])
        gsl = sidelen
    #for i in r:
    #    print(i)
    #    print(i.poss())
    print(f'solving {sidelen}*{sidelen}:')
    for a in range(2**sidelen):
        mainsolve(r[a],r[a].ones,0)
debug = False
log = False
#for i in range(2,8):
#    allcount=0
#    main(i)
#    print(i,allcount)
#    input()
#for i in range(3,100):
#    main(i)
"""
for i in range(3,11):
    allcount=0
    main(i)
    print(i,allcount)
    #print(decsolutions)
    input()
"""
repeat = 2
rep = int(repeat / 2)
maxx = 8
for lll in range(3,maxx):
    timeit = []
    for i in tqdm(range(repeat)):
        allcount = 0

        log = i < rep

        t = time.time()
        main(lll)
        timeit.append(time.time() - t)
        print(allcount)
    print(timeit[:rep])
    print(timeit[rep:])
    input()
