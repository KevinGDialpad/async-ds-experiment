Python 2:
```
$ python client.py
Model sync get()
Model base _get()
get() with key = my_key
```

Python3:
```
$ python client.py
Model async get()
Model base _get()
client.py:6: RuntimeWarning: coroutine 'get' was never awaited
  await ads.Model.get(key='my_key')
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
```
