
# Title: **Determining EVCS Infrastructure in a country Using OpenAI and LangChain**

## Overview

This project is designed to determine the electric vehicle charging station (EVCS) infrastructure in Canada using the OpenAI API via the LangChain library. The project consists of multiple steps to identify the province with the most EV public chargers, the number of public EV charging stations in the city within the province with the most EV public chargers, and the detailed breakdown of chargers in that city.

## Setup

1. **Clone the Repository**: Clone the repository to your local machine.

2. **Environment Setup**: Ensure you have Python installed. Create a virtual environment and activate it.

3. **Install Dependencies**: Install the required Python packages.

4. **API Key Configuration**: Create a `.env` file in the root directory of your project and add your OpenAI API key.


## Usage

To run the script and obtain the EV infrastructure details for Canada, execute the following command:
```bash
python script.py
```

## Script Explanation

The script follows a sequence of steps to derive the required information:

1. **Load API Key**: 
The load_api_key function ensures the API key is loaded from the environment.

2. **LLM Chain Creation**:
The create_llm_chain function initializes the LLM chain with the specified model.

3. **Prompt Template Creation**:
The create_prompt_template function creates prompt templates with input variables and a template string

4. **Chain Creation**:
The create_chain function creates an LLM chain using the provided LLM and prompt template.

5. **Combining Chains**:
The combine_chains function combines multiple chains into a single sequential chain.

6. **Main Function**:

- The main(country) function orchestrates the chain creation and execution process.

i. First Step: Identifies the province in the specified country with the most EV public chargers.

ii. Second Step: Finds the city within that province with the most EV public chargers.

iii. Third Step: Determines the number of public EV charging stations in the identified city, detailing counts for Level-2, fast DC, and ultra-fast chargers formatted as a JSON object.

- This approach improves readability, maintainability, and reusability.


## References

* LangChain Documentation, [LangChain Docs](https://api.python.langchain.com/en/latest/langchain_api_reference.html)
* OpenAI API Documentation, [OpenAI Docs](https://platform.openai.com/docs/overview)
* How to Build LLM Applications with LangChain Tutorial, [How to Build LLM Applications with LangChain Tutorial](https://www.datacamp.com/tutorial/how-to-build-llm-applications-with-langchain)


## License

This project is licensed under the MIT License. See the LICENSE file for details.




