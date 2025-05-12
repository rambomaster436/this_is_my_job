#Api for users 

#In this case of api we can to separe if we want for become it more andarstable we could become in 2 apis differents for users and for user
#REMEMBER TO RUN A SERVER YOU NEED TO PUT THE UVICORN IN THE FILE THAT YOU GONNA TO USE

#we cant to have syncronas in our api because it'd mean that every time that somebody does a petition would block the operation of the server and would block the ejecution that reach new petitions #it's asyncrono by definition
#python 3.11 is faster 
#mongotv and fastapi is resources free
#it's almost the same that the other but withb /users
#apart of FastAPI we must import from pydantic import BaseModel for server of for users  for that we work with an entity that serve for define users 
from pydantic import BaseModel
#To release an exceptions we need also import HTTPException that exist already in fastapi so we can to use already
from fastapi import APIRouter, HTTPException 
from fastapi.encoders import jsonable_encoder #here we import from fastapi.encoders jsonable _encoders to safe that the datas sent to the server are coded 
#fastAPI accept millions of  parameters is the initial of fastAPI of how it gonna behave our server practicely to the time of to try petitions in the API
router = APIRouter() #FastAPI() is a class 

#Model object encharge of understand that all the datas that pass to us are what have typed and of to become the json in an user
#defining entity user is with entity class User(): where in the part of down it find the parameters
#here we put BaseModel in the item User(BaseModel) to do use of it 
#BaseModel help to what we dont have that create the structure to hand instead of down 2 hand done BaseModel build it alone#if we can possess an objec that implement the behavior of BaseModel we can already drive it how if it was a json directly fastapi gonna in charge of the object with beahvior of BaseModel without problems 
#it'd be very uneasy to do it without BaseModel 
class User(BaseModel): #The BaseModel is giving us the capacity to create an entity is how if we would be creating an estructure of user type that hase the parameter of down an this BaseModel gonna have by inside a very concret mechanism that allow that we create it, try with it 
    #we're typing name as a string because is help when we work with a object user type then the name has that to be text string no other also serve for all the rest
    #equal that we have this formation for users we can do some seemed also but for some that give back objects
    id: int  #we put the ID identificador único de cliente mediante el cual un anunciante elige identificar a un usuario que visita su sitio web. to identify and this is in path
    name: str
    surname: str
    url: str
    age: int

#we're going to define a list with differents users
#we call to entity user here [User(element of user)]#the classes has a builder
#Normally the clases has that to have a cosntructer but we're going to do it without it#We put datas inside of User(elements) 
#it has that to have a constructer if no it doesn't execute for what it wotk also we can to put BaseModel
#we're going to create 3 users 
#we put this for what it can eport in users #"no more problem with the limit of number of user untill 9"
#this is a data base invented
Users_data_Base = [User(id=1, name="robetr", surname="ray", url="https://mouredev.com/python.queti", age=12 ),
                   User(id=2, name="rambo", surname="quispe", url="https://lavacalola.com/python.import", age=15 ),
                   User(id=3, name="julio", surname="mamani", url="https://lavacaachorada.com/python.that is the same", age=18 )]#gonna be a list with differents users or gonna be how globals users #this gonna be how database

#When we work with apis is recommended to work with the error codes of fastapi 
#this time for run we dont use uvicorn main:app --reload for start the serve instead that we use uvicorn users:app --reload
#name= input("insert your name:")
#lastname= input("insert your lastname:")

#the normal is what when we are inside a router is what all the requests go to the same 
#this serve without from pydantic import BaseModel for simple datas "jsons are how claves values
@router.get("/usersjson") #for what go in in main normally we 
 
#user() dont affect much
async def usersjson(): #with async we become def of a funtion sincrona to a funtion async #ever that we call to a server the operation that it execute have that to be asynchronous
    #it's better  with [] or {} there almost dont do errors in the symbols

    # we wanna return user for to do this server for users we're going to give back users 
    #in the dictionaries we work we work with a lenguage oriented to objects
    return [{"name": "robetr", "surname": "ray", "url": "https://mouredev.com/python.queti", "age":12},
            {"name": "rambo", "surname": "quispe", "url": "https://lavacalola.com/python.import", "age":15},
            {"name": "julio", "surname": "mamani", "url": "https://lavacaachorada.com/python.that is the same", "age":18}] #also work with string but someone symbols dont reknow them

