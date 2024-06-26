import sys
import openai

# Set your OpenAI API key
API_KEY = "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"
openai.api_key = API_KEY

# Variable to store conversation history
conversation = []

def get_gpt3_response(context, user_task, user_query):
    """
    Function to interact with the GPT-3 model and get a response.
    
    Args:
        context (str): Context of the conversation.
        user_task (str): Task assigned to the user.
        user_query (str): User's query or input.
    
    Returns:
        str: Response generated by the GPT-3 model.
    """
    try:
        # Create request for OpenAI API
        request = {
            "model": "gpt-3.5-turbo-0125",
            "messages": [
                {"role": "system", "content": context},
                {"role": "user", "content": user_task},
                {"role": "user", "content": user_query}
            ],
            "temperature": 1,
            "max_tokens": 4096,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        # Get response from OpenAI API
        response = openai.ChatCompletion.create(**request)

        # Add user query and response to conversation
        conversation.append(user_query)
        conversation.append(response.choices[0].message.content)

        # Return response content
        return response.choices[0].message.content
    except openai.error.APIError as e:
        print("Error getting response from GPT-3:", e)
        return None

def save_conversation(filename):
    """
    Function to save conversation history to a file.
    
    Args:
        filename (str): Name of the file to save the conversation.
    """
    try:
        with open(filename, "w") as file:
            for i in range(0, len(conversation), 2):
                file.write(f"User: {conversation[i]}\n")
                file.write(f"GPT-3: {conversation[i+1]}\n")
        print("Conversation saved successfully.")
    except Exception as e:
        print("Error saving conversation:", e)

def main():
    """
    Main function to run the conversational interface.
    """
    # Check if conversation mode is activated
    if "--conversation" in sys.argv:
        print("Conversation mode activated.")

        while True:
            try:
                # Accept user input
                context = input("Conversation context: ")
                user_task = input("User task: ")
                user_query = input("User query ('q' to exit, 's' to save conversation): ")

                # Exit loop if user enters 'q'
                if user_query.lower() == 'q':
                    print("Exiting program...")
                    break
                elif user_query.lower() == 's':
                    filename = input("Enter filename to save conversation: ")
                    save_conversation(filename)
                    continue

                # Retrieve previous user query if the user presses the up arrow key
                if user_query == "\033[A" and len(conversation) > 0:
                    user_query = conversation[-2]
                    print("Previous user query retrieved:", user_query)
                    continue

                # Verify if the user query has text
                if user_query:
                    print("User query:", user_query)

                    # Get response from GPT-3
                    gpt3_response = get_gpt3_response(context, user_task, user_query)

                    if gpt3_response:
                        # Print GPT-3 response
                        print("GPT-3 response:", gpt3_response)
                    else:
                        print("Unable to get a response.")
                else:
                    print("User query is empty. Please try again.")
            except KeyboardInterrupt:
                print("\nExiting program...")
                break
            except Exception as e:
                print("Error executing the program:", e)
    else:
        print("Conversation mode not activated. Use '--conversation' as a command-line argument.")

if __name__ == "__main__":
    main()
