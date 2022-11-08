

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


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(prod_of_array_excp_self(nums))  # [24,12,8,6]
