# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        val = list(str(x))
        left, right = (1 if val[0] == "-" else 0), len(val) - 1

        while left < right:
            val[left], val[right] = val[right], val[left]
            left += 1
            right -= 1

        result = int("".join(val))

        if result > 2**31 - 1 or result < -(2**31):
            return 0

        return result


print(Solution().reverse(123))
print(Solution().reverse(-123))
