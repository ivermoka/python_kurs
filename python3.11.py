tall1: int = int(input("Tall 1: "))
tall2: int = int(input("Tall 2: "))

def calculator(tall1, tall2) -> int:
    operator: str = input("Operator: ")
    match operator:
        case "/":
            return tall1 / tall2
        case "*":
            return tall1 * tall2
        case "//":
            return tall1 // tall2
        case "%":
            return tall1 % tall2
        case default:
            print("Method not allowed.")
            return

print(calculator(tall1, tall2))


        
        