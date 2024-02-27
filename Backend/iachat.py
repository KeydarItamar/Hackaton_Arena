
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:15:17 2024

@author: Itamar
"""

from langchain_community.chat_models import ChatCohere
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
import getpass
import os

COHERE_API_KEY = '0Luj5pPG0qr5smcMdNravruypYYGwjs45LvQmJCo'
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

chat = ChatCohere(model="command", max_tokens=256, temperature=0.75)

animal_data={"name": 'pickles', "age": 3,"specie": 'cat', "size": 'big'}

query  = "What is a good diet for my pet?"
query2 = "What foods are poisonous for my pet?"
query3 = "What do you suggest a training for my pet?"
query4 = "Can you write a song lyric about my pet?"

def ia_question(animal_data, num):
    query1  = "What is a good diet for my pet?"
    query2 = "What foods are poisonous for my pet?"
    query3 = "What do you suggest a training for my pet?"
    query4 = "Can you write a song lyric about my pet?"
    query=''
    if num == 1 : query = query1
    if num == 2 : query = query2
    if num == 3 : query = query3
    if num == 4 : query = query4
    
    prompt = ChatPromptTemplate.from_template("I have this animal with me, {animal_data} and i like to know: {query} ")
    chain = prompt | chat
    return chain.invoke({"animal_data": animal_data, "query": query}).content


ia_question(animal_data, 3)







