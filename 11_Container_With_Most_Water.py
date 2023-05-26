class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        start=0
        end=len(height)-1
        while start < end:
            if height[start] < height[end]:
                if area < (end-start) * height[start]:
                    area = (end-start) * height[start]
                start += 1
            else:
                if area < (end-start) * height[end]:
                    area= (end-start) * height[end]
                end -= 1
        return area

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         area=0
#         start=0
#         end=len(height)-1
#         while start < end:
#             area = max(area, (end-start) * min(height[start],height[end]))
#             if height[start] < height[end]:
#                 start += 1
#             else:
#                 end -= 1
#         return area