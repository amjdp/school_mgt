class Operation:
    def add(self,inp1,inp2):
        if type(inp1) == str and type(inp2) == str:

          result = inp1 + inp2
          print('Result after concatenation is ',result)

        elif type(inp1) == int and type(inp2) == int:

          result = inp1 + inp2
          print('Result after addition is ',result)

        else :
          print('Invalid input')

    # def add(self,str1,str2):
    #     result = str1 + str2
    #     print('Result after concatenation is ',result)

obj = Operation()

obj.add(5,10)

obj.add('athira','M J')

obj.add(1,'a')