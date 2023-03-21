import re  # imports Regular Expression package for error handeling


class QuestionSet():
    '''Compiles a question string, answer, and answer length together.
    
    Parameters
    ----------
    prompt: string
        String of the question to be asked.
    answer: string
        String of the answer to the prompt.
    length: integer 
        Number of letters in the answer.
    
    Returns
    ----------
    None
    '''
    
    def __init__(self, prompt, answer, length=1):
        """Inits QuestionSet and assigns each object 
        a prompt, answer, and length.
        """
        self.prompt = prompt
        self.answer = answer
        self.length = length
        

# String list of the questions 
# for the first question set
question_prompts_1=[
    "How many times a year does the average human eye blink?\n(A) 1 million\n(B) 5 million\n(C) 25 million\n(D) 100 million\nYour Answer: ",
    
    "\nWhat is the only animal on earth where the male carries the unborn offspring?\n(A) Cuddlefish\n(B) Giant Squid\n(C) Lobster\n(D) Seahorse\nYour Answer: ",
    
    "\nWhat organelle, found in the cytoplasm of living cells, has the function of protien building from amino acids?\n(A) Ribosome\n(B) Golgi Bodies\n(C) Mitochondria\n(D) Nucleus\nYour Answer: ",
    
    "\nAll amino acids contain carbon, hydrogen, oxygen, and what other element?\n(A) Fluorine\n(B) Potassium\n(C) Sodium\n(D) Nitrogen\nYour Answer: ",
    
    "\nWhat is the more common term used to describe ectothermic animals such as turtles, toads, and tarantulas?\n(A) Warm Blooded\n(B) Amphibians\n(C) Cold Blooded\n(D) Arachnids\nYour Answer: ",
    
    "\nWhat word refers to an individual organism's observable traits?\n(A) Phenotype\n(B) Genotype\n(C) Karyotype\n(D) Allele\nYour Answer: "]


# String list of the questions 
# for the second question set
question_prompts_2=[
    "What is the more common name of the world\'s most simple animal from the phylum Porifera?\n(6 Letters)\nYour Answer: ",
    
    "\nWhat is the name of the neurotoxin produced by the bacterium Clostridium botulinum?\n(5 Letters)\nYour Answer: ",
    
    "\nFor an X-linked gene, only the genotype of what parent matters for XY trait inheritance?\n(6 Letters)\nYour Answer: ",
    
    "\nWhat is the name used to describe a type of chromosome whose centromere is located at one end?\n(11 Letters)\nYour Answer: ",
    
    "\nWhat type of dominance is used to describe an intermediate phenotype?\n(10 Letters)\nYour Answer: ",
    
    "\nWhat is the name of the type of single-celled protist known for its slipper shape\nand covered in short hairy structures called cilia?\n(10 Letters)\nYour Answer: ",
    
    "\nFrequently used in labs, roundworms are also known by what name derived from the Greek word thread?\n(8 Letters)\nYour Answer: ",
    
    "\nWhat is the name of the genetic structure, typically circular in bacteria, that can replicate independently of the chromosomes and is commonly used as a vector in genetic engineering?\n(7 Letters)\nYour Answer: ",
    
    "\nWhat fight or flight hormone is released in the body by the adrenal gland?\n(11 Letters)\nYour Answer: ",
    
    "\nWhat is the last name of the famous biologist who published the Origin of Species in 1859?\n(6 Letters)\nYour Answer: "]


# String list of the questions 
# for the third question set
question_prompts_3=[
    "We want to store a set of DNA sequences for a study.\nWhich data structure is the best for this purpose?\n(A) string\n(B) bool\n(C) list\n(D) dict\nYour Answer: ",
    
    "\nWhat is the output of the following code: 1) RNA = “UCGUAC” 2) DNA = RNA.replace(“U”,”T”) 3) print (DNA)\n(A) TCGTAC\n(B) AGCATG\n(C) AUGAUC\n(D) UCGUAC\nYour Answer: ",
    
    "\nAs a part of a research study, you have been given a protein sequence to analyze.\nWhich function would you use to find the number of specific amino acids present in the sequence?\n(A) find()\n(B) sort()\n(C) index()\n(D) count()\nYour Answer: ",
    
    "\nYou want to find the length of a DNA sequence.\nWhich function would you use? \n(A) len()\n(B) count()\n(C) sum()\n(D) append()\nYour Answer: ",
    
    "\nWhich of the following Python libraries would you use when analyzing structured and labeled data?\n(A) matplotlib\n(B) numpy\n(C) biopython\n(D) pandas\nYour Answer: ",
    
    "\nWhich of the following libraries would you use for creating plots of gene expression data?\n(A) biopython\n(B) matplotlib\n(C) numpy\n(D) pytorch\nYour Answer: "]


