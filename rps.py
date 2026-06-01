import random
  
def ispis_choice(me_choice,ai_choice):
    print(f" Moj odabir : {me_choice}")
    print(f" Njegov odabir : {ai_choice}")

def ispis_rez(me_score,ai_score):
    print(f"My Result : {me_score}")
    print(f"Bot Result : {ai_score}")


def main():
    choice=["Rock","Paper","Scissors"]
    me_score=0
    ai_score=0
    win=[("Rock","Scissors"),("Paper","Rock"),("Scissors","Paper")]
    lose=[("Rock","Paper"),("Paper","Scissors"),("Scissors","Rock")]
    while me_score<3 and ai_score<3:
        while True:
            me_choice=input("Input (Rock , Paper ,Scissors) :").capitalize()
            if me_choice not in choice:
                print("Nevalidan unos pokusajte ponovno!!!")
                continue
            else:
                break
    
        ai_choice=random.choice(choice)
        
        if (me_choice,ai_choice) in win:
            ispis_choice(me_choice,ai_choice)
            me_score+=1
            ispis_rez(me_score,ai_score)
            
        elif(me_choice,ai_choice) in lose:
            ispis_choice(me_choice,ai_choice)
            ai_score+=1
            ispis_rez(me_score,ai_score)
        else:
            ispis_choice(me_choice,ai_choice)
            ispis_rez(me_score,ai_score)
            
        

    if me_score==3:
        print("Cestitam pobijedio si")
    elif ai_score==3:
        print("Nazalost si izgubio:(")

if __name__ == "__main__":
    main()