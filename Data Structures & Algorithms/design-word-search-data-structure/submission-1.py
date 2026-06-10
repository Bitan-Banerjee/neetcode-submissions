class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.endOfWord = True
        return
        
    def _search(self, node, word):
        curr = node
        # Scanning the word
        for i in range(len(word)):
            # If a '.' if found, and the trie has children we go inside
            if word[i] == '.' and curr.children:
                # If the '.' is the last char of the word, 
                # and we know that the current node has children, 
                # then the last position can contain any of those children, 
                # so we return True
                if i == len(word) - 1:
                    for ch in curr.children.keys():
                        if curr.children[ch].endOfWord: return True
                    return False

                # when '.' is not the last char
                for ch in curr.children.keys():
                    if self._search(curr, (ch + word[i+1:])):
                        return True
                return False
            
            # When there is no '.' in the word
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.endOfWord 
                


    def search(self, word: str) -> bool:
        curr = self.root
        return self._search(curr, word)

        
