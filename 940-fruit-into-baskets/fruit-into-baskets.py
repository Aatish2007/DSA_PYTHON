'''
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n=len(fruits)
        max_fruit=0
        for start in range(n):
            fruit_type=set()
            for end in range(start,n):
                fruit_type.add(fruits[end])
                if len(fruit_type)>2:
                    break
                max_fruit = max(max_fruit, end - start + 1)
        return max_fruit
'''

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        max_fruits=0
        count={}
        for right in range(len(fruits)):
            fruit=fruits[right]
            count[fruit]=count.get(fruit,0)+1
            while len(count)>2:
                left_fruit=fruits[left]
                count[left_fruit]-=1
                if count[left_fruit]==0:
                    del count[left_fruit]
                left+=1
            max_fruits=max(max_fruits,right-left+1)
        return max_fruits