# List of all the compiled questions for the 
# first problem set using the QuestionSet class
multiple_choice_questions=[
    QuestionSet(question_prompts_1[0],'B'),
    QuestionSet(question_prompts_1[1],'D'),
    QuestionSet(question_prompts_1[2],'A'),
    QuestionSet(question_prompts_1[3],'D'),
    QuestionSet(question_prompts_1[4],'C'),
    QuestionSet(question_prompts_1[5],'A')]


# List of all the compiled questions for the second 
# problem set using the QuestionSet class
response_questions=[
    QuestionSet(question_prompts_2[0],'SPONGE',6),
    QuestionSet(question_prompts_2[1],'BOTOX',5),
    QuestionSet(question_prompts_2[2],'MOTHER',6),
    QuestionSet(question_prompts_2[3],'TELOCENTRIC',11),
    QuestionSet(question_prompts_2[4],'INCOMPLETE',10),
    QuestionSet(question_prompts_2[5],'PARAMECIUM',10),
    QuestionSet(question_prompts_2[6],'NEMATODE',8),
    QuestionSet(question_prompts_2[7],'PLASMID',7),
    QuestionSet(question_prompts_2[8],'EPINEPHRINE',11),
    QuestionSet(question_prompts_2[9],'DARWIN',6)]


# List of all the compiled questions for the third 
# problem set using the QuestionSet class
python_multiple_choice_questions=[
    QuestionSet(question_prompts_3[0],'A'),
    QuestionSet(question_prompts_3[1],'A'),
    QuestionSet(question_prompts_3[2],'D'),
    QuestionSet(question_prompts_3[3],'A'),
    QuestionSet(question_prompts_3[4],'D'),
    QuestionSet(question_prompts_3[5],'B')]
    
    
def trading_phase(tokens, correct_counter):
    """
    Simulates a trading phase for our trivia game where the user can choose to trade (buy or sell) correct answers for tokens.

    Parameters:
    tokens (int): The number of tokens the user has.
    correct_counter (int): The number of correct answers the user has.

    Returns:
    A tuple containing the updated values for tokens, correct_counter, and quiz_percentage_1, quiz_percentage_2, and quiz_percentage_3.
    
    Description: 
    The function prompts the user to choose one of three options: buy a correct answer for 60 tokens,
    sell a correct answer for 20 tokens, or do nothing and continue. If the user chooses to buy a correct
    answer and has enough tokens, the user's token count decreases by 60 and correct_counter increases
    by 1. If the user chooses to sell a correct answer for 20 tokens and has at least one correct answer to sell, 
    the user's token count increases by 20 and correct_counter decreases by 1. If the user chooses to do nothing, 
    the function returns without changing the values of tokens or correct_counter. 

    After any of the three options are chosen, the function calculates the quiz percentages for the three
    different sets of questions and returns a tuple containing the updated values for tokens,
    quiz_percentage_1, quiz_percentage_2, and quiz_percentage_3.

    """
    # Print the trading phase message and display the number of tokens the user has
    print("\nTrading Phase:")
    print("You have {} tokens.".format(tokens))
    
    # Prompt the user to choose one of three options
    # Save their input in the variable "choice"
    choice = input('Would you like to:\n1) Buy a correct answer for 60 tokens\n2) Sell a correct answer for 20 tokens\n3) Do nothing and continue\nEnter 1, 2, or 3:')

    # This while loop ensures that the user enters a valid choice of 1, 2, or 3 for the trading phase. 
    # The re.match() function checks whether the input matches the pattern "^[1-3]*$".
    # If the input does not match the pattern, the loop continues until a valid choice is entered.
    while not re.match("^[1-3]*$", choice):
        print("Invalid choice. Please try again.")
        choice = input("Your choice: ")
    
    # Ensure the user's input is a single digit
    while len(choice) != 1:
        print("Your response isn't the correct length! Please try again here\n")
        choice = input("Your choice: ")    
    
    # Convert the user's input to an integer
    choice = int(choice)
    
    # If the user chose option 1, attempt to buy a correct answer
    if choice == 1:
        # Check if the user has enough tokens to buy a correct answer
        if tokens >= 60:
            # Decrease the user's token count by 60 and increase their correct answer count by 1
            tokens -= 60
            correct_counter += 1
            print("You bought a correct answer. You now have {} tokens.".format(tokens))
        else:
            # Inform the user they do not have enough tokens to buy a correct answer
            print("You don't have enough tokens to buy a correct answer.")
    
    # If the user chose option 2, attempt to sell a correct answer
    elif choice == 2:
        # Check if the user has any correct answers to sell
        if correct_counter > 0:
            # Increase the user's token count by 20 and decrease their correct answer count by 1
            tokens += 20
            correct_counter -= 1
            print("You sold a correct answer. You now have {} tokens.".format(tokens))
        else:
            # Inform the user they do not have any correct answers to sell
            print("You don't have any correct answers to sell.")
    elif choice == 3:
        # If the user chose option 3, do nothing and continue with the game
        print("You chose to do nothing.")
        
    # Calculate quiz percentages for each set of questions
    quiz_percentage_1=round((correct_counter/len(multiple_choice_questions))*100,1)
    quiz_percentage_2=round((correct_counter/len(response_questions))*100,1)
    quiz_percentage_3=round((correct_counter/len(python_multiple_choice_questions))*100,1)
    
    # Return a tuple containing the updated values for tokens, quiz_percentage_1, quiz_percentage_2, and quiz_percentage_3
    return tokens, quiz_percentage_1, quiz_percentage_2, quiz_percentage_3


