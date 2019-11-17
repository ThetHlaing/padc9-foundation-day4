d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  ## Return if the key is existed in the above dictionary "d"
  if x in d.keys():
    print("Key is existed")
  else:
    print("Kye not found")
  return x
is_key_present(5)
is_key_present(9)