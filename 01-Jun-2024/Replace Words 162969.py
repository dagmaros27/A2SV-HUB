# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def find(roots, word):
            for root in roots:
                if word.startswith(root):
                    return root
            return None

        dic = defaultdict(list)

        for d in dictionary:
            dic[d[0]].append(d)
        
        for arr in dic:
            dic[arr].sort(key = lambda x: len(x))
        
        words = sentence.split()

        ans = []
        for word in words:
            root = find(dic[word[0]], word)
            if root is not None:
                ans.append(root)
            else:
                ans.append(word)
        
        return " ".join(ans)

        