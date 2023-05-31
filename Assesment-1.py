#<aside>
#💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#**Example:**
#Input: nums = [2,7,11,15], target = 9
#Output0 [0,1]

#**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][

#</aside>

def twoSum(nums, target):
    complement_map = {}  # Dictionary to store complements
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i

    return []
    
    
nums = [2,7,11,15]
target = 9

result = twoSum(nums, target)
print(result)

[0, 1]


#<aside>
#💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#- Return k.

#**Example :**
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_*,_*]

#**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[

#</aside>

def removeElement(nums, val):
    k = 0  # pointer for the next position of non-val elements

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

    nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print(result)  # Output: 2


#<aside>
#💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

#**Example 1:**
#Input: nums = [1,3,5,6], target = 5

#Output: 2

#</aside>


def search_insert(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

nums = [1, 3, 5, 6]
target = 5
print(search_insert(nums, target))  # Output: 2



#<aside>
#💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

#**Example 1:**
#Input: digits = [1,2,3]
#Output: [1,2,4]

#**Explanation:** The array represents the integer 123.

#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4].

#</aside>

def plusOne(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digit_sum = digits[i] + carry
        if digit_sum == 10:
            digits[i] = 0
            carry = 1
        else:
            digits[i] = digit_sum
            carry = 0
    
    if carry == 1:
        digits.insert(0, 1)
    
    return digits

digits = [1, 2, 3]
result = plusOne(digits)
print(result)

#[1, 2, 4]


#<aside>
#💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

#**Example 1:**
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]

#**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
#The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

#</aside>

def merge(nums1, m, nums2, n):
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for the merged array

    # Loop until we process all elements in nums2
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy the remaining elements of nums2 (if any) to nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)

#[1, 2, 2, 3, 5, 6]


#<aside>
#💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#**Example 1:**
#Input: nums = [1,2,3,1]

#Output: true

#</aside>

def containsDuplicate(nums):
    unique_nums = set()
    for nums in nums:
        if nums in unique_nums:
            return True
        unique_nums.add(nums)
    return False
    
nums = [1,2,3,1]
print(containsDuplicate(nums))
#True


#<aside>
#💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

#Note that you must do this in-place without making a copy of the array.

#**Example 1:**
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

#</aside>


def moveZeroes(nums):
    left = 0  # pointer for non-zero elements
    right = 0  # pointer for all elements

    while right < len(nums):
        # If the current element is not zero, swap it with the left pointer
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1  # increment the left pointer

        right += 1  # always increment the right pointer

    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

#[1, 3, 12, 0, 0]


#<aside>
#💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

#You are given an integer array nums representing the data status of this set after the error.

#Find the number that occurs twice and the number that is missing and return them in the form of an array.

#**Example 1:**
#Input: nums = [1,2,2,4]
#Output: [2,3]

#</aside>


def findErrorNums(nums):
    num_set = set()
    duplicate = -1
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    n = len(nums)
    for i in range(1, n + 1):
        if i not in num_set:
            missing = i
            break

    return [duplicate, missing]

nums = [1, 2, 2, 4]
print(findErrorNums(nums))

#[2, 3]


