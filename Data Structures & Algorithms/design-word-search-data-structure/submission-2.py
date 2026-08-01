class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(root, word):
            cur = root
            for i, c in enumerate(word):
                if c != '.':
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                else:
                    res = []
                    for child in cur.children.values():
                        res.append(dfs(child, word[i+1:]))
                    return any(res)
            return cur.endOfWord
        
        return dfs(self.root, word)
                