def game_set_1(multiple_choice_questions):
    '''Asks the user the questions from the inputed parameter question set while grading the responses. 
    
    Parameters
    ----------
    multiple_choice_questions: variable
        List of all the compiled questions to be asked to the user for the first problem set.
        Each index uses the QuestionSet class.
    
    Returns
    ----------
    correct_counter: integer
        The number of correctly answered questions from the completed set. 
    '''
    
    correct_counter=0
    
    for question in multiple_choice_questions:
        answer=input(question.prompt)
        
        # Error handeling, incase the user puts multiple letters in
        while question.length != len(answer):
            print("Your response isn't the correct length! Please try again here\n")
            answer=input(question.prompt)
            
        # Uses Regular Expression method .match() to determine 
        # if the user's response matches one of the specified 
        # characters for error handeling    
        while not re.match("^[a-d]*$",answer.lower()):
            print("It looks like you've chosen an invalid response. Please try again here\n")
            answer=input(question.prompt)
        
        if answer.upper()==question.answer:
            correct_counter+=1
            
    return correct_counter


def game_set_2(response_questions):
    '''Asks the user the questions from the inputed parameter question set while grading the responses. 
    
    Parameters
    ----------
    response_questions: variable
        List of all the compiled questions to be asked to the user for the second problem set.
        Each index uses the QuestionSet class.
    
    Returns
    ----------
    correct_counter: integer
        The number of correctly answered questions from the completed set. 
    '''
    
    correct_counter=0
    
    for question in response_questions:
        answer=input(question.prompt)
        
        # Error handeling. Gives the user another chance incase they 
        # accidentally spelt their input wrongly  
        while question.length != len(answer):
            print("Your response isn't the correct length! Please try again here\n")
            answer=input(question.prompt)
        
        
        if answer.upper()==question.answer:
            correct_counter+=1

    return correct_counter


def game_set_3(python_multiple_choice_questions):
    '''Asks the user the questions from the inputed parameter question set while grading the responses. 
    
    Parameters
    ----------
    python_multiple_choice_questions: variable
        List of all the compiled questions to be asked to the user for the third problem set.
        Each index uses the QuestionSet class.
    
    Returns
    ----------
    correct_counter: integer
        The number of correctly answered questions from the completed set. 
    '''
    
    correct_counter=0
    
    for question in python_multiple_choice_questions:
        answer=input(question.prompt)
        
        # Error handeling, incase the user puts multiple letters in
        while question.length != len(answer):
            print("Your response isn't the correct length! Please try again here\n")
            answer=input(question.prompt)
        
        # Uses Regular Expression method .match() to determine 
        # if the user's response matches one of the specified 
        # characters for error handeling
        while not re.match("^[a-d]*$",answer.lower()):
            print("It looks like you've chosen an invalid response. Please try again here\n")
            answer=input(question.prompt)
        
        if answer.upper()==question.answer:
            correct_counter+=1
            
    return correct_counter


