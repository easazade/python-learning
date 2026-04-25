# since python is a dynamic type language all below values will return false
# 0
# ""
# []
# None (null)
# everything else is true including "False"

flag = True

print(bool(0))
print(bool([]))
print(bool(""))
print(bool(None))
print("##############")
print(bool("False"))  # returns true
print(bool(-1))  # returns true
