class Handler:
	"""
	An object that handles method calls from the Parser
	
	The Parser will call the start() and end() at begining of each block ,with the proper block name as parameter. The sub() method will be
	used in regular expression substitution.When called with a name  such as 'emphasis',it will return a proper substitution function.
	
	"""
	def callback(self,prefix,name,*args):
		method = getattr(self,prefix+name,None)
		if callable(method):
			return method(*args)
	
	def start(self,name):
		self.callback('start_',name)
	def end(self,name):
		self.callback('end_',name)
	def sub(self,name):
		return lambda match: self.callback('sub_',name,match) or match.group(0)
