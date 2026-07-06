class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # to return the array 'strs' as sublists;   

        my_dict = {}

        for i in strs:
            # Fix: Sort letters and join them into a string key
            key = "".join(sorted(i))
            
            # If the key is already there, add the word to that list
            if key in my_dict:
                my_dict[key].append(i)
            # Otherwise, create a new list for that key
            else:
                my_dict[key] = [i]

        # Return just the groups (the values inside the dictionary)
        return list(my_dict.values())