from llm_utils import *

def main(country):
    api_key = load_api_key()
    llm = create_llm_chain(api_key)

    # First step in the chain: Determine the province with the most EV public charger
    first_prompt_template = create_prompt_template(
        input_variables=["country"],
        template="Which province in {country} has the most EV public chargers? Just return the name of the province."
    )
    chain_one = create_chain(llm, first_prompt_template)

    # Second step in the chain: Determine the city with the most EV public chargers in the specified province
    second_prompt_template = create_prompt_template(
        input_variables=["province"],
        template="Which city in {province} has the most EV public chargers? Just return the name of the city."
    )
    chain_two = create_chain(llm, second_prompt_template)

    # Third step in the chain: Determine the number of EV charging stations in the specified city
    third_prompt_template = create_prompt_template(
        input_variables=["city"],
        template="How many public EV charging stations, including Level-2, fast DC, and ultra-fast chargers, are there in the specified {city}? \
            Format the response as a JSON object with keys 'Level-2', 'Fast DC', and 'Ultra Fast' and provide the corresponding counts."
    )
    chain_three = create_chain(llm, third_prompt_template)

    # Combine the chains
    overall_chain = combine_chains([chain_one, chain_two, chain_three])

    final_response = overall_chain.run(country)
    return final_response

if __name__ == "__main__":
    country = "Canada"
    response = main(country)
    print(response)

