import datetime
from fastapi import FastAPI, HTTPException
from yatzy import roll_a_die, roll_the_dice, score_yatzy, create_json_w_scores



####################################################
#                                                  #
#  run api with following command in terminal:     #
#  > fastapi dev app.py                            #
#  followed by clicking link to swagger-docs       #
#                                                  #
####################################################



app = FastAPI(
    title="Yatzy API",
    summary="Et super smart API til at lære om API'er mens man spiller yatzy."
    )

@app.get("/is_alive")
def is_alive():
    return {"message": "Hello, this api is up and running!"}

# @app.get("/average")
# def average(number1: int, number2: int):
#     return {"average": 0.5*(number1+number2))}

# @app.get("/get_squared/{number}")
# def squared(number:int):
#     return {"Kvadratet er": number*number}

# @app.get("/what_time_is_it")
# def now():
#     return {datetime.datetime.now()}

@app.get("/roll_die")
def roll_die():
    return({"Terningekast": roll_a_die()})

@app.get("/roll_n_dice/{number}")
def roll_n_dice(number:int):
    return({"Terningekast": roll_the_dice(number)})

@app.get("/play_yatzy")
def play_yatzy():
    dice = roll_the_dice(5)
    scores = score_yatzy(dice)
    return({"Terningekast": dice, "Score": scores})

@app.post("/calculate_score")
def calculate_score(dice:list[int]):
    # check input
    if len(dice) != 5:
        raise HTTPException(status_code=403, detail="Yatzy kræver præcis 5 terninger. Prøv igen!")
    elif min(dice) < 1 or max(dice) > 6:
        raise HTTPException(status_code=403, detail="Terningeslag skal være mellem 1-6. Prøv igen!")
    
    # calculate scores
    scores = score_yatzy(dice)
    return({'Score':scores})



@app.post("/new_game")
def initialize_game(name1:str, name2:str):
    create_json_w_scores(name1, name2)
    return({'message': f'Nu er vi i gang! Dagens spillere er {name1} og {name2}'})