#In all this we can to put the answers codes for can explain to the users about its error besides of if their operations are rights
#to get concrets things we use an api thinked forn users
#first we create an entity that serve for users to define users this has a router for agrupar routes #we can create severals apis can agrupar all from our api general that value for obtain datas from users and obtains datas from products 
#if we wanna work with an object or model but it'd be complicate by that we hace some what can be an object user or be a class
#for thos operations we need to give it another focus for what they've more sense
@router.get("/users") #by some one reason when we put the answer code when we do the petition get in thunder this  cant reknow the answer code by that we deleted 

#"remember the double funtions can create you problems or to do that dont reknow 'em"
#user() dont affect much
async def users(): #with async we become def of a funtion sincrona to a funtion async #ever that we call to a server the operation that it execute have that to be asynchronous
    #it's better  with [] or {} there almost dont do errors in the symbols

    # we wanna return user for to do this server for users we're going to give back users 
    #in the dictionaries we work we work with a lenguage oriented to objects
    #also work with string but someone symbols dont reknow them
    
    #with BaseModel when we call to the api we get we have a class, an object of way transformed to a json quick
    #now we have a listed of users that coincided with usersjson()
    #now we're going to return Users_data_Base
    return Users_data_Base #we create the class user with this with this we are indicating that all these parameters we are doig of way positional and with = we're saying that we're representing in everyone of the camps #really we can create a class and  to send the arguments how we want but in this case we have a class that is herediting a behaviour of BaseModel in this case by that are espcifying how go everythingfor what doesnt exist no doubt of how are creating the objects how you can to see in the postman the order of position of all 
#the lecture can be of all the users or user paginados because can to have many but we th typycal is what we use tha path also to pass information to our api, im the path can to go the ID of the user that wanna search

#path 
#From here start the path #and we're going to create the ID
#the usual is what when we create funtions must to give it a name that can interpretate with the operation that it gonna perform
#the ID yes or yes has that be an integer
#then user() we gonna call user() because we're going to pass an ID, in ("/users/") we put so to use the own path and in this we gonna can pass it parameters that we gonna to can capture ("/users/{parameter}") the parameter in this case is the usual to give it the name that know that gonna be inside Example ID
@router.get("/user/{id}", status_code=216)#Theparameters go in /{parameter} #and if form part of this path and we wanna try how a parameter this doesnt mean that we are calling /users/ID if no we call to /users after would call to a parameter that we must capture that iterpretate how an ID, this gonna to by an user then logically is not call it users if no to call to users

async def user(id: int): #The ID we capable of to read it here in with funtions that might to have parameters we pass it parameters with the name of the (parameter: typing the datatype)in this case (ID: int) fastapi work tipeando the datatype 
    #if we execute filter it gonna reboock
    #Lambda return the camp ID #if we execute it gonna give back an object, and we save it in a user because we said that we dont access Users_data_Base because is in another funtion, aslo we can save of many forms how in a for and anothers etc
    return user_search(id)    

    #the filter we can apply in anyone structures where we have severals objects
    #we put list(users) for that it give back the objects user new 
    #advice when you put an ID bigger than 9 this doesnt reknow it besides to search to the user we use /number ID #the /1 return a listed but our operation is users or be only it'd have that to go to the 1rst result for what it gives back an only result and no a list we put[0] the 1rst result
    #The post man or server gonna return only the amount of users that we put and if that amount of users there's no then the server gonna return Internal server because has petado the server because i've not in the element 0 then to evit that we must to do tests of what the list wasn't empty with try except etc
    #return "" #a time that we have the ID might to access to the ID# if we wanna access to the listed of users can to look for operations or method

#besides of the parameters that can go by the self path also we have parameters that can go by the cueri #we have others more for invocate 
#to go by the path is to say that was by the self path that was in the URL when we speak that can go by the query is what we can indicate it almost all what we wanted by cuery

#to call by query is this of down

