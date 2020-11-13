def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  if (to_find in lst):
      return lst.index(to_find)
  else:
    return -1


print(linear_search([1], 1))
