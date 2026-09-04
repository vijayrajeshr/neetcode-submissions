class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            key="".join(sorted(i))
            if key in map:
                map[key].append(i)
            else:
                map[key]=[i]
        
        return list(map.values())