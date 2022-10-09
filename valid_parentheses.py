
s = '()'


def check(s):
  para_dict = {')':'(', ']':'[', '}':'{'}
  stack = []
  result = True
  for i in s:
      print(i)
      if i in para_dict.values():
        stack = stack + [i]
        print(stack)
      if i in para_dict.keys():
        if len(stack) > 0:
          if para_dict[i] == stack[-1]:
            print(stack[-1])
            stack = stack[:-1]
            print(stack)
            result = True
          else:
            result = False
            return result
        else:
          result = False
          return result
      if len(stack) > 0:
        result = False
  print(result)
  return result

check(s)
