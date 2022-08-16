def decorator_with_arbitrary_agrument(func_to_decorate):
    def wrapper_acepting_arbitrary(*args,**kwargs):
        print("The positional arguments are", args)
        print("The keyword arguments are", kwargs)
        func_to_decorate(*args)
    return wrapper_acepting_arbitrary