#we can also to do search by name through of to put onother parameter in user(ID: int, name: str):
#with query we are limiting that the petitions be of a way very concret thanks to type and by other side since we can define it in "path" up and query 
#this is a little better because this allow us create a form more seemed to a web page more real with /?ID=ner ID
#if we put userquery it gives back that lack some to the initial because we typed it or taught it if we've idicated if we call to this operation it say us that lack some or the ID and in the terminal gives back error 422 fastapi no only gives back error 200 if no all 
#to call to a parameter by query mean is what we can equal a key to a value inside the URL because is very typical also in users or in obligatory things like the ID of the users but what was optional to say it how many users wanna bring 
#the query does very simple the ask the amount of users #the query especify of way how back the / goes "?" so /?"parameter"=1 so /?d=1 in postman parameter is the 1 parameter of the query /?ID=1 , it ID=1 is saying that search ID 1 etc in postman or in the server
#also we can call to /user/ normal in @app.get("/userquery/") also it'd be well but in postman we put /user/1 and it return the user and iqual work with /user/?ID=1 or be we can redefine the same operations example in patn we put IDe instead ID and work normal yet if we put IDe how in path this return in postman doesnt exist is to say we've been capable of to create the same operation but in a case seeing through of the path by other side through of the query 
#we start to difference that inside the own query we have many forms of to call it
#in get we can access to an user in specifyc when we put user/nmber
@router.get("/user/", response_model=User, status_code=217)#"/user/" the same of up but without the {ID} #if we put the same /userquery/ in postman it gonna return that the values gave back are not 

#we start to difference that inside the own query 
#the ID we're going on passing it equal
#if we want concadenar mas or be add (ID: int, name: str) for more parameters and what this work or search in postman we do it by ampersand or be we add & so ?ID=1&name=robetr or other name of this way we can add more parameters with & like surname etc
async def user(id: int): #The ID we capable of to read it here in with funtions that might to have parameters we pass it parameters with the name of the (parameter: typing the datatype)in this case (ID: int) fastapi work tipeando the datatype 
       
       #this operation we could externalizar migth to be a funtion or to be in a module because because we are searching in the same place
    #if we execute filter it gonna reboock
    #Lambda return the camp ID #if we execute it gonna give back an object, and we save it in a user because we said that we dont access Users_data_Base because is in another funtion, aslo we can save of many forms how in a for and anothers etc
    return user_search(id)
#python is a lenguage of dynamic typed but fastapi recomend that we type all the parameters #"value is not a valid integer" mean that the value must be integer in postman in the postman "the /?ID=some can be anyone thing no justly an integer" 

#operation that allow us add users

#post 

#post is for add values 
#also it can to do others operations with get like delete but is not recomendable by that we do with the correspondiente
#to create a post we access amplification @app that is a instancia of fastapi and to put what we want like delete put but in this case post()
#we put status_code=201 for what if it execute rightly then in thunder the status shows the 201 instead 200 we can to put what want
#This status_code we can to do it with all to get to do well the same that in case against like the return
#status_code=201 is an answer code by defect and in case against like the if operation we release if it fail
#In this operation in the user status_code we can to indicate also for the diocumentation for what it be understable better we can to say that it gonna give back already because in case that it doesnt retur  that we can mark error with reponse_model= User that return an entity of User type this go first that staus_etc
@router.post("/user/", response_model=User, status_code=201) #and we have that indicate where of the URl we must call to do a post the (paraneter) how we wanna add a new user put ("/user/") now with the response in the swagget we have response or be a request in post that say us also what it reponse if it run well and if run bad also say us the 201 or what we puts or the right answer code also return, when it go well return an object of user type and if it go bad then return an error by defect
#for what anyone operation is exposed in our api with app. and to say the operation type that we're going to do it's enough

