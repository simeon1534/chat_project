from cryptography.fernet import Fernet

DISCONNECT_MESSAGE = "!DISCONNECT"

key = b'8tqWJ5x5fH9Dqq5ecj8lHyIaLdNbuTHkPv-wN_zDRN8='
cipher_suite = Fernet(key)

encrypted_message = cipher_suite.encrypt(b"DISCONNECT_MESSAGE")
print(encrypted_message)


# n = int(input("Enter the number of rows: "))
#
# for i in range(0, n, 1):
#
#     for j in range(0,n-1):
#         print(' ',end='')
#
#     # spaces = ' '*(n - i)
#     # result = spaces + '*' + spaces
#     # print()

#
# n = int(input("Enter the number of rows: "))
#
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# class Solution:
#     def romanToInt(self, s: str):
#         roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#         res = 0
#         skip = False
#         for i in range(0,len(s)):
#
#             if skip:
#                 skip=False
#                 continue
#             if i + 1 != len(s): # if not out of range of the list
#                 if roman_letters[s[i]] >= roman_letters[s[i+1]]:
#                     res += roman_letters[s[i]]
#
#
#                 else:
#                     # exception logic -  IV,IX etc.
#                     res += roman_letters[s[i+1]] - roman_letters[s[i]]
#                     skip = True
#             else:
#                 res += roman_letters[s[i]]
#
#         return res
#
# s = Solution()
# print(s.romanToInt('III'))
# print(s.romanToInt("LVIII"))
# print(s.romanToInt('MCMXCIV'))

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         res = nums1 + nums2
#         res.sort()
#         while len(res) > 2:
#             res.pop(0)
#             res.pop(-1)
#         return sum(res) if len(res)==1 else sum(res)/2
#         if len(res) % 2 == 0:
#             while len(res) > 2:
#                 res.pop(0)
#                 res.pop(-1)
#             return float((res[0]+res[1]) /2)
#         else:
#             while len(res)>1:
#                 res.pop(0)
#                 res.pop(-1)
#             return float(res[0])
#
# s = Solution()
# print(s.findMedianSortedArrays([1,3],[2]))


# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
#

# class Solution:
#     def cloneGraph(self, adjList):
#         graph = []
#         idx = 1
#         for el in adjList:
#             graph.append(Node(idx, el))
#             idx += 1
#         res = []
#         for n in graph:
#             res.append(n.neighbors)
#         return res
# 
#
# adjList =  [[2,4],[1,3],[2,4],[1,3]]
# s = Solution()
# print(s.cloneGraph(adjList))

# def my_sorting_algo(lst):
#     import copy
#     input_list = copy.deepcopy(lst)
#     # [ 8 , 5 , 6 , 2 , 3]
#     new_sorted_lst = []
#     while input_list:
#         min_n = min(input_list)
#         new_sorted_lst.append(min_n)
#         input_list.remove(min_n)
#     return new_sorted_lst
#
# print(my_sorting_algo([8,2,6,2,3]))

# a =[1,2,3]
# b = a
# b.pop()
# print(a)

# def pow2(x , n):
#
#     if n==1:
#         return x
#     if n==0:
#         return 1
#     return x * pow2(x, n-1)
# print(pow2(2,2))
#
# def classic_pow(x, n):
#     sum = 1
#     for i in range(1,abs(n)+1):
#         sum*=x
#     return sum if n>=0 else 1/sum
#
# print(classic_pow(0.00001,2147483647))
# print(pow2(0.00001,2147483647))


# def minimizeArrayValue(nums):
#     #[3,8,10,12,20]
#     sumlist = sum(nums)
#
#     each_element = sumlist // len(nums)
#     ostatyk = sumlist % len(nums)
#     res = []
#     for i in range(0,len(nums)):
#         res.append(each_element)
#     while ostatyk:
#         for i in range(0,len(nums)):
#             res[i]+=1
#             ostatyk-=1
#             if ostatyk ==0:
#                 break
#     return res
# def min_max_num(nums):
#     left, right = 1, max(nums)
#     while left <= right:
#         mid = (left + right) // 2
#         ops = sum(max(num - mid, 0) for num in nums)
#         if ops > mid:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left
# nums = [10,1]
# print(minimizeArrayValue(nums))

# if max_num doesnt change break we reached limit
# for idx in range(1,len(nums)+1):

# index and value >=1

# class Solution:
#     # [[1, 1, 1, 1, 1, 1, 1, 0],
#     # [1, 0, 0, 0, 0, 1, 1, 0],
#     # [1, 0, 1, 0, 1, 1, 1, 0],
#     # [1, 0, 0, 0, 0, 1, 0, 1],
#     # [1, 1, 1, 1, 1, 1, 1, 0]]
#     def closedIsland(self, grid) -> int:
#
#         visited = []
#         stack = []
#
#         def dfs(row_idx,col_idx):
#             # check adjacent elements
#
#             up = grid[row_idx - 1][col_idx] if row_idx > 0 else None
#             down = grid[row_idx + 1][col_idx] if row_idx < len(grid) - 1 else None
#             left = grid[row_idx][col_idx - 1] if col_idx > 0 else None
#             right = grid[row_idx][col_idx + 1] if col_idx < len(grid[0]) - 1 else None
#
#             visited.append([row_idx, col_idx])
#             if up is not None and up != 1 and up is not visited:
#                 stack.append([row_idx - 1, col_idx])
#
#             if down is not None and down != 1 and down is not visited:
#                 stack.append([row_idx + 1, col_idx])
#
#             if left is not None and left != 1 and left is not visited:
#                 stack.append([row_idx, col_idx - 1])
#
#             if right is not None and right != 1 and right is not visited:
#                 stack.append([row_idx, col_idx + 1])
#             if stack:
#                 visited.append(stack.pop(-1))
#                 dfs(visited[-1][0],visited[-1][1])
#             return visited
#         for row_idx in range(0, len(grid)):
#             for col_idx in range(0, len(grid[row_idx])):
#
#                 if grid[row_idx][col_idx] is not visited and grid[row_idx][col_idx] == 0:
#
#
#
#
# grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 0]]
#
# s = Solution()
# s.closedIsland(grid)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        for el_s, el_t in zip(s, t):
            idx_s = []
            idx_t = []
            for i in range(len(s)):
                if len(idx_s) == s.count(el_s):
                    break
                if s[i] == el_s:
                    idx_s.append(i)
            for i in range(len(t)):
                if len(idx_t) == t.count(el_t):
                    break
                if t[i] == el_t:
                    idx_t.append(i)
            if idx_s != idx_t:
                return False
        return True


s = 'AAABBBBA'
t = 'BBBAAAAB'
solution = Solution()
print(solution.isIsomorphic(s, t))
