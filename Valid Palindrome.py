import re
def isPalindrome(s: str) -> bool:
  ls = re.sub('[^a-zA-Z0-9]','', s)
  print(ls)
  n = len(ls)
  for i in range(int(n/2)):
    if ls[i].lower() != ls[n-i-1].lower():
      return False
  return True

print(isPalindrome("ab-a"))
