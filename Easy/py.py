# # n=int(input())
# # dict={}
# # for i in range(n):
# #     name=input()
# #     if name not in dict:
# #         print("OK")
# #         dict[name]=0
# #     else:
# #         dict[name]+=1
# #         dict[name+str(dict[name])]=0
# #         print(name+str(dict[name]))

# #problem2
# n=int(input())
# occ=1
# L=[]
# L1=[]
# for i in range(n):
#     L.append(int(input()))
#     L1.append(int(i))   
# L2=[]
# L3=[]
# for i in range(n):
#     L2=L[i:]    
#     if L2[i] not in L3:
#             L3.append(L2[i])
#             occ+=1
#     else:
#          occ=1        
#     print(len(L3))
#     print(occ)


n,m=map(int,input().split())
t = list(map(int, input().split()))
for _ in range(m):
    index=int(input())
    print(len(set(t[index:])))