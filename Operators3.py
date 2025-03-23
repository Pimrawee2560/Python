p = True
q = False

a1 = p and q #และ T and T =T  /  F and F = F /T and F =F
print(a1) #false

a2 = p or q #หรือ T or F = T  / F or T = T / T or T =F
print(a2) #True

a3 = not p #ตรงข้าม not T = F   / not F = T
print(a3) # false