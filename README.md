This is an extremely thin wrapper around [pyactiveresource](http://code.google.com/p/pyactiveresource/) which provides easy access to the [Spreedly.com](http://spreedly.com/) API.  pyactiveresource does **all** of the heavy lifting, so make sure you've installed it.  python-spreedly simply adds syntactic sugar.

Example (from console):

	>>> from spreedly import Spreedly
	>>> spreedly = Spreedly(SPREEDLY_API_URL)
	>>> customer = spreedly.Subscriber.create({
	...     'customer_id': '1234',
	...     'screen_name': 'Anthony Hopkins'
	... })
	>>> customer.attributes['store_credit']
	Decimal("0.0")
	
To retrieve all subscribers:
	
	spreedly.Subscriber.find()
	
To retrieve a specific subscriber:

	spreedly.Subscriber.find(1234)
	
Creating a Complimentary Subscription works slightly different however:

	>>> customer = spreedly.ComplimentarySubscription.create({ 
	...     'duration_quantity': 30,
	... 	'duration_units': 'days',
	... 	'feature_level': 'free' }, { 'subscriber_id':1234 })
	>>> customer.active
	True

Two dictionaries are sent, one for the complimentary subscription info and one for the subscriber number.
	
For a full list of what the API does, check out the [Spreedly Integration Reference](http://spreedly.com/manual/integration-reference/).  You might find the [Rails Examples](http://spreedly.com/manual/integration-reference/api-access-using-rails/) helpful, as they use the [ActiveResource](http://api.rubyonrails.org/files/vendor/rails/activeresource/README.html) pattern.

If you've never heard of them, here's what the fine Spreedly folks do:

"Spreedly lets you collect recurring and one-time subscription payments simply and securely. Your customers can upgrade and renew with ease while you monitor everything from your dashboard. Spend your time improving your service - not building a billing system."