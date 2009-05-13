from pyactiveresource.activeresource import ResourceMeta, ActiveResource

class Subscriber(ActiveResource):
    pass

class ComplimentarySubscription(ActiveResource): 
    @classmethod
    def create(cls, attributes, prefix_options):
        """
        Override create method to accept two parameters since prefix
        options are required. This simply provides the ComplimentarySubscription.create()
        interface instead of creating the object manually and calling save()
        """
        resource = cls(attributes, prefix_options)
        resource.save()
        return resource

RESOURCES = {}
for r in [Subscriber, ComplimentarySubscription]:
    RESOURCES.update({r.__name__: r})
    
class Spreedly(object):
    
    def __init__(self, site):
        if not site.endswith('/'):
            site.append('/')
        self.site = site
    
    def __getattr__(self, key):
        if key in RESOURCES:
            klass = RESOURCES[key]
            if klass == ComplimentarySubscription:
                setattr(klass, 'site', '%s%s'% (self.site,'subscribers/$subscriber_id/') )
            else:
                setattr(klass, 'site', self.site)
            return klass
