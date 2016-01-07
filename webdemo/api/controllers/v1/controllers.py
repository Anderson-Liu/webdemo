from pecan import rest
from wsme import types as wtypes

from webdemo.api import expose


class V1Controller(rest.RestController):

	@expose.expose(wtypes.text)
	def get(self):
		return 'webdemo v1controller'