# The idea
## ds/ and ads/
The idea is to have:
1. a synchronous ds/ library that can be called from either Python 2 or Python 3, and
2. an asynchronous ads/ library

ads/ is meant to be a wrapper around ds/. It is callable with the await/async syntax but makes synchronous calls to ds/.

## The transition
While we have both Python 2 and 3 code using the datastore, Python 2 uses ds/ while Python 3 uses ads/. Moving a module to Python 3 means using the async syntax and using ads/ (even though it makes synchronous calls under the hood).

When everything is on Python 3, nothing is calling ds/. We can move all the ds/ code to ads/ and remove the wrapper code. ads/ is now asynchronous and ds/ can disappear. We can even rename ads/ to ds/ after that. 

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
