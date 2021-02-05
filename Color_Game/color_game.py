def retrieve_color_items_subscribed(color):
    for item in items[color]:
        if item in current:
            if item == 'frog':
                print("I'm Frog! I am", color, "today!")
            else:
                print("I'm ",item,"! I'm sometimes ",color,"!",sep='')


items = {'red': ['book', 'apple', 'ink'],
         'blue': ['sky', 'frog'],
         'green': ['banana', 'apple'],
         'yellow': ['banana', 'frog'],
         'black': ['sky', 'ink'],
         'white': ['salt']}

current = []

curr_input = input().strip()
while curr_input != 'exit':
    if curr_input == 'list':
        print(current)
    elif curr_input in items.keys():
        retrieve_color_items_subscribed(curr_input)
    elif curr_input[0] == '+':
        current.append(curr_input[1:])
    elif curr_input[0] == '-':
        current.remove(curr_input[1:])
    else:
        print('Error: Invalid Token Detected! Please retry')
    curr_input = input().strip()
