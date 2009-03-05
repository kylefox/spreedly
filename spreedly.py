from pyactiveresource.activeresource import ResourceMeta, ActiveResource

class Subscriber(ActiveResource):
    pass

class ComplimentarySubscription(ActiveResource):
    pass        
    
RESOURCES = {}
for r in [Subscriber, ComplimentarySubscription]:
    RESOURCES.update({r.__name__: r})
    
class Spreedly(object):
    
    def __init__(self, site):
        self.site = site
    
    def __getattr__(self, key):
        if key in RESOURCES:
            klass = RESOURCES[key]
            setattr(klass, 'site', self.site)
            return klass
