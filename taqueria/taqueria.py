def cst(prompt):
    menu={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    tot=0
    while True:
        try :
            itm=input(prompt).title()
            tot=tot+menu[itm]
            print(f'Total: ${tot:.2f}')
        except KeyError:
            continue
        except EOFError:
            break
def main():
    cst('Item: ')
main()

