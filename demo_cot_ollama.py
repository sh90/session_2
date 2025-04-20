import ollama

def chain_of_thought_reasoning(question,model):
    """Implement basic chain-of-thought prompting with an LLM."""

    # Construct prompt that encourages step-by-step reasoning
    prompt_text = f"""
    Question: {question}

    Let's think about this step by step to find the correct answer.
    """
    response = ollama.generate(model=model,prompt=prompt_text)

    return response.response

# Example usage
math_problem = "If John has 5 apples and gives 2 to Mary, then buys 3 more and gives half of his apples to Tom, how many apples does John have left?"
logical_problem = "If all A are B, and some B are C, can we conclude that some A are C? Why or why not?"

model = "gemma3:1b"  # Example AI models from Ollama llama2

print("Math Problem:\n", chain_of_thought_reasoning(math_problem,model))
print("\nLogical Problem:\n", chain_of_thought_reasoning(logical_problem,model))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
