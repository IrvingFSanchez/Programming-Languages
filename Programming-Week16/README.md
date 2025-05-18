# DudeAI - The Chill Conversational Companion 🤙

![DudeAI Banner](https://example.com/dudeai-banner.jpg) *[placeholder image: cartoon surfboard with chatbot icon]*

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Wellness Tools](#wellness-tools)
- [Development](#development)
- [License](#license)

## Overview

DudeAI is your easy-going digital pal that blends natural conversation with wellness support. Originally developed as an NLP class project at Lewis University, this chatbot now helps users:

- Have natural conversations about family, pets, and school
- Manage stress with built-in wellness tools
- Track emotional trends over time
- Get creative with collaborative storytelling

"Whoa, that sounds heavy. Wanna chat about it?" - DudeAI probably

## Features

### 🗣️ Core NLP Skills

| Feature | Example |
|---------|---------|
| Family recognition | "My sister just graduated" → "Right on! What's your sister studying?" |
| Pet conversations | "I have a hamster" → "Hamsters rule! What's yours named?" |
| Teacher detection | "Mr. Finkelstein helped me" → "He sounds like a rad robotics teacher!" |

### 🧠 Wellness Support

| Tool | What It Does |
|------|-------------|
| 4-4-4 Breathing | Guides calming breathing exercises |
| Journal Prompts | Suggests reflective writing starters |
| Story Builder | Co-creates fun micro-stories |
| Mood Tracking | Notices emotional patterns (3+ negative → suggests help) |

### 🏄 Dude Personality

```python
# Sample DudeAI response logic
if stress_detected:
    return random.choice([
        "Sounds gnarly. Wanna take a breather?",
        "Heavy vibes. Maybe try the journal thing?",
        "I feel you. Let's shake it off with a story?"
    ])
```

## Installation

1. **Prerequisites**
   - Python 3.8+
   - pip package manager

2. **Setup**

   ```bash
   # Clone the repo
   git clone https://github.com/yourusername/dudeai.git
   cd dudeai

   # Install dependencies
   pip install textblob
   python -m textblob.download_corpora
   ```

3. **Run It**

   ```bash
   python dudeai.py
   ```

## Usage

### Basic Commands

```markdown
help   - Show wellness options
breathe - Start breathing exercise
journal - Get a writing prompt
story   - Build a story together
bye    - End conversation
```

### Sample Session

```plaintext
You: I'm so stressed about finals
DudeAI: Heavy vibes. Wanna try 4-4-4 breathing? (type 'breathe')

You: breathe
DudeAI: Let's chill for a sec...
Breathe in... (4 seconds)
[countdown continues]

You: My cat just knocked over my coffee
DudeAI: Cats rule! What's your troublemaker's name?
```

## Wellness Tools

### 🌬️ Breathing Exercise

Guides through:

1. 4-second inhale
2. 4-second hold
3. 4-second exhale

### 📓 Journal Prompts

- "What's one small win today?"
- "Who made you smile this week?"
- "What are you oddly proud of?"

### 📖 Story Builder

Try inputs like:

- "Let's do a space story"
- "Make it about a surfing robot"

## Development

### File Structure

```markdown
dudeai/
├── dudeai.py       # Main chatbot class
├── responses/      # YAML response templates
├── tests/          # Unit tests
└── README.md       # This file
```

### Adding New Features

1. Extend `known_entities` for new topics
2. Add methods to `chill_activities`
3. Update response banks in YAML files

```python
# Example: Adding music recognition
self.known_entities["music"] = {"band", "song", "guitar"}
```

## License

[MIT License](LICENSE.md)

---

> "Be excellent to each other... and party on!" - DudeAI's life philosophy
