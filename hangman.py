import random
import json

def createRandomWord(digits, dup):
    prefix = "/home/sozo/eng_word/"
    file_dict = {
        "3" : "letters03.json",
        "4" : "letters04.json",
        "5" : "letters05.json",
        "6" : "letters06.json",
        "7" : "letters07.json",
        "8" : "letters08.json",
        "9" : "letters09.json",
        "10" : "letters10.json"
    }
    with open(prefix+file_dict[str(digits)], encoding="utf-8", mode="r") as f:
        word_dict = json.load(f)

    if(dup):
        word_list = word_dict["dup"] + word_dict["no_dup"]
        set_word_list = list(random.choice(word_list))
    else:
        word_list = word_dict["no_dup"]
        set_word_list = list(random.choice(word_list))
    return set_word_list

def main():
    set_word_list = createRandomWord(6, False)
    #print("set_word_list : ", set_word_list)

if __name__ == '__main__':
    main()
    pass



def hangman(word):
	wrong = 0
	stages = ["",
			  "_________        ",
			  "|        |       ",
			  "|        |       ",
			  "|        |       ",
 			  "|        o       ",
			  "|       /|\      ",
			  "|       / \      ",
			  "|                ",
		      "|________________"
			 ]


	rletters = list(word)
	board = ["_"]*len(word)
	win = False
	print(" welcome to hangman ")
	while wrong < len(stages) - 1:
		print("\n")
		msg = " Guess the word "
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = "$"
		else:
			wrong += 1
		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print(" You Win! ")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print(" You Lose , The answer is {}.".format(word))


hangman(f"{createRandomWord(6, False)}")





