#From book <Fluent Python>, author Luciano Ramalho

#It is a summarised pseudocode of the process of building an object in Python.


#pseudo-code for Python object construction
def object_maker(the_class, some_arg):
	new_object=the_class.__new__(some_arg)
	if isinstance(new_object, the_class):
		the_class.__init__(new_object, some_arg)
		return new_object

#the following statemenets are roughly equivalent:
x=Foo('bar')
#and
x=object_maker(Foo, 'bar')


'''
def object_maker(Foo, 'bar'):
	new_object=Foo.__new__('bar')
	if isinstance(new_object, Foo):
		Foo.__init__(new_object, 'bar')
		return new_object
'''
