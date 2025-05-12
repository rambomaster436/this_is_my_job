#api of basic authentications for users 

#URL local: http://127.0.0.1:8000

#these system of authentification are standar it does in all the backends mounted with all the languages #there's organisms of security and standars that encharge of define how must to work all this equal that the procoles http but the standar serve for what all the languages can understand it and be easy adapt it to anyone laguage etc this standar gonna serve for all also the concept of authentication the api concept authorisation concept or be the learned are generals
#for a best working we translate the server to router folder in the terminal in we gonna mount this api without what it be a router how such at least initially for work only with users api for that we do the next

#We import the FastAPI etc of things what we need #if we wanna work with status we must to import status class and inside of status or be status. we have all the codes also of answer code
from fastapi import FastAPI, Depends, status
from fastapi import APIRouter, HTTPException
#we import the BaseModel for the fichero from pydantic 
from pydantic import BaseModel
#we import for security the 2 auth the first for the password and the user and the next for the form in what the backend gonna capture that user and key
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#we define our app how class FastAPI #we use the APIRouter instead Fastetc for a better optimisation
router=APIRouter()

#once imported the OAs we have a form of to implement that critery of authentication so what equal that we've a tht we have an instance of app that is of the own api we gonna create an instance of our authentication system that we gonna call oauth2
#we could call to our api "/login" pass it the user and password and what next our backend decide if we are indentified or no we gave tha name login and in the the sef we put the operation of authentication
oauth2 = OAuth2PasswordBearer(tokenUrl="login") #this is our critery pof authentication and the class that that ghonna encharge of manage our authentication is the OAuth2AuthorizationCodeBearer(here go the URL that it gonna encharge of manage the authentiction int this case tokenURL="login") #oauth is a standar that say us how we must to work with authentication in a backend 

#we have already an api of users so what we cn run the server uvicorn
#how we gonna to work with users we gonna retake of the class user() name for down , to work with users the form is redefine the of class User(BaseModel) os api users also it might reuse the of users for what it quiet well defiend we redefine in this fichero ii gonna have some different
#here the use gonna return yet we dont wanna return the password so what we have the what is the user and by other side how would the user of data base so what we dont put to the class User we dont put password and by that we do it very simple
#this entity user created gonna go a little throught the net 
class User(BaseModel): #the BaseModel gives us certain mechanism for what this object that we defined how a class it can to pass throuth of the net of a way very easy and it can transform in a json of there it can transform to a class and to the final we cn to work in python and by other side sith all the protcole http what we have mounted for it the o down
    username: str #
    full_name: str
    email: str
    disabled: bool #disabled is desactivated bool only accept a 1 or 0 or False or True

#in the rality we work with this api but with a real data base #in our data base we can to have a data base no relacional can to have differents users 
#data base 

#equal that we have an user for up also we've an entity that should represent to the user of data base or be the class where the data base user is userDDB(where we impliment the User) is the same that the user yet has additionally has more than the user of up is the password of type string so with this we have a form of define to the user how such to the user what we gonna work with it by net and to the user of data base that has all the user by that we're hereding of User(BaseModel) of up that apart of all the of User has the password  
class userDDB(User): #this is the entity that represent to the data base user and is of type User
    password: str

