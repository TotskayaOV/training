import view

def compute():
    num_1, num_2, oper = view.get_value()
    match oper:
        case '+': return(num_1 + num_2)
        case '-': return(num_1 - num_2)
        case '*': return(num_1 * num_2)
        case '/': return(num_1 / num_2)

def compute2(num_1, num_2, oper):
    match oper:
        case '+': return(num_1 + num_2)
        case '-': return(num_1 - num_2)
        case '*': return(num_1 * num_2)
        case '/': return(num_1 / num_2)