#operation
#to do it better we put the operation before of lambda
#if we want that this operation in case that dont happen nothing strange return a 201 instead a 200 then we can in the definition of the funtion or in the async def just over or be in the operation post we add to the user/", status_code=201 ) this mean that we said it that return by defect a 201 instead 200
async def user(user: User): #the name can return to be user because we gonna add a new user in parameter we put user: User because we gonna add a new the user is the parameter and the User because we have one up
    
    #remember a error code 500 we cant release only the server is danger 

    #with the operation of down we evit that it repeat the user or ID with that we control it 
    #the 405 method not allowed is because you're in the user but that code after user is not allowd but 404 is because you're not in of no one// 500 internal error
    #the operation is in put by that now is a post in thunder besides in body put the list User so it return null or the error of else
    #we have that to call to /user/ no more and once that the we put the list User in thunder and we puts the send then the fastapi gonna encharge of become the json of thunder in the user of User for what there in the funtion reach an user that perfectly we can understand already from python and that it has already the structure #when we put in bofy in post man a User unexist then return null, to know that the puts in body we call to users with get and it gonna return all the users of the list with the new user inserted in thunder besides it can add so many users how we want but one by one doesnt accept list but remember once that you puts an User inside body you can't delete till you leave gonna appear again how its ID but it gonna disappear if you go to another file and you insert a new with the same User ID 
    #here if the User exist already then retun an error and if no in else add the user
    #if to the look for user i can find out or verify that who comes in if the type of user == User then  do a thing and if no another
    #for what the status in thunder dont be unright and return the right status we do the next operation we cant o put the satus what we want but is better one that is correspondent
    #I have the user yet
    if type(user_search(user.id)) == User:#we can obtain this list of users, to say user_search("passing the ID that reach by here" user.ID) with if we prove that the ID exist or not also if it's error or if has list of users#we can do a proveexample to prove that if the user exist already then we dont add and it return an error how drive of exceptions
        
        #to release an error we release an exception called http exception this is a class that exist already inside fastapi by this we need to import apart of FastAPI also , HTTPExceptions
        #we put HTTPException(status_code=409) in this case error 409 or be the message when the request  conflicts with current state state of the server
        #we return then the exception for what it save it in the thunder but for whag the status change really we put instead of return the raise #the error code 204 is a no content and when you send it in thunder it return nothing status 204 no content remember every error code drive of differents ways the datas example content in response dont return nothing but the 404 only return the message of detail 
        #concret answer code for error #raise is for propagate the exception no return simply the content of the exception if no that it release it with the detail it shows it because we are launching an error when we launching and 404 really is launching already the result and this does it by defect the standar by that you must to have very especify with what you're releasing and how and that operations are being exposing if is a post etc, 
        raise HTTPException(status_code=404, detail="the user exist already") #we can to put more parameters ,detail #with HTTPetc ww dont need return because we're releasing an exception

        #return {"error":"User exist already"} # we dont need more the return because we are launching an exceotion in up
    
    #if i haven't that user then add the user 
    #another good practice in the moment that it work for havent doubts how it has resulted 
    else:    #now with this of down we can do it without else 
        Users_data_Base.append(user) #to access to the list of users and with append add a new user with (user)
    #another good practice in the moment that it work for havent doubts how it has resulted to dont return a null we return user in the post that has been added in the post because if it fail it returned error and in the put some seemed also we put
        return user
    #to return a http code, if we wanna change the satisfactory answer code then the message of status of up of thunder should be an 201 of created user  
    
#we put thiss operation in postman taking adventage of what we have thunder client putting instead get post to do the operation and we gonna call to /user/ having that receive our user in body some how in get but user was an object of type User but this must represent of way that it be understandable or that can understand like a json and fastapi authomatically gonna encharge of become this json in the User to what in user:User reach an user that we can understsand from pyhton and it' already thestructure of funtion User 

#put

#put is for update also to change and user by other or another elements by other we could to do a put of parameters by separed
#@app.put("/user/") update the user by reason of that the user change 
#with the same funtion of the others if we want to update an user we have differents options in (parameter to update) this depende how we wanna implement the api like update the object complete but also the parts
#remember with put you can to do also small changes 
@router.put("/user/",response_model=User ,status_code= 201)
async def user(user: User): #we can update the complete object or be we send it the complete user and it gonna change and user by other or by parameters by separed or be this object user accept nulls and we just modify parameters that we wants inside this user like the URL or be only send that to my operation this to do it of way more advanced this might to be well for these cases would be to use patch but patch we do not gonna use because is not an operation of the super comuns  when we gonna create an APi w'll have of all #the patch is better to update a concret part of the user and the put is better for all the user # we dont gonna use the patch because patch is an operation a little more advanced #We gonna implement a pure behaviour of a put that would be update the complete user to update the complete user we have that to put in (user : User) seemed to up if we wanna update the complete user we have that to put the user
    
    #if we put the update uncomplete then the result will be a message of that loc or lack some like the ID etc this happen because we did this with the Api or be the structure of up User(BaseModel) with the strings int etc where we stablish it thanks to BaseModel by that it give an answer so, even we might stablish that someone parameter dont must to receive it in User BaseModel stablish that all it inside of its structure is obligatory if we dont send it then it peta or return the message doing it automatically fastapi, if lack the name equal return the message for all the obligatories is equal besides if we write bad the code of user then return what was the error
    #we create a variable to get improve the update
    found = False #we say it that is false is a variable more or less to control if we updated the user or not 

    #when it result in null in update then mean that it updated
    #if we reached untill here mean that it got update
    #we need to search the user and update #so what we we have now in for an index and in the in we have an enumeration of the list we put index in the for by that, first user of the list star 0 2 start 1 etc if we find it we can to do the operation of down is to access to the list of users with its indice index Users_data_Base[index]
    for index, saved_user in enumerate(Users_data_Base): #to update the user how we've a list if we did with the filter we dont gonna have a reference of the user so what we gonna do it of a way that it be understable simply we gonna run our list and in the moment that it find the user that coincide with the ID of the user that they are sending us well we update it in the list and it'd be how represent that it's updated the user in data base so what we do a operation for of the user in the lists and we saved them in the saved_user and we gonna run the list 
        
        #a time that we have users list we have to test the saved_user.ID is == to user that reach us of thunder its ID user.ID it wanna say that we've found the user therefore then we can update it, we can update it with 
        if saved_user.id==user.id: #here we dont have a reference of the user we'd have that to know in what position is in that user for it we enumerate the list and keep the ID of the list with emumrate funtion we do it so enumerate (we pass the list user Users_data_Base) in for in
            
            #we access to the list users with its indice index where gonna go the user that has reached 
            Users_data_Base[index] = user #we dont care already the user that is saved it gonna update it then we give the replace or update of it in body with this we may update and it'd be al but we can do it more beautiful how down
            found = True #then found is True or be yes we have found the user and we updated it 

    #if we dont find then it doesnt update and we return an error
    if  not found:

        #if we put a user with some lack and we send in put then it gonna return loc or be lack 
        raise HTTPException(status_code=409, detail="the user wasnt updated") #the errrors cant be represented so ever if no there's many ways better 
    #in the two we do it up in post and in here equal
    else:
        #we return, in case that get to find it, the user# thie gonna say tof up if the user doesnt exist if we send in thunder
        return user
    
