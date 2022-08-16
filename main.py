

from decorator.decorator_with_agrument import decorator_with_agrument
from decorator.decorator_with_arbitrary_agrument import decorator_with_arbitrary_agrument
from decorator.pass_agrument_to_decorator import decorator_make_with_agruments
from decorator.uppercase_decorator import uppercase_decorator

@decorator_make_with_agruments("huy","23","Soft")
def func_with_argument(func_1,func_2,func_3):
    print("Args in func are:{0},{1},{2}".format(func_1,func_2,func_3))

func_with_argument("truc","24","design")

