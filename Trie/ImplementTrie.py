class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ALPHABET_SIZE = 26
        self.children = [None] * self.ALPHABET_SIZE
        self.isEndOfWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            self.isEndOfWord = True
            return
        idx = ord(word[0]) - ord('a')
        if self.children[idx]:
            self.children[idx].insert(word[1:])
        else:
            self.children[idx] = Trie()
            self.children[idx].insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            if self.isEndOfWord:
                return True
            else:
                return False
        idx = ord(word[0]) - ord('a')
        if self.children[idx]:
            return self.children[idx].search(word[1:])
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        idx = ord(prefix[0]) - ord('a')
        if self.children[idx]:
            return self.children[idx].startsWith(prefix[1:])
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieV1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEndOfWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            self.isEndOfWord = True
            return
        if word[0] in self.children:
            self.children[word[0]].insert(word[1:])
        else:
            self.children[word[0]] = Trie()
            self.children[word[0]].insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            if self.isEndOfWord:
                return True
            else:
                return False
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class TrieV2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEndOfWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = Trie()
            root = root.children[c]
        root.isEndOfWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.isEndOfWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self
        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True
