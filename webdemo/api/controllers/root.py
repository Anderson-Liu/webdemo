from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose
from webdemo.api.controllers.v1 import controllers as v1_controllers


class RootControllers(rest.RestController):
	v1 = v1_controllers.V1Controller()

	@expose.expose(wtypes.text)
	def get(self):
		return "webdemo"