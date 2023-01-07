def test(*args, **kargs):
    for arg in args:
        print(arg)
    for key, value in kargs.items():
        print('%s:%s' % (key, value))
