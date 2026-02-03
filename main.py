from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke(
    {
        "reviews": [],
        "question": "what is the best pizza place in town?"
    }
)

print(result)
# result:
# Based on my expertise, I'd be happy to help!
# Unfortunately, I don't have any specific reviews from customers at this time. However, I can suggest that you check out some of the top-rated pizzerias in your area by looking up online review platforms such as Yelp or Google Reviews.
# That being said, I can give you a general answer about what makes a great pizza place. A good pizza restaurant should have a variety of toppings, crispy crust, and a flavorful sauce. They should also have a welcoming atmosphere and attentive service to make your dining experience enjoyable.
# If you're looking for recommendations, I can suggest asking friends or colleagues who have tried pizzerias in the area for their opinions. Alternatively, you could try checking out online review sites to see which pizza place has received the highest ratings from customers.