#we gonna work with an operations aditionals #we gonna create a mechanism for what in the moment that call to us this api can to search if in this database is our user 
#in data base no relational the users a little its structures of that type of data bases are how json to the final we have keys and values and in the part of down we have the types of datas of user of the class User 
userses_db ={   #once we have an object that has these datas surely these data bases has that to be saved of some one way so what we gonna create all the elements of the data base and define em how they'd be and we add one more 
    #remember the username in thunder is the name of the list keep seems
    "mouredev": { #this is a list an array of differents users that this is representa the data base 
         #datas of user 
        "username": "mouredev", 
        "full_name": "Juanpapiriky",
        "email": "Juanpapiriky@gmail.com",
        "disabled": False,  #For if is disabled or not, this is very typical when we're working with users in data bases because any times the only what we wanna do is to put a flag that says this user is able or disabled beacuse he's deleted is restringed etc 
        "password": "4321"   #A password we cant save in data base in clear it should apply a has or some seemed for what when someone reach to our data base the password gonna be encripted so what the hacker dont gonna see the passwor to steal it to evit that we must hasearla so what with a seed or a encript toolwe protect the password #here if we wanna work with users and passwords we must save their password is this for what the user get authentic self 
    },
    "mouredev2": {
        "username": "mouredev2", #
        "full_name": "layout",
        "email": "layout@gmail.com",
        "disabled": True,  # we change this False for a True for what this user is disabled #with dissabled in True say us that the user is unactive #the dissabled mean that the user is disactivated or dissabled 
        "password": "1234"  #in this we gonna start to work with authentication 
    }

}

#also we have another type of authentication surest like of the type jwt we gonna create a new fichero authenticating it of another way with jwt besides int this jwt it does with the oauth with password using the token jwt or be it works with encriptation we dont pass the token how here in this we go really to a type of authentication oauth of type bearer with a token jwt the jwt also is in fastApi documentation #the new file or fichero isb in up is jwt inside router 

#operation for what it search if in our data base is their user wished and in this searchUser the only that we gonna pass is the name of user or be the username that is a str this is necessary typear becuase this is FastAPI because it work much better with it 
#part of authentication standar simple normal  
def searchUser_db(username: str): #with this it connect with the server or be the parameter 

    #For to search if we have the user in some one side is to run all the data base with if 
    if username in userses_db: #what we are finally doing here is retreiving the user and we gonna return it
            
            #with the return we can search already it #of this way we've transformed that critery in an user of data base with this we can obtain already
            #when we try of to post the username and the password in /login thunder body form it send a internal server error a 500 or be this has petado because this is not working no matter if you send the user.. right or the pass.. eveny it sends us that that is because it is failing in this creation of down by that we put the ** in (**userses) once puts this this gonna work and gonna return acces_token and a token_type, to do this call to create it the UserDDB here we're not saying it in really how it's that to create simply is a class with the BaseModel we're indicating nothing more is to say that we can to send em differents parameters and with these ** we indicate the nmber abitrary of parameters how it's that to create the UserDDB(User) the inside BaseModel funtion that is not in this module the representation metaclass=ModelMetaClass in really we could to pass it a huge of parameters by that we must indicate it what in userses_db can to go severals now it'll work well 
            return userDDB(**userses_db[username]) #we create the userDDB( and we pass here is of our data base user_db[the user that coincide with the key defined or be username])
            #we need a a operation that be capable of authenticate us here goes the concept of authentication inside fastapi this we get importing the classes OAuth2PasswordBearer that is the protocole of authentication that we gonna use this gonna encharge of gestionate the authentication the user and the password that it gonna authenticate in our system and we gonna authenticate the OAuth2PasswordRequestForm that is the form in what it gonna be send to our backend to our api these criteries of authentication is to say the form in what we must to send from the client the user and password and the form in what our backend gonna capture that that user and password for see if really is an user of our system from fastapi.security  

#with this operation we get the return well in the thunder the user that we asked or be the right withou the password 
#we'll have that to create the user of type User and no userses_ , we can to create with the same datas of before but only to create it of type user
#operation searcher that return the user of type User in case that was so 
def searchUser(username: str): #with this it connect with the server or be the parameter 

    if username in userses_db: #what we are finally doing here is retreiving the user and we gonna return it
            
            #In case that dont lack us we dont call to the user of data base user and we return an  User no more 
            return User(**userses_db[username])

