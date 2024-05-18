from view import pnpView

class pnpController:

	def __init__(self):
		self.view = pnpView(self)

if __name__ == '__main__':
	app = pnpController()