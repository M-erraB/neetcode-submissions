class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.current = newNode
        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode
        

    def back(self, steps: int) -> str:
        while steps != 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url
        

    def forward(self, steps: int) -> str:
        while steps != 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1
        return self.current.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)