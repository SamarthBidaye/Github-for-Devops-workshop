# Given an array A of length N and an integer B. You have to check if there are 2 numbers present in the array whose sum is equal to B. You have been provided with the pseudocode, please write the proper code in the language of your choice.

# Note: Same indexed element can't be considered twice

# A=[1,2,2,6,7]
# B=5
# flag=False
# for i in range(len(A)):
#     for j in range(i+1,len(A)):
#         if(A[i]+A[j]==B):
#             print("Bulls Eye",A[i],A[j])
#             flag = True
# if not flag:
#     print("Nothing Found")


# Given an array A of length N, task is to reverse the array. You have been provided with the pseudocode, please write the proper code in the language of your choice

# A=[1,2,2,6,7]
# RevArray=A[::-1]
# print(RevArray , A)

# Suppose you are given a group of N students, and you want to reward the top two students with the highest scores. You have their scores in an array A. Your task is to find the sum of the highest and second-highest scores among the group.

# A=[10,20,30,40,50]
# higest=0
# secondhigh=0
# sum=0
# for i in A:
#     if i>higest:
#         secondhigh=higest
#         higest=i
#     elif i>secondhigh:
#         secondhigh=i
# sum=higest+secondhigh
# print(sum)



# Remove Duplicates
a=set([1,1,1,1,2,2,4,4,6,7,8,9,3,3])
print(a)

