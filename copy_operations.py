"""
    This is for Assignment OOP 4.1 Shallow and Deep Copy Operations
"""

import copy

nested_list = [[1, 2, 3], [4, 5, 6]]

shallow_nested_copy = copy.copy(nested_list)

deep_nested_copy = copy.deepcopy(nested_list)

shallow_nested_copy[0] = [1, 200, 3]
deep_nested_copy[1][1] = 500

print(f"Original Nested List: {nested_list}")
print(f"Shallow Copied List: {shallow_nested_copy}")
print(f"Deep Copied List: {deep_nested_copy}")

print("\nExplanation:")
print("- The original list (nested_list) does not get modified\n")
print("- The shallowed copied list (shallow_nested_copy) does get modified\nit can change the original list (ex: shallow_nested_copy[0][1] = 200)\nThis would refference and modify the original list as well as the copied list\nWhereas, (shallow_nested_copy[0] = [1, 200, 3]) only changes the copied list\n")
print("- The deep copied list creates different references from the original list\nThis allows us to modify the list without modifying the original list")
