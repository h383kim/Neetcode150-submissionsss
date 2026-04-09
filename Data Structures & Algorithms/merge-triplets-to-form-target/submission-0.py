from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        gota = False
        gotb = False
        gotc = False
        
        for triplet in triplets:
            ai, bi, ci = triplet
            if ai > a or bi > b or ci > c:
                continue
            
            if ai == a: gota = True
            if bi == b: gotb = True
            if ci == c: gotc = True

        return (gota and gotb and gotc)
