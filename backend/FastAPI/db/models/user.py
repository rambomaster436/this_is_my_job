#we import base model from pydantic 
from pydantic import BaseModel #this BaseModel that was from usersdb we delete of ther because we dont need it there more 

#with this we've already defined what would be already our user if we want even we can to simplify of someone way we gonna make what it's ID etc
class User(BaseModel): 

    #to simplify we gonna make that it's someone things differents necessaries for what be even much easier to work with our user and delete the last 2 because to have more datas only would be more datas and it's all but dont care then with that we'd have our entity now what we've that to make is to import it and in the part of the class form in the usersdb folder we delete all the class because it doesnt serve us 
    id: str | None  #we put the ID identificador único de cliente mediante el cual un anunciante elige identificar a un usuario que visita su sitio web. to identify and this is in path
    username: str
    email: str