#other typical operation of the apis are  this is for to ride Sclude that are the operations of reading of writting of updating and of deleting 

#delete 

#we do the operation of the same way tha of others but put the delete after.
#her the only that it does is to search in the path a parameter that it gonna iterpretate how an ID of integer type so what it doesnt case to the body 
@router.delete("/user/{id}", status_code=210) #delete of an only user #In here in no one place we're recollecting the body of this petition 

#this is a path but in a put because the ID is obligatory
#what we have that to pass to our operation delete to know that we we've that to delete is the ID the clave of the user is the ID is not necessary to pass it all only we must to do the same that in get 
#the ID is obligatory therefore then is a path we do a path or copy the get of path
#Now with this operation we can delete doing a search in the thunder join to the users/ner of user that you wanna delete of ths way we can delete the user in this case dont care the json that is in the body 
async def user(id: int): #the funtion to use is remove or method 

    #with this we test that is right if we found or i didnt find 
    found = False 

    #we can to search through how a for of the put operation 
    #and in the moment that we found the user that we wanna delete in this case i's not already the user if no straightly the ID well in the moment that we found it then we delete it, we do a deleting ooeration
    for index, saved_user in enumerate(Users_data_Base): #to update the user how we've a list if we did with the filter we dont gonna have a reference of the user so what we gonna do it of a way that it be understable simply we gonna run our list and in the moment that it find the user that coincide with the ID of the user that they are sending us well we update it in the list and it'd be how represent that it's updated the user in data base so what we do a operation for of the user in the lists and we saved them in the saved_user and we gonna run the list 
        
        #a time that we have users list we have to test the saved_user.ID is == to user that reach us of thunder its ID user.ID it wanna say that we've found the user therefore then we can update it, we can update it with 
        if saved_user.id==id: #In this case is not user is justly ID 
            
            #in the moment that found it then we delete it with this operation del and we delete the element of the list that coincide with the indice or be the of if that is what we've found and done the saved in ID 
            del Users_data_Base[index] #we do a deleting operation 
            
            #we found it 
            found = True
    # if we found it then 
    if  not found:

        #if we put a user with some lack and we send in put then it gonna return loc or be lack 
        raise HTTPException(status_code=409, detail="the user wasnt deleted") #the errrors cant be represented so ever if no there's many ways better 
    #in the two we do it up in post and in here equal
    else:
        #we return, in case that get to find it, the user# thie gonna say tof up if the user doesnt exist if we send in thunder
        return {"the user was delete": user}


