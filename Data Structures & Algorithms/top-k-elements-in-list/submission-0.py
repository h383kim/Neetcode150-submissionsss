class Solution(object):
    def topKFrequent(self, nums, k):
        count_dict = {}
        output = []
        for i in nums:
            value = count_dict.get(i)
            if value is not None:
                count_dict[i] = value + 1
            else:
                count_dict[i] = 1
        
        for i in range(k):
            max_count = max(count_dict.values())
            max_key = 0
            for key, value in count_dict.items():
                if value == max_count:
                    max_key = key
                    output.append(max_key)
                    break

            del count_dict[max_key]
        
        return output
