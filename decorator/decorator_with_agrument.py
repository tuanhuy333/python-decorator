def decorator_with_agrument(function):
    def wrapper_accepting_agruments(arg1,arg2):
        print("Input Agrument {0},{1}".format(arg1,arg2))
        function(arg1,arg2)
    return wrapper_accepting_agruments