#here we create a funntion to get save the funtion repeated of query and path or its operation
def user_search(id: int):
    users = filter(lambda user: user.id == id, Users_data_Base) #filter is called funtion of superior order, filter pertenece to a of the funtions that is build in and is of superior order because it encharge of to do complex operations and give back a result
    
    try: #En try start all the drive of the exceptions
        return list(users)[0]

    except:
        return {"error":"didnt find the user"} #we can also return an json with a dictionary and his gonna be in the server#in except we do return of vacume, in this the server gonna give back the ""

#the criteries to get datas usually form part of the URL now we're going to go to oanother operations type 
#we have many operations that form part of the protocole http is the protocole of conmunication that we have in this type of APIS is a standar that allow us conmunicate through internet 
#there's a advantage to use parameters and queries in the URLs we ussually use the path /1 when we considere that is an obligatory parameter 
#the URl may be dynamic or be can to be of differents ways like the /ID without the ? etc etc when ussually goes fix some it hgo in the path and no in the query ussually to use query normally we use it for parameters that are not necessarie to do the petition an example very typical is when we ask a user or a scroll or ask the 10 last publications sure that form part of the URL how a query and the pagination gonna form part of the query like give me the publications of the 0 untill 10 we can to be in the 7 or 8 publication and we ask to the api of the 8 to the 20 is the query is variable that can to change when ussually varia we use it also it cn to do others with query but is a good practce to do it by query in the /users/ is the path but in the /users/"1" is variable users in cahnge is obligatory 
#all this is how in the rutes /users/?ID=1 to concadenar we add & that go after ever of ? /users/?keyword=1&car=0 car is asking the element 1 of car #when we have that concadenar with a query we do example /user/1/?start=1 this say of the first user we want the first user list its start 1 and if we want concadenar or look for more we use &end=10&car=5

#we're going to see the most frecuents like post get put delete because if we understand how work em then we can advance more in backend to do it through of the documentation of fastapi with thi we have the bases
#get is for read datas, post is for create datas also save datas also to create a new user doing case to the api of users of some one form will be it, put is for update dtas of an user will be put because if we wnna change some concret we use a put and if we wanna delete (data) then will do it with delete 

#for what the post react when you send /user/ in postman or thunder you must to put a list User inside with all its datas in body to put it in thunder and to send

#error codes #we can return errors like 404 that didnt find the user this serve for give me count and react
#the messages are important to get interpreate or what the final user can to do some in answer and this is better with a text or a clue or key error 
#if even it return a 200 ok can be that dont return the asked by that we use the http codes 

#In dcumentation search if you want some concret 
#status codes there's codes between te 100 and the 199 to give us answer information 200-299 is for say that the things has gone well 300-399 redirection_messages 400-499 is what there's an error type and the 500-599 is what has petado the server and there's more codes one are sandar and the others let us intuir some with this we can do that the client intuya some because th user see the standar because in there there's no convention is some that we decide to send to the user 
#instead that if we work with the answer codes http there yes or yes we're talking of some tha if is puts bad then is bad, onother thing that you can to do by example is of the 200 and 299 where you can to do with the rest we can use yourself can write your own error codes for your user for what understand that did bad who use your api 
#there's codes much more often than the anothers and in the documentation of fastapi say it, like the 100 with information, 200 what it has resulted well 201 what what it's been created some 204 there's no contain when there's no to give back to the client, 300 tere's redirection,300 redirection, 307 temporal redirection, 304 a name fire, 400 that there's a error, 404 no found, 500 internal error that are mmuch less etc. The 100 doesnt use much and these told are the most used with these would be well to work 

#we create an api for products this of up is for user# remember for can run another api you must to put in uvicorn the new file:app
#we have no reference of the fichero principal of our bacckend by that when we havee run our api we've that to run 'em by separed we've no reference of our apis users no products for what in main we do it our main fichero for to do it we makes a group in main file where are the routers for that we create a new folder called routers where we the routers are all the routers that we can to have or be in our base URL the /users etc and we put the 2 apis files inside this new folder how 2 ficheros# we need to do reference from this fichero users so what if we create an api we've those 2 instances separed for that we create a router instead of an api that is main users etc but in really products in users work in general api or be for us it dont gonna be an api how entity in itself if no it gonna be a router so what in products instead import the FastAPi we gonna import the APIRouter and instead create FastAPI() we create APIRouter() and we call it router and we put in @ the new value instead of app 
# Wev go to the main  file and we import what seem that can work how router like the of products ##GO TO THE MAIN IN THERE IS THE INSTRUCTIONS all this is for what the main fichero is in the file main