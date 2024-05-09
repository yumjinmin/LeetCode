class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)-2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]: # 축에 대한 문제
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # 스킵 처리
                    while left < right and nums[left] == nums[left+1]: 
                        left += 1
                    while left > right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
                
