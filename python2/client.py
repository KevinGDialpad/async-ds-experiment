from lib import ds

def main():
  model = ds.Model.get(key='my_key')
  print('Got a model with key=%s' % model.key)

if __name__ == '__main__':
  main()