#operation for do the critery of dependence of me  funtion in down
async def current_user(token: str = Depends(oauth2)): #this funtion serve for to do the critery of dependece of operation me doing that fulfill what want that full the operaion me
    
    #the searchUser is creating an user data base type then the 1 that we could to do is this search and also the testing of if the user is activo or not before of nothing 
    #we to start to consume our api we must to do or our api must start to consume it once that it has generated a token once it has authenticated rightly and return us the access token now we'll have to valid if tha access token is right how ware using the system of authenticattion OAuth2PasswordBearer we know what ever we must to expect is a token so what the what it must to have is a (token of type str ever typear it =this has a dependence for obtain the token depends(the token will have that to search inside our system of authentication who is the OAuth2 that has managed a token that we've obtained in the login and that is of type PasswordBearer so what depends(oauth2) this mean that we depends of oauth2)) in the funtion async and how we depend of this and this is a system that is capable of to capture the token that to reach to our api then now we'll can to access to the token theoritically we gonna have a token of type string  in case that the system valid it 
    #we return the search if really has found to the user inside of the data base and if it doesnt find we can to drive 
    user = searchUser(token) # return operation it can also to get of the data base the token because it is the user of our data base or coincide with our data base so what we put  searchUser(token)#to obtain the user for to know if it's well or not this we create an user = with an operation that search in the data base this time we reuse because we had already one funtion so#theoritically we have a token of type str in this case in case that the system valid it and case that it doesnt valid it fastapi gonna do all authomatically if doesnt valid it it'll says that didnt valid it and if has valided well will go in the operation and we'll can do things 

    #testing if really it has found it not
    if not user: # if has the user we return it if hasnt it then we'll launch an exception well concret with its headers that is not used
        
        #if we wanna use status in status_code= then we need to import status from fastapi#we launch in status code status and by its inside we put the answer code that is in this case the 401 or be status.the 401 because is more easy to work with status we put this also in all the rest 
        #in details we put that the credentials of aunthentication are invalids and we can also launch headers headers= inside headers goes in a standar the standar of the type of header and the autthentication type that has been used for what we get a little of information in header we put inside a set example ={"www-autheetc": "type Bearer"} for what it know what we're making here
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="credenciales de autentcacion invalidos", 
            headers={"www-Auhtenticate": "Bearer"} ) #401 mean that we're not autorizated or be we are authenticated but are not autorizated if wanna use or to access to status in status_code we must to import from fastapi another class that is status by if we wanna to work with it
    
    #we have some bad still by here that still we were not capable of to create an user ho such so what we'll have that to search the way of to create an user and create it that be of type User that dont be of the type userses_db
    #this is for solve the problem of that return things that dont should the /users/me 
    #imaging if the user is dissabled then we can to put another error 
    #here the user it's been found but we convalidate if the user is dissabled then we could return an error in this case a 400 because is a bad request in detail we put unactive user also to have in count that flag and in case against return the user  
    #if user is dissabled then it sends the error 
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="unactive user")
 
    #returning the user if has been found the user 
    return user
#operation of authentication equal how we had the api 
#/login is where we shall to put the user and the password #for call to this operation we call it in thunder /login, if we wanna call first to /users/me it gonna return not authorized
#1 /login in thunder is the first operation that we must to call because we must authenticate in it
#we need to pass it in this operation the user and the password  for get the token when wew out /login is following already the authentication critery auth, to send the user and the other we send em in auth in thunder evenly in body these have differents forms of to send the information in Auth o down of the link has Bearer etc in body has to form what is the way that we gonna to pick and this form says pass me differents camps what are in this case username and password you just need to put username in field name and ready it open for to put another camp and in the values we put the values that we wan to sign up  or be field name and its value to the next this is the form of to post the u and the p but first test with anyone of the data base
#if it work well then it'll return an access_token and a token_type: bearer and if you dont pass the right password then return the detail puts if not form.password
#once obtained the token in an aplication the access_token its value we must save it because if we wanna call to anyone authenticated operation and to know if we're authorizated to invocate it we'll have that to pass it the token and we wont have that to pass it continually user and password so what if we want can once obtained the acces_etc we can desactivate them with push the well and to let empty to dont pass it more the user etc, it says that the authentication tha we're calling gonna be of type bearer and the token is mouredev then now since is a standar we'll have that to call with an authetication of type bearer and the token of this way we'll call, one authenticated operation that we've is /user/me remember dont put a / of more
@router.post("/login") #in this operation is of type authentication where we pass it user and password by that we use the operation post that ussually it use because we gonna pass it datas to gets datas the URL where we gonna expose this operation of the api is the login

