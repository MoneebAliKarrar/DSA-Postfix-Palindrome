from Stack import Stack
from LinkedList import *

def infix_to_postfix(expression):
    precedence = {'*': 1, '/': 1, '+': 2, '-': 2, '(': 0}
    output = []
    operator_stack = Stack(len(expression))

    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
            num = []
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num.append(expression[i])
                i += 1 
            tokens.append(''.join(num))
            continue
        elif expression[i] in '+*/()':
            tokens.append(expression[i])
        elif expression[i] == '-':
            if i == 0 or expression[i-1] in '+-*/(':
                num = ['-']
                i += 1
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num.append(expression[i])
                    i += 1
                tokens.append(''.join(num))
                continue
            else:
                tokens.append('-')
        i += 1

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            output.append(token)
        if token.startswith('-'):
            token.replace('-','',-1).isdigit()
            output.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top_token = operator_stack.pop()
            while top_token != '(':
                output.append(top_token)
                top_token = operator_stack.pop()
        elif token in '+*/()':  # The token is an operator
            while (not operator_stack.isempty()) and (precedence[operator_stack.top()] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.isempty():
        output.append(operator_stack.pop())

    return ' '.join(output)

def evaluate_postfix(expression):
    operand_stack = Stack(len(expression))
    tokens = expression.split()

    for token in tokens:
        if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
            operand_stack.push(token)
        else:
            val1 = float(operand_stack.pop())
            val2 = float(operand_stack.pop())
            if token == '+':
                operand_stack.push(str(val2 + val1))
            elif token == '-':
                operand_stack.push(str(val2 - val1))
            elif token == '*':
                operand_stack.push(str(val2 * val1))
            elif token == '/':
                operand_stack.push(str(val2 / val1))

    return float(operand_stack.pop())

def PalindromeEvaluator(expression):
    stringStack = Stack(len(expression))
    linkedList = string_to_singly_linked_list(expression)
    for char in expression:
        stringStack.push(char)
    item_cur = linkedList.head
    while item_cur:
        if item_cur.data != stringStack.pop():
            return False
        item_cur = item_cur.next
    return True 


if __name__ == "__main__":
    expression = input("Enter an infix expression: ")
    print("Infix expression:", expression)
    postfix_expression = infix_to_postfix(expression)
    print("Postfix expression:", postfix_expression)
    result = evaluate_postfix(postfix_expression)
    print("the value is :", result)
    
    '''
    expression = input("Enter expression to evaluate if palindrome: ")
    palindrome = PalindromeEvaluator(expression)
    print(palindrome)
    '''
