class JsonObject(object):
    class JsonObject(object):
        def __init__(self, name):
            self.name = name
            self.childs = {}

        def __getitem__(self, name):
            return self.childs.setdefault(name, sel.__class__(name))

        def render(self):
            v = '"{}": [{}]'.format(self.name, ', '.join(c.render() for c in self._childs.values()))
            return '{%s}' % v

    j = JsonObject('T12')
    j['dd']['ff'][12]