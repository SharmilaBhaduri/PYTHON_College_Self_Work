import inspect

def example_function(python, computer, graphics , networking):
    pass

params = inspect.signature(example_function).parameters
param_names = list(params.keys())

print("The parameter names are:", param_names)