#it can authenticate the user in login but can that is not authorizated how the mouredev2 this can to pass in the case that in what an user is authenticated but not authorizated because is unactive the user then you can to do the login but it doesnt gonna let you to access to your datas of user because the user is unactive and inside the critery of dependence of to obtain ourselve datas in /users/me, some that we control is that the user is not unactive or desactivated dissabled
#we have that capture the user and the password we do it throught OAuth2PasswordRequestForm there's another ways of to send datas but we do it through this formulary that gonna have 2 camps user and password 
async def login(form: OAuth2PasswordRequestForm =Depends()): # we capture a parameter called form: what gonna be of type OAuth2PasswordRequestForm or form and the next important is what we gonna say it that the OAuth2PasswordRequestForm by defect gonna come of Depends(): for that we import Depends from fastapi together with FastAPI depends serve for when we have that to see if the parameters how if we area authenticated or not for to access to the user or if we can to do some one thing there is where go in the depedence by example the dependence for modify datas gonna be that we're authenticated or not and what are authentication with the credencials rights or be more or less how and if it work in our case this depends mean tht the operation gonna receive datas but dont depends of no one 
     
    #with down we obtain the user or we try to search it what is in in userDDB or be we may to search it in there with with the username that reach but we make it with form. what how it is of type OAuth2PasswordRequestForm we've inside of the formulary is paremeters how the id client_secret this can be because also can be necessary to abarcar this authentication in our case gonna be the user and password and we put in this username
    #if the user is valided welll then pass to password if no gets loose the detail how answer 
    user_db=userses_db.get(form.username) #once we've form.username can we start to test if really we have an user with user_db or be we gonna search in our data base if really is this user without to reach to transform it that we get with users_db.get(form.username) with the get we really search if is that user 

    #conditionals to allow the acces or not or return if exist the user or not
    if not user_db: #if doesnt exist the user posted then is not in the data base  
            
        #in here with raise it stop the execution here we can to search in data base and even we might to transform it in an user of data base int this class that we gonna control 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="el usuario es incorrecto") #launching the exception in this case and sopping the execution with the raise it can and the status code we defined it how a 400 the message is what the user hasnt been foundwith that we have a ewxception catched

    #we call to the user of data base in the case that does lack us that was here 
    #the next is what we can to have already an user how such and for that we have this operation searchUser we might to pass it straightly or to do this operation and already to try to search it to call to searchUser(here we pass it the form.username) now with this it gonna can return the user 
    user=searchUser_db(form.username)#here we have already the user or it return the user with this operation they give us the user if pass the others conditions in parameters goes the (form.username) for what now if return the user
        
    #testing the password that has reached us coincide with this user of data base that is user
    #if the password is valided well then return the token if no then it shows the detail
    #here the form.password is the password of data base and the user.password is the password passed 
    if not form.password==user.password: #here we test that the password that has reached in form.password is equal to the user from to the user of database its password .password if is equeal then the user has been authenticated rightly and if not we launch an exception with the funtion
        
        #instead to launch to hand the status_code we launch it with status in really this just it correspond with a string but is a way of to see it of a way more visual or if we dont remember of the anwers codes well we can to put im em by here  
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="la contraseña es incorrecta") #launching the exception
    
    #here we have the operation of authentication
    #if really we proved the password and the user then we must return that really we've found the user and the password the of up user= this we might return, in these cases ussually it does or the way that it work in this type of authentication of type auth is what in the moment that the user be authenticated rightly what has that return the system is the called the axestoken this work so by standar we by that we created a Json that we gonna return by a side access_token, and by other return of what type is the token that is inside of a camp that it calls "token_type" and the type of token that we gonna return it calls "Bearer" that also form part of a standar and equal that we're talking about that the authentication that gonna to manage is the of OAuth2PasswordBearer is beacuse now we gonna return a token of type bearer because this also inside the protocole http it pass of a way very rifgth and very concret we would lack define what's the token the token should be some encripted some that known by the backend the token is for dont be continuely authenticatin self the token serve for when te user pass well the user and the password without the token we need to pass every time that i wanna call an operation would have that to pass the user and the password thing very akward for the user like the delete user etc of the moment with the toke_type is enough and jwt we will see after but starting by this part we would have that to pass it some that really we can to be resending coninuely to the backend and what this dont be an user and password if not it'b a shit but after of to pass it the user and the password is what we can to say how backend is what once passed the user and the password then ever that the user pass some that is right then must to pass the datas how you're authenticated the what it ussually return some encripted in this case the token gonna be the own user so user.username so what if you're authenticated rightly the  authentication token gonna be the own name of the user and when it pass how authentication token the own name of the user for me gonna be well
    return {"access_token": user.username, "token_type": "bearer"} #we launch the password of the user of the data base #if the user athenticate self rightly the authentication token gonna be the own name of the user and when it pass how authentication token the own name of the user gonna be well no se suele to do all with encripted parameters 

