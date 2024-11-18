# Import necessary libraries
import gradio as gr
import keras_nlp

# Custom CSS for styling
css = """
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
}
.gradio-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 20px;
    flex-direction: column;
}
.tab-content {
    background-color: #f9f9f9;
    padding: 20px;
    width: 80%; /* Adjusted to make the chat area wider */
}
"""

# Load the Keras NLP model from Hugging Face or Kaggle
model_repo = "Justsp3cial/maize_model" # Address of fine-tuned model  Hugging Face
gemma_lm = keras_nlp.models.CausalLM.from_preset(f"hf://{model_repo}")

# Define the function to generate responses
def generate_response(input_text):
    template = "Instruction:\n{instruction}\n\nResponse:\n{response}"
    prompt = template.format(instruction=input_text, response="")
    out = gemma_lm.generate(prompt, max_length=128)
    ind = out.index('Response') + len('Response') + 2
    return out[ind:]

# Chat function with input validation and formatted output
def chat(user_message, history):
    if not user_message.strip():
        return history, "Please enter a message."
    
    # Generate response
    response = generate_response(user_message)
    
    # Append user and bot messages in the required format
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": response})
    
    return history, ""

# Set up the Gradio interface with header and tabs in a single row
with gr.Blocks(css=css) as app:
    with gr.Tabs() as tabs:
        with gr.Tab("Chat with CropXpert"):
            chatbot = gr.Chatbot(label="CropXpert", type="messages", height=400)
            user_input = gr.Textbox(
                placeholder="Message CropXpert",
                lines=2,
                show_label=False
            )
            send_button = gr.Button("Send")

            # Update send button and input box to handle chat
            send_button.click(
                lambda msg, hist: chat(msg, hist) if msg.strip() else (hist, "Please enter a message."),
                [user_input, chatbot],
                [chatbot, user_input]
            )

            user_input.submit(
                lambda msg, hist: chat(msg, hist) if msg.strip() else (hist, "Please enter a message."),
                [user_input, chatbot],
                [chatbot, user_input]
            )

        with gr.Tab("About CropXpert"):
            gr.Markdown("CropXpert is your expert guide on maize 🌽 production, providing crop management insights and farming tips. For now, the model is trained with only maize data, hoping to add more data across different crops in future. ")

        with gr.Tab("Reach Out"):
            gr.Markdown("For inquiries, please contact us at: ymkayode@gmail.com")

# Launch the app
app.launch()