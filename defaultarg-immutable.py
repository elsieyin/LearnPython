def register(name, hobby, l=[]):
    l.append(hobby)
    print(name, l)


register('Kobe', 'play')  # Kobe ['play'] 一切正常~
register('James', 'read')  # James ['play', 'read'] what?!
register('Albert', 'music')  # Albert ['play', 'read', 'music'] 这就是未设置为不可变类型出现的BUG