# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import openai

# Set your API key
import data_info

openai.api_key = data_info.open_ai_key


def chain_of_thought_reasoning(question):
    """Implement basic chain-of-thought prompting with an LLM."""

    # Construct prompt that encourages step-by-step reasoning
    prompt = f"""
    Question: {question}

    Let's think about this step by step to find the correct answer.
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response.choices[0].message.content

# Example usage
math_problem = "If John has 5 apples and gives 2 to Mary, then buys 3 more and gives half of his apples to Tom, how many apples does John have left?"
logical_problem = "If all A are B, and some B are C, can we conclude that some A are C? Why or why not?"

print("Math Problem:\n", chain_of_thought_reasoning(math_problem))
print("\nLogical Problem:\n", chain_of_thought_reasoning(logical_problem))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
