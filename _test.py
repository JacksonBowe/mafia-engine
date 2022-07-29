class A:
    def __init__(self) -> None:
        self.visited = []
        pass
    
    def visit(self, target):
        self.visited.append(target)
    
class B:
    def __init__(self) -> None:
        self.events = []
        pass
    
    def track(self, target):
        self.events.append(target.visited)    


a = A()
b = B()

b.track(a)

a.visit(b)

print(b.events)
