# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        root = self.root

        for ch in word[::-1]:
            idx = ord(ch) - ord('a')

            if not root.children[idx]:
                root.children[idx] = TrieNode()

            root = root.children[idx]


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        myTrie = Trie()      
        total_length = 0
 
        for word in words:
            myTrie.add(word)

        def dfs(node, l) -> int:
            nonlocal total_length

            for r in node.children:
                if r:
                    dfs(r,l+1)
            
            if all(nbr is None for nbr in node.children):
                total_length += l+1
    


        dfs(myTrie.root,0)

        return total_length

        