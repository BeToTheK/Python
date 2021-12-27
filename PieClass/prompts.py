from question import Question

question_prompts = [
	"What is my name?\n(a) bk\n(b) notbk\n(c) senpai",
	"How are you(youre bad)?\n(a) good \n(b)bad"

	]

questions = [
	Question(question_prompts[0],"a"),
	Question(question_prompts[1],"b")]

def run_test(questions):
	score = 0 
	l=[]
	for q in questions:
		answer =  input(q.prompt)
		if answer == q.answer:
			score +=1
		else:
			l.append(q.answer)


	print("you got "+ str(score)+ "/" +str(len(questions)) + "correct")
	return l
run_test(questions)