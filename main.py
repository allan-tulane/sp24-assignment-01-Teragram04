"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x == 0:
      return 0
      
    if x == 1:
      return 1
      
    if x > 1:
      return (foo(x-1) + foo(x-2))
    pass


def longest_run(mylist, key):
    current_run = 0
    longest_run = 0
    for i in range(len(mylist)):
      if mylist[i] == key:
        current_run += 1
      else:
        current_run = 0
      if current_run > longest_run:
        longest_run = current_run
    return longest_run
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  for i in range(len(mylist)):
    if mylist[i] == key:
      return Result(longest_run_recursive(mylist[0:i], key), longest_run_recursive(mylist[i+1:], key), longest_run(mylist, key), False)
  else:
    return Result(0, 0, 0, True)




