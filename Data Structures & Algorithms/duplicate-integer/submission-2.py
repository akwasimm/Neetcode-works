class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for _ in nums:
            if _ in check:
                return True
            else:
                check.add(_)
        return False
        