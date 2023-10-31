def count_sheep(sheep):
    cnt=0
    for ele in sheep:
        if ele==True: cnt+=1
    return cnt
sheep=[True, True, False]
print(count_sheep(sheep))


