class Items:
    def post(self):
        pass


class NormalItems(Items):
    def __init__(self, name):
        self.name = name

    def post(self, color):
        print("I'm ", self.name, "! I'm sometimes ", color, "!", sep='')


class SpecialItems(Items):
    def __init__(self, name):
        self.name = name

    def post(self, color):
        print("I'm ", self.name, "! I'm ", color, " today!", sep='')


book = NormalItems('book')
apple = NormalItems('apple')
ink = NormalItems('ink')
banana = NormalItems('banana')
sky = NormalItems('sky')
salt = NormalItems('salt')
frog = SpecialItems('frog')

items = {'red': [book, apple, ink],
         'blue': [sky, frog],
         'green': [banana, apple],
         'yellow': [banana, frog],
         'black': [sky, ink],
         'white': [salt]}

current = []


def retrieve_color_items_subscribed(color):
    for item in items[color]:
        if item.name in current:
            item.post(color)


def run_command(command):
    if command == 'list':
        print(current)
    elif command in items.keys():
        retrieve_color_items_subscribed(command)
    elif command[0] == '+':
        current.append(command[1:])
    elif curr_input[0] == '-':
        current.remove(command[1:])
    else:
        print('Error: Invalid Token Detected! Please retry')

curr_input = input().strip()
while curr_input != 'exit':
    run_command(curr_input)
    curr_input = input().strip()
