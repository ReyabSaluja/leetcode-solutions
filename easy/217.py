class Solution(object):
    def containsDuplicate(self, nums):
        distinct = set()
        for num in nums:
            if num in distinct:
                return True
            distinct.add(num)
        return False
