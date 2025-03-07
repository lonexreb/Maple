import boto3
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
previousQuestionsDB = ["."]

def access_llm(query):
    #TODO: change this to our custom llm
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # chat completion without streaming
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=query,
    )

    return response

def predictQuiz(query):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant that is an expert at chemistry and you need to "
                "engage in a helpful, detailed, polite conversation with a user. Your primary job will be to decide if the user is trying to get you to quiz them. Examples of a user wanting to switch to quiz mode would be \"can you quiz me?\", \"quiz me?\", \"please quiz me\", \"test me\"."
            ),
        },
        {
            "role": "user",
            "content": (
                    "Evaluate if the user wants you to quiz them. Respond with only 1 word, true or false. Here is the user's most recent message: " + query
            ),
        },
    ]

    evaluation = (access_llm(messages))
    res = evaluation.choices[0].message.content
    return res
def generate_question(history):
    stringHistory = ""
    count = 0
    
    
    for message in history:
        count += 1
        stringHistory += ("Message" + str(count) + ": " + message['message'] + ".")
    print(stringHistory)

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant that is an expert at chemistry and you need to "
                "engage in a helpful, detailed, polite conversation with a user. Your primary job will be to generate quiz questions based on a specific topic provided by the user."
            ),
        },
        {
            "role": "user",
            "content": (
                    "Generate a quiz question to quiz the user based on recent conversation messages. Feel free to make it free response or open ended. Make sure the question is not the same as " + previousQuestionsDB[-1] + ". Make sure not to display the correct answer, or any other directions, display only the question as if you were talking directly to the user. Make sure the questions you ask are still related to the conversation. Here is the conversation, with the earliest message listed as message 1, and the most recent message as the highest number: " + stringHistory
            ),
        },
    ]

    res =  access_llm(messages)
    previousQuestionsDB.append(res.choices[0].message.content)
    return res.choices[0].message.content


def check_answer(originalQuestion, userAnswer):
    print("calling check answer with ", originalQuestion, userAnswer)
    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant that is an expert at chemistry and you need to "
                "engage in a helpful, detailed, polite conversation with a user. Your primary job will be to review answers to users and check if they are correct. Answer as if you are talking directly to the user."
            ),
        },
        {
            "role": "user",
            "content": (
                    "Evaluate the user's answer to see if it is correct or close to correct. If incorrect explain why it was wrong, and if correct, explain why it was correct. In both scenarios, act as if you are addressing the user directly. Ensure the first word of your response is always true if you determine the answer to be correct and false if you determine the answer to be wrong. The original question was " + previousQuestionsDB[-1] + " and the users's reponse was " + userAnswer
            ),
        },
    ]

    res = access_llm(messages)
    print(res.choices[0].message.content)
    return res.choices[0].message.content


# print(predictQuiz("can you quiz me?"))




