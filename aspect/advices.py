import inspect
import re
import sys
import enum

# Наверное вариант получше, если я дам функции класса атрибут _advice_type_ или что то такое
# И все advice функции буду складывать в класс в виде поля-списка. А не менять название функций.
# В любом случае я уже успел напороться на ошибку.
# Нельзя быть так просто зависимым на наименование класса.
# У меня были дандры, я решил поменять на одиночный _method_ в части классов. Из за этого ничего не работало.
# Надо уйти от зависимости на строку. Хотя бы в таком явном виде.


class AdviceType(enum.Enum):
    BEFORE = enum.auto()
    AFTER = enum.auto()


def how(how_type: AdviceType):
    if how_type not in AdviceType:
        raise ValueError(f'expected how type from {AdviceType}, but got {how_type:=}')

    def decorator(func):
        # Maybe not a good name because of dunder.
        new_name = f"_{how_type.name}_aspect_{func.__name__}_"
        namespace = sys._getframe(1).f_locals
        namespace[new_name] = func
        return func
    return decorator


def encode_method(method_name: str, advice_type: AdviceType):
    return f"_{advice_type.name}_aspect_{method_name}_"


def decode_advice(advice_name: str):
    advice_type_name, _, method_name = advice_name.strip('_').split('_')
    advice_type = AdviceType[advice_type_name]
    return method_name, advice_type


def is_advice(method_name):
    advice_type_names = AdviceType.__members__.keys()
    types_for_regex = '|'.join(advice_type_names)
    advice_method_pattern = rf'_({types_for_regex})_aspect_\w+_'
    advice_methods_match = re.match(advice_method_pattern, method_name)
    return bool(advice_methods_match)


def is_advice_and_type(method_name, advice_type: AdviceType):
    advice_method_pattern = rf'_{advice_type.name}_aspect_\w+_'
    return bool(re.match(advice_method_pattern, method_name))


def get_class_advice_methods(cls, advice_type: AdviceType) -> dict:
    cls_methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    advice_type_members = []
    for method_name, method in cls_methods:
        if is_advice(method_name):
            origin_method_name, method_advice_type = decode_advice(method_name)
            if method_advice_type is advice_type:
                advice_type_members.append((origin_method_name, method))
    return advice_type_members
