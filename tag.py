class Zawor:
	def __init__(self, iprefix, iname, isensorHP, isensorWP, ivalveHP, ivalveWP, isideHP, isideWP, iidle):
		self.prefix = iprefix.upper()
		self.name = iname.upper()
		self.sensorHP = isensorHP.upper()
		self.sensorWP = isensorWP.upper()
		self.valveHP = ivalveHP.upper()
		self.valveWP = ivalveWP.upper()
		self.sideHP = isideHP.upper()
		self.sideWP = isideWP.upper()	

		if iidle == '':
			self.idle = 'NONE'
		else:
			self.idle = iidle.upper()

	@property
	def rname(self):
		#ST1 DOCISK
		return f'{self.prefix} {self.name}'.lstrip() 

	def rsenNameHP(self, rodzaj):
		#ST1 DOCISK HP LEFT
		if rodzaj == 0:
			_tmp = ''
		else:
			_tmp = 'VSEN'
		return f'{_tmp} {self.rname} HP {self.sideHP}'.lstrip()

	def rsenNameWP(self, rodzaj):
		#ST1 DOCISK WP RIGHT
		if rodzaj == 0:
			_tmp = ''
		else:
			_tmp = 'VSEN'
		return f'{_tmp} {self.rname} WP {self.sideWP}'.lstrip()		

	def rvalveNameHP(self, rodzaj):
		#ST1 DOCISK HP LEFT
		if rodzaj == 0:
			_tmp = ''
		else:
			_tmp = 'VALVE'		
		return f'{_tmp} {self.rname} HP {self.sideHP}'.lstrip()  

	def rvalveNameWP(self, rodzaj):
		#ST1 DOCISK WP RIGHT
		if rodzaj == 0:
			_tmp = ''
		else:
			_tmp = 'VALVE'	
		return f'{_tmp} {self.rname} WP {self.sideWP}'.lstrip()  	

	def rvalveNameIDLE(self, rodzaj):
		#ST1 DOCISK IDLE
		if rodzaj == 0:
			_tmp = ''
		else:
			_tmp = 'VALVE'
			
		if self.idle == 'NONE':
			return 'NONE'
		else:
			return f'{_tmp} {self.rname} IDLE'.lstrip()
	  		