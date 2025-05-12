#api for products

#Now instead of import FastAPI we import APIRourter 
from fastapi import APIRouter

#with this is more understandable 
#all this we can to centralizar with the router etc we could to make differents things but we initially or if we want we can to make of that way then we create a router now in users_db in the part of the router = abd we copy this of down o be the router of here to put it in the router of there
#And instead of to create FastAPI() we create APIRouter() #And for dont call it app we call it router in really we can call how we want
#In APIRouter there's an operation that is prefixwhere the prefix will be products for what we havent to indicate which is in the prefixes in the roperations router in down () so what we just need to put so .get(/) by defect they know what is the prefix besides in the operations or funtions we just put ()
#with the prefix stablished we dont need repeat in the rest we just put "/" how parameters #remember response is an answer code by if there's a problem or it need to send a message reponse must be a dictionary, in this case is responses={404: {"message": "no found"}}) and this now form part of our api
#adnd to do it some we've also some called tags= where we put how value ["products"] the same how list
#Now with this tags in docs of google it gots to divided we've some by defect what have all that we didnt delimitate what is in really the api of users and our normal api now appear all the operations like the root url etc the /user also might be divided besides we have products now because on products we've indicated that have the tags  if we take off the tags in docs the products dissapear and it become in default withb tags we say that all be /products besides for the the documentation that group em in docs tags is for group in documentation so what in docs appears separed the products instead of the default also with that we've information own of the products  
router = APIRouter(prefix="/products",tags=["products"] ,responses={404: {"message": "no found"}}) #now we have a new api of products#this app = etc serve for stablish the @app.etc remember #all the prefix is for the router 

#we define the list 
products_list=["mandarinas", "papas", "yourold"]

#when we talk about a router is ussual that all have the same path

#this funtion return all the products
#In really app could be anyone that we puts how saver in APIRouter 
@router.get("/")

async def products():

    return products_list

#This return by ID
#we make another with the parameter or path /{ID}
@router.get("/{id}") #how is router with the prefix "/products we just need to put here "/{ID}" pithon assume by defect that the prefix is /products/

async def products(id: int): #ID how an int

    return products_list[id] #we return the list with the ID that reach of the thunder body with [ID] #This is justly a test 

#also it could to use graph UL where in standar the biggest part are api rests 

#we do a data base autenticationthe documentation it does automatically in python in swagged and no only documentation with swagged if no with redoc besides