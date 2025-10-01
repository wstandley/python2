"""
    This is for Assignment OOP 5.1 Metaprogramming
"""

"""
    'WaterFlowsEvaporates' is taken as first argument to take name of class
    The 2nd argument is to inherit from other classes, in this case it inherits from 'objects'
    The 3rd argument defines any methods for the instances of the class as a dictionary
"""
WaterFlowsEvaporates = type('WaterFlowsEvaporates', (object,), {'flows': lambda self: 'Water flows', 'evaporates': lambda self: 'water Evaporates'})

ocean = WaterFlowsEvaporates() # Create instances of class
rivers = WaterFlowsEvaporates()

# Call instances to print
print(ocean.flows())
print(ocean.evaporates())

print(rivers.flows())
print(rivers.evaporates())