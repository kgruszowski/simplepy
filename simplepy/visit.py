# visit.py
# Updated 2013-06-20 to fix bug on line 38

import inspect

__all__ = ['on', 'when']

def on(param_name):
  def f(fn):
    dispatcher = Dispatcher(param_name, fn)
    return dispatcher
  return f


def when(param_type):

  # f - actual decorator
  # fn - decorated method, i.e. visit
  # ff - fn gets replaced by ff in the effect of applying @when decorator
  # dispatcher is an function object
  def f(fn):
    frame = inspect.currentframe().f_back
    dispatcher = frame.f_locals[fn.__name__]
    if not isinstance(dispatcher, Dispatcher):
      dispatcher = dispatcher.dispatcher
    dispatcher.add_target(param_type, fn)
    def ff(*args, **kw):
      return dispatcher(*args, **kw)
    ff.dispatcher = dispatcher
    return ff
  return f


class Dispatcher(object):
  def __init__(self, param_name, fn):
    frame = inspect.currentframe().f_back.f_back   # these 2 lines
    top_level = frame.f_locals == frame.f_globals  # seem redundant
    self.param_index = inspect.getargspec(fn).args.index(param_name)
    self.param_name = param_name
    self.targets = {}

  def __call__(self, *args, **kw):
    typ = args[self.param_index].__class__
    d = self.targets.get(typ)
    if d is not None:
      return d(*args, **kw)
    else:
      issub = issubclass
      t = self.targets
      ks = t.__iter__()
      return [ t[k](*args, **kw) for k in ks if issub(typ, k) ]

  def add_target(self, typ, target):
    self.targets[typ] = target