#implementation of operation that give us datas of users once authenticated
#if we wanna call to /users/me in thunder it gonna return not authenticated  because is being directly managing by it because the dependence critery is indicating already that hasnt been passed no one token it doesnt know how toauthenticate you by that the first that we've that to obtain is a token in login for that you need to pass it in a for is the user and the password
#remember no a / of more#if we post the username and the password well and we try to get the /users/me then it still dont gonna atuhorize it because it has a dependence the current_ and this dependence the 1rst that makes is to depend of the authentication system (oauth2) that still hasnt done nothing then to try to search this user dont worth or be no reach to /users the reason because it says not authenticated and get us an unauthorized is because when we call to this operation we should to pass it a token and its type in Auth down Bearer or be int the Auth inside we must to choose the type in this case is Bearer thanks to this we jusst need to pass it the username since that we put how the token if we pass it bad then it gonna return the detail of current_user and if it's right then return the datas of the username list, the detail of the current_ mean that to the to search an user with the token unright hasnt found and it launched the exception remember that we pass it headers the www- etc for what we follow knowing that happen with this type of authentication to pass the header we must to put in Headers down of the statusand to choose the www_etc next Bearer, when we put well the token in auth return also things that dont should like the password to solve this we can to use the dissabled since with it we can to see some we use in searchUser, though we told here that the user depend of current_etc what we've give back by user=search_user is a search_etc that is creating is an user but of data base type 
@router.get("/users/me") #get("/user/me")this path is for what once authenticated us what's my user 

#operation
#the current_user we use here how dependence critery in this depends we dont gonna have an user so really if our current_user is not capable of return an user what is searched in current_user following the authentication critery in base to the token that we've released   
async def me(user: User = Depends(current_user)): #the criteries of dependence mean that we can implement operations that validen this sign user: User = Depends() now even this is not valided beacuse this user: etc dependence(there's no dependence) still hasnt dependence by that we put in up of operation post a funtion async for to put the citery of dependence that help us to valid the way async is because it gonna to execute equal that this operation of this row and this dont gonna be with an operation exposed in the api or be app.operation if no this gonna be a critery of dependence and we call it current_user because we speak of me #here we return the user with the concept of dependence #we indicate that it gonna calculate of some one form an user of type User of up where we had an object user that dont return the password because if we return by net on object of user with password that is a brech of security huge by that we've 2 users 1 of data base that has the password and other to entity level that hasnt the password being this what we gonna return, now we put the part of dependence this operation depend of what the user is autheticated in this case the the criteries of dependence are user: User = depend or be the user etc depends of what the user is authenticated 
     
    #implementation if really we can obtain to this user inside of the implementation
    return user# returning the user giving it how it gonna work 
#the process of calls 
#thunder client is a client for to perform calls to an api
#after we'll desplegate in a real server and about data base 