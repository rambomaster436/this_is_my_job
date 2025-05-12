#This is a type hints are to begging python 3.6 are a new sitaxis that allow us declare the type of a variable or be that we are typing of some one way the variable

#using the using the declarations of type for your variables , the editors and anothers tools can give you a better support 
my_string_variable = "this is string"#if the edito is good this variable gonna help me to work faster but it we depemnding of the editor
print(my_string_variable)
print(type(my_string_variable))

my_string_variable= 5
print(my_string_variable)
print(type(my_string_variable))

#"these are typehints " fastAPI use type hints to do several things declare the parameters and to get the support of the editor an to have type checks or be fastAPI gonna can valid that the datas are rights if we send to operation of my API a string and it is not fastAPI gonna give us that that is unright with type hints fastAPI want understand that datatype 

#with : str we say that the variable is a str then the variable gonna really a string #:int is a typed feeble we can try to say it that it gonna to have with this but we cant obligate to to have that datatype by that :int dont become the variable in a int
#my_typed_variable: int = "variable string"
#my_typed_variable: int = "My typed String variable"#to work with fastAPI they gonna ask us that we work specifying the type of the variable because so we helping more to what the datas with what we're working in server that travel through of net gonna help to unaderstandn self better
my_typed_variable: str = "why did you leave me"
#with this :int etc the editor gonna interpretar how we want this is necessary for fast API since work much with this
#the backend with this gonna be faster clearer gonna interpreter better 
my_typed_variable.center # but when i put with :int the python intuye that is a int therefore it nw gonna give us operations methos of ints 
print(my_typed_variable)
print(type(my_typed_variable))

#the strong typed is what you cant to change the datatype python is of typed dinamyc for that we can to change it
 
my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))
#ls in terminal of python is for see all the folders that are inside of the superset or NEW PYTHON OF THE PRACTICES
