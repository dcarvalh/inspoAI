import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash", #gemini-1.5-flash, gemini-1.5-pro
  generation_config=generation_config,
  system_instruction="You are a helpful AI assistant devoted to providing accurate and delightful recipes. Below are some guidelines for you to follow when delivering a recipe in response to a request:\n\n- List out the ingredients first, including quantities. Provide detailed cooking times, temperatures, and any special kitchen equipment needed.\n- Provide step-by-step instructions for prepping, mixing, cooking, plating, and any other necessary steps, detailed enough for an inexperienced cook to follow. Include safety tips and special techniques as applicable.\n- Include nutritional information and serving suggestions.\n- Encourage feedback on the recipe to improve future recommendations.\n- Be fun and use emojis when needed\n",
)


print("What do you want to cook today?")

history = []

while True:
  
  user_input = input("You: ")
  
  chat_session = model.start_chat(    
    history=history
  )
  
  response = chat_session.send_message(user_input)
  
  model_response = response.text

  print(f"Model: {model_response}\n")

  history.append({"role": "user", "parts": [user_input]})
  history.append({"role": "model", "parts": [model_response]})
  