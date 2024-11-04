class Calculator:
    
    # def add(self, a, b):
    #     return a + b
    def add(self, a, b):
        return a + b
# =============================================================================
    # def subtract(self, a, b):
    #     return b - a
    def subtract(self, a, b):
        return a - b
# =============================================================================
    # def multiply(self, a, b):
    #     result = 0
    #     for i in range(b+1):
    #         result = self.add(result, a)
    #     return result
    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result
# =============================================================================
    # def divide(self, a, b):
    #     result = 0
    #     while a > b:
    #         a = self.subtract(a, b)
    #         result += 1
    #     return result
    def divide(self, a, b):
        if b == 0:
            return ("Cannot div by zero")
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    # อธิบายการทำงานของ divide
    # ex. 8 / 4
    # 8 / 4
    # 8 - 4 = 4
    # 4 - 4 = 0
    # 2
    
    # ex. 8 / 3
    # 8 / 3
    # 8 - 3 = 5
    # 5 - 3 = 2
    # 2 - 3 = -1
    # 2

# =============================================================================    
    # def modulo(self, a, b):
    #     while a <= b:
    #         a = a-b
    #     return a
    def modulo(self, a, b):
        if b == 0:
            return ("Cannot mod by zero")
        while a >= b:
            a = self.subtract(a, b)
        return a

    # อธิบายการทำงานของ modulo
    # ex. 8 % 4
    # 8 % 4
    # 8 - 4 = 4
    # 4 - 4 = 0
    
    # ex. 8 % 3
    # 8 % 3
    # 8 - 3 = 5
    # 5 - 3 = 2
    # 2 - 3 = -1
    # 2 
# =============================================================================
# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))