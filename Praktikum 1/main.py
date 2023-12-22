class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def update_value(self, index, value):
        index += self.size
        self.tree[index] = value

        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        result = 0

        while left < right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1

            if right % 2 == 1:
                right -= 1
                result = max(result, self.tree[right])

            left //= 2
            right //= 2

        return result

# Fungsi untuk mencari panjang dari Largest Monotonically Increasing Subsequence.
def longest_increasing_subsequence_length(nums):
    n = len(nums)
    index_mapping = {num: i for i, num in enumerate(sorted(set(nums)))}
    segment_tree = SegmentTree(len(index_mapping))
    lis_lengths = [0] * n

    for i, num in enumerate(nums):
        index = index_mapping[num]
        lis_lengths[i] = segment_tree.query(0, index) + 1
        segment_tree.update_value(index, lis_lengths[i])

    return max(lis_lengths)


nums = [4, 1, 13, 7, 0, 2, 8, 11, 3] 
result = longest_increasing_subsequence_length(nums)
print("Panjang Largest Monotonically Increasing Subsequence :", result)
