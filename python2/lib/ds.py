class Model(object):
  @classmethod
  def _get(cls, get_method, key):
    # type: (Callable[(str]->Model], str) -> Model
    print('Model base _get()')
    return get_method(key)

  @classmethod
  def get(cls, key):
    # type: (str) -> Model
    print('Model sync get()')
    return Model._get(lambda k: get(k), key)

def get(key):
  # type: (str) -> Any
  print('get() with key = %s' % key)
