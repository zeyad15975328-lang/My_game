import random
import streamlit as streamlit_app  # Imported as streamlit_app to keep it clear

# Define ASCII art shapes for Rock, Paper, and Scissors
# Extracted and reconstructed from 1000054396.jpg and 1000054397.jpg
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

shape = [rock_art, paper_art, scissors_art]

# Streamlit UI Configuration
streamlit_app.set_page_config(page_title="Rock, Paper, Scissors", layout="centered")
streamlit_app.title("🪨 📄 ✂️ Rock, Paper, Scissors Game")

# Game Rules Expander
with streamlit_app.expander("📚 Show Game Rules"):
    streamlit_app.markdown(
        """
    ********** RULES **********
    1. You choose and computer choose.
    2. Rock smash scissors -> Rock win.
    3. Scissor cut paper -> Scissors win.
    4. Paper cover Rock -> Paper win.
    """
    )

# Game Play Section
streamlit_app.subheader("Make Your Move")

# User Input
choice = streamlit_app.selectbox(
    "Choose Rock, Paper, or Scissors:", 
    ["Select...", "Rock", "Paper", "Scissors"], 
    index=0
)

if choice != "Select...":
    # Display Player Choice
    streamlit_app.write("### You chose:")
    if choice == "Rock":
        streamlit_app.text(shape[0])
    elif choice == "Scissors":
        streamlit_app.text(shape[2])
    elif choice == "Paper":
        streamlit_app.text(shape[1])

    # Computer Choice Logic
    words_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(words_list).capitalize()

    # Display Computer Choice
    streamlit_app.write("### Computer chose:")
    if computer_choice == "Rock":
        streamlit_app.text(shape[0])
    elif computer_choice == "Paper":
        streamlit_app.text(shape[1])
    elif computer_choice == "Scissors":
        streamlit_app.text(shape[2])

    # Determine the Winner
    streamlit_app.write("---")
    if computer_choice == choice:
        streamlit_app.info("🤝 It's a tie!")
    elif (
        (choice == "Scissors" and computer_choice == "Paper") or
        (choice == "Rock" and computer_choice == "Scissors") or
        (choice == "Paper" and computer_choice == "Rock")
    ):
        streamlit_app.success(f"🎉 Winner! {choice} beats {computer_choice}")
    else:
        streamlit_app.error(f"😢 Loser! {computer_choice} beats {choice}")
