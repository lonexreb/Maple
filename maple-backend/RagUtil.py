# import boto3
# import os
# from dotenv import load_dotenv

# load_dotenv()
# bedrock_agent_runtime = boto3.client(
#     'bedrock-agent-runtime',
#     region_name='us-east-1',
#     aws_access_key_id = os.getenv("AWS_ACCESS_KEY"),
#     aws_secret_access_key= os.getenv("AWS_SECRET_KEY")
# )


# def retrieve(queryInput, kbId, numberOfResults):
#     return bedrock_agent_runtime.retrieve(
#         knowledgeBaseId = kbId,
#         retrievalQuery = {
#             'text': queryInput
#         },
#         retrievalConfiguration = {
#             'vectorSearchConfiguration': {
#                 'numberOfResults': numberOfResults
#             }
#         },
#     )

# def retrieveAndGenerate(query, kbId):
#     print("calling ret and gen with query: ", query)
#     return bedrock_agent_runtime.retrieve_and_generate(
#         input={
#             'text': query
#         },
#         retrieveAndGenerateConfiguration={
#             'type': 'KNOWLEDGE_BASE',
#             'knowledgeBaseConfiguration': {
#                 'knowledgeBaseId': kbId,
#                 'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-instant-v1'
#                 }
#             }
#         )



# def get_context(query, kbId, numberOfResults):
#     #TODO: toggle this on when sending to our custom model
#     #response = retrieve(query, kbId, numberOfResults)
#     #return response['retrievalResults']


#     response = retrieveAndGenerate(query, kbId)["output"]["text"]
#     return response


# print(get_context("how much is a flux 300", "AYP1IY3IUL", 10))

import openai
import os

from openai import OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_context(question):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": "You are an advanced mathematics tutor. Answer questions in a clear and concise way, providing step-by-step solutions and explanations."},
        {"role": "user", "content": question}
        ],
        max_tokens=200,# Adjust based on the depth of answers needed
        temperature=0.3,# Lower for consistent, factual answers
    )
    return response.choices[0].message.content

# # Example usage
# question = "Can you explain the concept of eigenvalues and eigenvectors in linear algebra?"
# print(ask_math_question(question))
