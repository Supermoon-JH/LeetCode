class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2
        # nums1.sort()

        m_idx = m - 1
        n_idx = n - 1
        right = m + n - 1

        while n_idx >= 0:
            if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
                nums1[right] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[right] = nums2[n_idx]
                n_idx -= 1
            
            right -= 1