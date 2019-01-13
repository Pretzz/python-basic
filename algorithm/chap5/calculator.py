#계산기 구현
opStack = []
operatorStack = []
displayStack = []
def inputNumInit():
    print("숫자를 입력하세요 : ")
    op1 = input()
    global opStack
    global displayStack
    opStack.append(op1)
    displayStack.append(op1)
    inputOperator()


def inputNum():
    print("숫자를 입력하세요 : ")
    op1 = input()
    global opStack
    global displayStack
    opStack.append(op1)
    displayStack.append(op1)
    operator = operatorStack.pop()
    if operator == "*" or operator == "/":
        op2 = int(opStack.pop())
        op1 = int(opStack.pop())
        result = calculator(op1,op2,operator)
        opStack.append(result)
    else:
        operatorStack.append(operator)

    print("계속 계산하시겠습니까? Y/N")
    contYn = input()
    if contYn == "Y":
        inputOperator()
    else:
        displayS()
        showResult()

def inputOperator():
    print("사칙연산 기호 입력하세요 : ")
    operator = input()
    global operatorStack
    global displayStack
    operatorStack.append(operator)
    displayStack.append(operator)
    inputNum()

def displayS():
    global displayStack
    print("".join(displayStack))

def showResult():
    global opStack
    global operatorStack
    result = 0;
    if len(operatorStack) == 0:
        result += opStack.pop()
    else:
        while operatorStack:
            op2 = int(opStack.pop())
            op1 = int(opStack.pop())
            result += calculator(op1,op2,operatorStack.pop())

    print("정답:"+str(result))


def calculator(op1,op2,operator):
    if operator == "+":
        return op1+op2
    elif operator == "-":
        return op1-op2
    elif operator == "*":
        return op1*op2
    elif operator == "/":
        return op1/op2


if __name__ == "__main__":
    inputNumInit()



