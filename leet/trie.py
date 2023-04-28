class TrieNode:
    def __init__(self):
        self.val = False
        self.children = dict()

    def __str__(self) -> str:
        return f"val={self.val}, children={self.children}"


class Trie:
    def __init__(self):
        self.nodes = dict()

    def insert(self, word: str) -> None:
        i = 0
        currNode = []
        if word[i] in self.nodes:
            currNode.append(self.nodes.get(word[i]))
            while len(currNode) > 0:
                node = currNode.pop()
                i += 1
                if i < len(word) and word[i] in node.children:
                    currNode.append(node.children[word[i]])
                else:
                    currNode.append(node)
                    break
        else:
            self.nodes[word[i]] = TrieNode()
            currNode.append(self.nodes[word[i]])
            i += 1
        while i < len(word):
            node = currNode.pop()
            node.children[word[i]] = TrieNode()
            currNode.append(node.children.get(word[i]))
            i += 1
        node = currNode.pop()
        node.val = True

    def search(self, word: str) -> bool:
        i = 0
        currNode = []
        if word[i] in self.nodes:
            currNode.append(self.nodes.get(word[i]))
        else:
            return False
        i += 1
        while i < len(word):
            node = currNode.pop()
            if word[i] in node.children:
                currNode.append(node.children[word[i]])
                i += 1
            else:
                return False
        return currNode.pop().val if currNode is not None else False

    def startsWith(self, prefix: str) -> bool:
        i = 0
        currNode = []
        print(prefix[i], self.nodes)
        if prefix[i] in self.nodes:
            currNode.append(self.nodes.get(prefix[i]))
        else:
            return False
        i += 1
        while i < len(prefix):
            node = currNode.pop()
            if prefix[i] in node.children:
                currNode.append(node.children[prefix[i]])
                i += 1
            else:
                return False
        return True


trie = Trie()
# trie.insert("apple")
# trie.insert("application")
# trie.insert("banana")
# trie.insert("ape")
# trie.insert("animal")
# trie.insert("balance")
# print(trie.search("app"))
# print(trie.search("apple"))
# print(trie.search("ap"))
# print(trie.search("application"))
# print(trie.search("ban"))
# print(trie.search("ball"))
# print(trie.search("balance"))
# print(trie.search("ape"))
# print(trie.search("banana"))
# print(trie.startsWith("app"))
# print(trie.startsWith("apple"))
# print(trie.startsWith("ap"))
# print(trie.startsWith("application"))
# print(trie.startsWith("ban"))
# print(trie.startsWith("ball"))
# print(trie.startsWith("balance"))
# print(trie.startsWith("ape"))
# print(trie.startsWith("banana"))
print(trie.startsWith("a"))