def play_game():
    """
    This function runs the entire trivia game, which consists of three rounds of questions and trading phases 
    after each round. The player starts the game with 100 tokens and must earn or trade enough correct answers 
    to advance to the next round.
    
    Parameters:
    None.
    
    Returns:
    None.

    Description:
    The function starts by initializing the player's tokens to 100. It then calls the function `game_set_1()`, which 
    takes a list of multiple choice questions and prompts the player to answer them. It returns the number of correct 
    answers as `correct_answers_1`. The function `trading_phase()` is then called with the player's tokens and 
    `correct_answers_1` as input. It returns updated values for `tokens`, `quiz_percentage_1`, 
    `quiz_percentage_2`, and `quiz_percentage_3`.

    If the player's score is at least 80% on the first quiz, the function congratulates the player and moves on to 
    the next round. Otherwise, it informs the player that they did not pass and returns.

    The function then calls `game_set_2()` with a list of response questions as input. It returns the number of correct 
    answers as `correct_answers_2`. `trading_phase()` is called again with `tokens` and `correct_answers_2` as input. 
    It returns updated values for `tokens`, `quiz_percentage_1`, `quiz_percentage_2`, and `quiz_percentage_3`.

    If the player's score is at least 60% on the second quiz, the function congratulates the player and moves on to 
    the next round. Otherwise, it informs the player that they did not pass and returns.

    The function then calls `game_set_3()` with a list of Python-related multiple choice questions as input. It 
    returns the number of correct answers as `correct_answers_3`. `trading_phase()` is called again with `tokens` and 
    `correct_answers_3` as input. It returns updated values for `tokens`, `quiz_percentage_1`, `quiz_percentage_2`, 
    and `quiz_percentage_3`.

    If the player's score is at least 50% on the third quiz, the function congratulates the player and ends the game. 
    Otherwise, it informs the player that they did not pass and returns.

    """
    # Initialize the tokens variable to 100
    tokens = 100
    
    # Start the first round of the game by calling the game_set_1 function and passing the multiple_choice_questions list
    # Store the number of correct answer's the user achieves in the "correct_answer_1" variable
    correct_answers_1 = game_set_1(multiple_choice_questions)
    
    # Run the trading phase based on the token count and correct answers count from the first round
    # Update the tokens and quiz percentages based on the user's responses in the trading_phase function
    tokens, quiz_percentage_1, quiz_percentage_2, quiz_percentage_3 = trading_phase(tokens, correct_answers_1)
    
    # Check if the user has scored 80% or more in the first round to move to the second round or return a message and stop the game
    if quiz_percentage_1 >= 80:
        print("Congratulations! You passed the first round with {}%. The second round will now begin...".format(quiz_percentage_1))
    else:
        print("Sorry, you did not pass the first round with {}%. Run the cell again to start over.".format(quiz_percentage_1))
        return
    
    # Start the second round of the game by calling the game_set_2 function and passing the response_questions list
    # Store the number of correct answer's the user achieves in the "correct_answer_2" variable
    correct_answers_2 = game_set_2(response_questions)
    
    # Run the trading phase based on the token count and correct answers count from the second round
    # Update the tokens and quiz percentages based on the user's responses in the trading_phase function
    tokens, quiz_percentage_1, quiz_percentage_2, quiz_percentage_3 = trading_phase(tokens, correct_answers_2)

    # Check if the user has scored 60% or more in the second round to move to the third round or return a message and stop the game
    if quiz_percentage_2 >= 60:
        print("Congratulations! You passed the second round with {}%. The third round will now begin...".format(quiz_percentage_2))
    else:
        print("Sorry, you did not pass the second round with {}%. Run the cell again to start over.".format(quiz_percentage_2))
        return
    
    # Start the third round of the game by calling the game_set_3 function and passing the python_multiple_choice_questions list
    # Store the number of correct answer's the user achieves in the "correct_answer_3" variable
    correct_answers_3 = game_set_3(python_multiple_choice_questions)
    
    # Run the trading phase based on the token count and correct answers count from the third round
    # Update the tokens and quiz percentages based on the user's responses in the trading_phase function
    tokens, quiz_percentage_1, quiz_percentage_2, quiz_percentage_3 = trading_phase(tokens, correct_answers_3)

    # Check if the user has scored 50% or more in the third round to complete the game or return a message and stop the game
    if quiz_percentage_3 >= 50:
        print("Congratulations! You passed the third round with {}%.".format(quiz_percentage_3))
        print("Game Complete! Thank you for playing our trivia game!")
    else:
        print("Sorry, you did not pass the third round with {}%. Run the cell again to start over.".format(quiz_percentage_3))
        return