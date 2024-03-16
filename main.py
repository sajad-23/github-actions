

class Main:
    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name
    def __str__(self) -> str:
        return f'You are {self.name} and your id is {self.id}'




if __name__ == '__main__':
    x = Main(1, 'Mohammed')
    print(x)