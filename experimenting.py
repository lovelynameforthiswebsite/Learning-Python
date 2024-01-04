# ask the user's name and say hello to them, use defs
def main():
    name = input("what's your name ? ").title().strip()
    hello(name)



def hello(to):
    print("hello", to)

main()






