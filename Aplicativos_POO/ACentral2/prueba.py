import copy

original = [1, 2, [3, 4], 5]

# Copia superficial
copia_superficial = copy.copy(original)

# Copia profunda
copia_profunda = copy.deepcopy(original)

print(copia_superficial)
print(copia_profunda)
