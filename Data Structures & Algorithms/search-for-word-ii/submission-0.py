class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Built the Trie
        root = TrieNode()
        for w in words:
            # Insert the word
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWordEnd = True
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in node.children or (r, c) in visited:
                return False
            visited.add((r, c))
            if node.children[board[r][c]].isWordEnd:
                res.add(word + board[r][c])
            dfs(r + 1, c, node.children[board[r][c]], word + board[r][c])
            dfs(r - 1, c, node.children[board[r][c]], word + board[r][c])
            dfs(r, c + 1, node.children[board[r][c]], word + board[r][c])
            dfs(r, c - 1, node.children[board[r][c]], word + board[r][c])
            visited.remove((r, c))
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return list(res)
