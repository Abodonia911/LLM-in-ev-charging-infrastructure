import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from langchain_core.prompts import PromptTemplate

def load_api_key():
    _ = load_dotenv(find_dotenv())  # read local .env file
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key

# Create OpenAI LLM chain with the model name
def create_llm_chain(api_key, model_name="gpt-3.5-turbo"):
    return OpenAI(model_name=model_name, openai_api_key=api_key)

def create_prompt_template(input_variables, template):
    return PromptTemplate(input_variables=input_variables, template=template)

def create_chain(llm, prompt_template):
    return LLMChain(llm=llm, prompt=prompt_template)

def combine_chains(chains, verbose=True):
    return SimpleSequentialChain(chains=chains, verbose=verbose)