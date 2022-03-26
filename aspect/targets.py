"""
Rename to explicit-python-aspect
explicit-pyspect
expyspect
"""
import inspect

from aspect.advices import AdviceType, get_class_advice_methods


def bind(target_bind_cls):
    def decorator(source_bind_cls):
        # before_target_methods = dict(_before_methods(target_bind_cls))
        # after_target_methods = dict(_after_methods(target_bind_cls))
        before_target_methods = dict(get_class_advice_methods(target_bind_cls, AdviceType.BEFORE))
        after_target_methods = dict(get_class_advice_methods(target_bind_cls, AdviceType.AFTER))

        source_methods = dict(inspect.getmembers(source_bind_cls, predicate=inspect.isfunction))

        for method_name in source_methods:
            # import pdb; pdb.set_trace()
            if (method_name in before_target_methods) or (method_name in after_target_methods):
                def decorated_method(*args, **kwargs):
                    if method_name in before_target_methods:
                        before_target_methods[method_name](*args, **kwargs)

                    result = source_methods[method_name](*args, **kwargs)

                    if method_name in after_target_methods:
                        after_target_methods[method_name](*args, **kwargs)
                    return result

                setattr(source_bind_cls, method_name, decorated_method)
        return source_bind_cls
    return decorator
