def partial(func, *args, **kwargs):
  def func_wrapper(*new_args, **new_kwargs):
    all_args = {*args, *new_args}
    all_kwargs = {**kwargs, **new_kwargs}
    return func(*all_args, **all_kwargs)
  return func_wrapper
