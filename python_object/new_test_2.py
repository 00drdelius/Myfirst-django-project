import json

class TraditionalCar:
	def __new__(cls, *args, **kwargs):
		print('Construct a new object...')
		Name=kwargs.pop('Name')
		Wheel_num=kwargs.pop('Wheel_num')
		Medium=kwargs.pop('Medium')
		Fuel=kwargs.pop('Fuel')
		print(super().__new__(cls))
		return super().__new__(cls, **kwargs)

	def __init__(self, *args, **kwargs):
		print('Initialise a new object')
		self._name=kwargs.pop('name')
		self._price=kwargs.pop('price')
		self._first_appreared_time=kwargs.pop('first_appeared_time')
		
	def __str__(self):
		print('The properties of the car are:')
		return json.dumps(self.__dict__)

if __name__=='__main__':
	print('object_construction pseudocode testifying:')
	
	MyFavor=TraditionalCar(
	Name='Car',
	Wheel_num='4',
	Medium='Road',
	Fuel='Petroleum',
	name='Audi R8',
	price='$143,000',
	first_appeared_time='2006')
	
	print(MyFavor)

	
