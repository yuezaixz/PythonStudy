class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens : return -1
        operator = ["+","-","*","/"]
        operatorStack = []
        for operStr in tokens:
            if operStr in operator :
                if len(operatorStack) < 2 : return -1
                result = None
                two = operatorStack.pop()
                one = operatorStack.pop()
                if operStr == '+': result = one + two
                if operStr == '*': result = one * two
                if operStr == '-': result = one - two
                if operStr == '/': result = -((-one)/two) if one*two < 0 else one/two
                operatorStack.append(result)
            else:
                operatorStack.append(int(operStr))
        return operatorStack[0]

if __name__ == '__main__':
    print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])