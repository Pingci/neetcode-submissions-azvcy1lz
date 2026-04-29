class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()

            cur = cur.child[c]

        cur.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.child.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.child:
                        return False

                    cur = cur.child[c]

            return cur.isWord

        return dfs(0, self.root)

                
