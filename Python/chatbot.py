import numpy as np
import linearReg as lr
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

prompt = """
Reply to questions related to the topic of batterys, if the question asked or statment made is not related to batterys reply by saying
Please ask questions related to batterys, be very strict of this rule as if that is your only field of knowledge

Text: {answer to question}
"""

def classify_soh(soh_value: float, threshold: float = 0.6) -> str:
    if soh_value >= threshold:
        return "The battery is healthy"
    else:
        return "The battery is not healthy"
    

def aiChatBot(question: str) -> str:
    """
    Uses Gemini API to answer general battery-related questions.
    """
    try:
        prompt = (
            "You are a helpful chatbot in a university project about battery health. "
            "Answer clearly and simply. The user's question is:\n\n"
            f"{question}"
        )

        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Sorry, I couldn't contact the Gemini API. Error: {e}"


def main():
    print("=== Battery SOH Chatbot ===")
    print("Your linear regression model has been trained in linearReg.py.\n")
    print("You can type:")
    print(" - [type: 1] to check battery soh predicts SOH for a random sample")
    print(" - [type: 2] to set threshold change the SOH threshold (default 0.6)")
    print(" - any general battery related question")
    print(" - 'quit or exit' to close")

    threshold = 0.6  # default threshold

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["quit", "exit", "clear"]:
            print("Chatbot: Goodbye!")
            break

        elif user_input == "1":
            X_test = lr.X_test
            idx = np.random.randint(0, X_test.shape[0])
            sample = X_test[idx:idx+1]
            pred_soh = lr.regModel.predict(sample)[0]

            status = classify_soh(pred_soh, threshold)

            print(f"Chatbot: Predicted SOH = {pred_soh:.3f}")
            print(f"Chatbot: {status}")

        elif user_input == "2":
            try:
                new_th = float(input("Enter new threshold (#.#): "))
                threshold = new_th
                print(f"Chatbot: Threshold updated to {threshold:.2f}.")
            except ValueError:
                print("Chatbot: That wasn't a valid number. Threshold unchanged.")

        else:
            #other questions answered by Gemini
            answer = aiChatBot(user_input)
            print("Chatbot:", answer)


if __name__ == "__main__":
    main()
