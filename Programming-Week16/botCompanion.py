# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: Chill conversational AI with wellness features

"""
DudeAI 2.0 blends our original NLP chatbot with wellness features in a relaxed style:
1. Keeps all original family/pet/teacher recognition
2. Adds stress-relief tools (breathing, journaling)
3. Tracks mood trends without being pushy
4. Offers creative escapes (storytelling)
5. Maintains that easy-going "dude" personality
"""

import re
import random
import time
from textblob import TextBlob

class DudeAI:
    def __init__(self):
        # Core Configuration
        self.name = "DudeAI"
        self.user_name = None
        self.mood_history = []
        
        # Original Knowledge Base
        self.known_entities = {
            "family": {"dad", "father", "mom", "mother", "brother", 
                     "sister", "grandma", "grandpa", "uncle", "aunt"},
            "pets": {"dog", "cat", "puppy", "kitten", "fish", 
                    "hamster", "bird", "turtle", "rabbit"},
            "negations": {"no", "not", "never", "none", "nobody"}
        }
        
        self.teacher_info = {
            "name": "Mr. Finkelstein",
            "pronoun": "He",
            "subject": "robotics"
        }
        
        # Enhanced Response Banks (Dude-style)
        self.family_responses = [
            "Family's important, dude. Tell me more about your {family_member}.",
            "Right on. What's your {family_member} like?",
            "No way! My {family_member} does that too sometimes."
        ]
        
        self.pet_responses = [
            "Dogs rule! What's your {pet}'s name?",
            "I'm totally a {pet} person too. What's yours like?",
            "Pets are the best. Tell me more about your {pet}, dude."
        ]
        
        # Wellness Features
        self.chill_activities = {
            "breathe": self.guide_chill_breathing,
            "journal": self.suggest_journal_prompt,
            "story": self.start_chill_story,
            "gratitude": self.ask_gratitude_question
        }
        
        self.chill_responses = [
            "Whoa, heavy stuff. Wanna try something relaxing?",
            "Sounds like you could use a breather, my dude.",
            "I feel you. Maybe take a quick brain break?"
        ]
        
    # Original Core Methods (Dude-ified)
    def analyze_sentiment(self, text):
        """Checks the vibe of the convo, dude"""
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0.2:
            return "positive"
        elif analysis.sentiment.polarity < -0.2:
            return "negative"
        else:
            return "neutral"

    def extract_name(self, text):
        """Catches your name if you drop it"""
        patterns = [
            r"my name is (\w+)",
            r"i['’]m (\w+)",
            r"i am (\w+)",
            r"call me (\w+)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                self.user_name = match.group(1).capitalize()
                return f"Righteous name, {self.user_name}! What's up?"
        return None

    # New Wellness Methods (Chill Edition)
    def guide_chill_breathing(self):
        """4-4-4 breathing, no pressure"""
        print("\nLet's take a breather together:")
        print("Breathe in... (4 seconds)")
        time.sleep(4)
        print("Hold it... (4 seconds)")
        time.sleep(4)
        print("Let it out... (4 seconds)")
        time.sleep(4)
        return "How's that feel? Better?"

    def suggest_journal_prompt(self):
        """Casual journal ideas"""
        prompts = [
            "What's one small win you had today?",
            "Who made you smile recently?",
            "What's something you're stoked about?"
        ]
        return f"Here's a thought: {random.choice(prompts)} No pressure though."

    def start_chill_story(self):
        """Collaborative storytelling"""
        starters = [
            "Dude imagine this... you find a glowing unicorn on a skateboard...",
            "So there's this taco that grants wishes..."
        ]
        print(f"\n{random.choice(starters)}")
        user_part = input("What happens next? ")
        return f"Rad addition! So then {user_part}"

    def ask_gratitude_question(self):
        """Keeps it light and positive"""
        return "What's one thing that didn't suck today?"

    # Enhanced Response Generator
    def generate_response(self, user_input):
        """Handles convo flow with wellness checks"""
        cleaned_input = user_input.strip().lower()
        words = set(re.findall(r'\b\w+\b', cleaned_input))
        
        # Special commands
        if cleaned_input == "bye":
            return "Peace out! Come chat anytime."
            
        if cleaned_input == "help":
            return ("Try these: 'breathe' for calming exercise, " 
                   "'journal' for writing ideas, 'story' to create together")
        
        # Name learning
        if not self.user_name:
            name_response = self.extract_name(cleaned_input)
            if name_response:
                return name_response

        # Empty input
        if not cleaned_input:
            return "I'm all ears, dude..."

        # Check for wellness activities
        for trigger, method in self.chill_activities.items():
            if trigger in cleaned_input:
                return method()
        
        # Original context detection
        family_words = words & self.known_entities["family"]
        if family_words:
            family_member = family_words.pop()
            return random.choice(self.family_responses).format(family_member=family_member)

        pet_words = words & self.known_entities["pets"]
        if pet_words:
            pet = pet_words.pop()
            return random.choice(self.pet_responses).format(pet=pet)

        if self.teacher_info["name"].lower() in cleaned_input:
            return f"{self.teacher_info['pronoun']} sounds like a rad {self.teacher_info['subject']} teacher!"

        # Sentiment analysis with wellness check
        mood = self.analyze_sentiment(user_input)
        self.mood_history.append(mood)
        
        if mood == "negative" and len(self.mood_history) > 2 and all(m == "negative" for m in self.mood_history[-3:]):
            return random.choice(self.chill_responses)
            
        return self.get_base_response(mood)

    def get_base_response(self, mood):
        """Handles regular convo flow"""
        if mood == "positive":
            responses = [
                "That's awesome, dude!",
                "Stoked to hear that!",
                "Right on!"
            ]
        elif mood == "negative":
            responses = [
                "Bummer, dude. Wanna talk about it?",
                "That's rough. I'm here to listen.",
                "No judgement here. What's up?"
            ]
        else:
            responses = [
                "Interesting... tell me more.",
                "I'm following you, keep going.",
                "Yeah? What else?"
            ]
        return random.choice(responses)

def main():
    """Runs the chill conversation loop"""
    try:
        ai = DudeAI()
        print("\n*DudeAI boots up*")
        print("Hey there! I'm DudeAI. Let's chat - or type 'help' for options.")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                response = ai.generate_response(user_input)
                print(f"DudeAI: {response}")

                if user_input.lower() == "bye":
                    break

            except KeyboardInterrupt:
                print("\nDudeAI: No worries, catch you later!")
                break
                
    except ImportError:
        print("\nWhoops! Need to install textblob first:")
        print("pip install textblob")
        print("python -m textblob.download_corpora")

if __name__ == "__main__":
    main()