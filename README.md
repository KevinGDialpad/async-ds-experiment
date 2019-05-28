Python 2:
```
$ python client.py
Model sync get()
Model base _get()
get() with key = my_key
Got a model with key=my_key
```

Python3:
```
$ python client.py
Model async get()
Model base _get()
async get() with key = my_key
Exception in callback <Task finished coro=<get() done, defined at /Users/kevinguillaumond/Stuff/async_lib_experiment/python3/lib/ads.py:23> result=<lib.ads.Mode...t 0x108840978>>()
handle: <Handle <Task finished coro=<get() done, defined at /Users/kevinguillaumond/Stuff/async_lib_experiment/python3/lib/ads.py:23> result=<lib.ads.Mode...t 0x108840978>>()>
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/events.py", line 88, in _run
    self._context.run(self._callback, *self._args)
TypeError: '_asyncio.Task' object is not callable
Traceback (most recent call last):
  File "client.py", line 10, in <module>
    asyncio.run(main())
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/runners.py", line 43, in run
    return loop.run_until_complete(main)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 584, in run_until_complete
    return future.result()
  File "client.py", line 6, in main
    model = await ads.Model.get(key='my_key')
  File "/Users/kevinguillaumond/Stuff/async_lib_experiment/python3/lib/ads.py", line 20, in get
    return Model._get(callback, key)
  File "/Users/kevinguillaumond/Stuff/async_lib_experiment/python3/lib/ds.py", line 10, in _get
    return get_method(key)
  File "/Users/kevinguillaumond/Stuff/async_lib_experiment/python3/lib/ads.py", line 18, in callback
    return get_task.result()
asyncio.base_futures.InvalidStateError: Result is not set.
```
