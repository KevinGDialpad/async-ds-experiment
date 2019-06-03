# The idea
## ds/ and ads/
The idea is to have:
1. a synchronous ds/ library that can be called from either Python 2 or Python 3, and
2. an asynchronous ads/ library

ads/ is meant to be a wrapper around ds/. It is callable with the await/async syntax but makes synchronous calls to ds/.

## The transition
While we have both Python 2 and 3 code using the datastore, Python 2 uses ds/ while Python 3 uses ads/. Moving a module to Python 3 means using the async syntax and using ads/ (even though it makes synchronous calls under the hood).

When everything is on Python 3, nothing is calling ds/. We can move all the ds/ code to ads/ and remove the synchronous transport layer (from ds) and the wrapper code (from ads). ads/ is now asynchronous and ds/ can disappear. We can even rename ads/ to ds/ after that. 

## Ilustration

![Example diagram](https://github.com/KevinGDialpad/async-ds-experiment/blob/master/images/get-example-diagram.png)

The left-hand side can be called form Python 2 or form Python 3. The right-hand side is Python 3 only.

`ds.Model._get()` contains all the get logic that's not part of the transport layer (see the [current `Model.get()` on master](https://github.com/dialpad/firespotter/blob/d472b03266f16efd90aec0b3eb4d583750be7bdc/common/lib3/ds/base.py#L209-L223)).
It's called form both `ds.Model.get()` and `ads.Model.get()`, with are just wrappers. The wrappers call `_get()` and make sure it uses the correct transport `get()`.

So when you use ds/, it goes `ds.Model.get()` -> `ds.Model._get()` -> `ds.get()`.

When you use ads/, it goes `ads.Model.get()` -> `ds.Model._get()` -> `ads.get()`.

The actual logic is not duplicated because it lives in `ds.Model._get()`. When we stop using ds/, that logic can move to `ads.Model.get()`. Then the call goes `ads.Model.get()` -> `ads.get()` and it's all asynchronous.

# Current output
## Python 2
```
$ python client.py
Model sync get()
Model base _get()
get() with key = my_key
Got a model with key=my_key
```

## Python 3
```
$ python client.py
Model async get()
Model base _get()
async get() with key = my_key
Got a model with key=my_key
```

# References
Python docs:
* [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
* [Event Loop](https://docs.python.org/3/library/asyncio-eventloop.html)

People solving similar problems:
* [How to wait for coroutines to complete synchronously within method if event loop is already running?](https://stackoverflow.com/questions/39470824/how-to-wait-for-coroutines-to-complete-synchronously-within-method-if-event-loop)
* [Asyncio and an attempt to run loop.run_until_complete() from within a running loop](https://mail.python.org/pipermail/python-list/2016-April/707139.html)
