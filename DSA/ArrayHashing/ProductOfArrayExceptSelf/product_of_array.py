
# https://leetcode.com/problems/product-of-array-except-self/S

"""
    [1, 2, 3, 4]
    1. Calculate all prefixes in array
        - product of all nums up to including index
           prefix =  [1, 2, 6, 24]
 
    2. Calculate all postfixes
        - same as prefix except reverse
            postfix = [24, 24, 12, 4]

    3. Calculate output as:
       prefix of previous index * postfix of next index
       (Assume 1 for pre prefix and post postfix) [1[1,2,6,24]] [24,24,12,4]1]

    4. To save memory, calculate prefix in output array,
        but start with imaginary '1' prefix to
        shift values to right to match prefix without 
        including self index. (Put prefix in output, then increment)

        for length of input:
            a. Start with prefix 1
            b. Put prefix in output array
            c. Increment (*=) prefix by multiplying by current value

        Then calculate postfix starting with imaginary '1'
        and multiply by current stored value in ouput to 
        calcualte actual output.

        for length of input, going reverse:
                a. start with postfix 1
                b. Increment (*=) output by multiplyig by current postfix
                c. Increment (*=) postfix by multiplying by current value
            
"""


def prod_of_array_excp_self(nums):
    # Time: O(n)
    output = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output


def productExceptSelf_onePass(nums):
    # Time: O(n), one pass

    # Calculate prefixes starting with front of array
    # Calculate postfixes starting with end of array
    # After they overlap, will create desired output
    output = [1] * (len(nums))
    prefix = 1
    postfix = 1

    for i in range(len(nums)):
        # Calculate prefixes starting with front of array
        # Calculate prefix in output by multiplying by current prefix
        output[i] *= prefix
        # Update prefix by multiplying by current num in array
        prefix *= nums[i]

        # Calculate postfixes starting with end of array
        output[-1-i] *= postfix
        postfix *= nums[-1-i]
    return output


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(prod_of_array_excp_self(nums))  # [24,12,8,6]
    print(productExceptSelf_onePass(nums))
