def decorator_make_with_agruments(dec_arg1, dec_arg2, dec_arg3):
    def decorator(func):
        def wrapper(func_arg1, func_arg2, func_arg3):
            print("The wrapper can access all the variables\n"
                  "\t- from decorator:{0},{1},{2}\n"
                  "\t- from func:{3},{4},{5}\n"
                  .format(dec_arg1, dec_arg2, dec_arg3, func_arg1, func_arg2, func_arg3)
                  )
            return func(func_arg1,func_arg2,func_arg3)
        return wrapper
    return decorator
