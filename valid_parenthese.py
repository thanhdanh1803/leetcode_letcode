def isValid(s: str) -> bool:
        l = []
        d = {'{':'}', '(': ')', '[': ']'}
        for item in s:
            if len(l) == 0 and item not in d:
              return False
            if item in d:
              l.append(d[item])
            else:
                if l.pop() != item:
                    return False
        return len(l) == 0

print(isValid("(){}{}"))