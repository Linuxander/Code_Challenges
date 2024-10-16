class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Verify arguments are same length
        if len(s) != len(t):
            return False

        # Verify sets are same length
        s_set = set(s)
        t_set = set(t)
        if len(s_set) != len(t_set):
            return False

        # Verify both sets have same chars
        for char in s_set:
            if char not in t_set:
                return False

        # Verify char counts are equal in original arguments
        s_dict_comp = {str(char): s.count(char) for char in s_set}
        t_dict_comp = {str(char): t.count(char) for char in t_set}
        allCharCountsAreEqual_boolAr = [False if s_dict_comp[elem] != t_dict_comp[elem] else True for elem in s_dict_comp]
        if False in allCharCountsAreEqual_boolAr:
            return False

        return True
