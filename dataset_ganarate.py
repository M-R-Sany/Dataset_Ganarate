import pandas as pd
import random

# Define target number of rows (50 Lakhs)
NUM_ROWS = 5000000

# Base templates to mimic your dataset's style
templates = [
    {"base": "That was painfully dumb.", "main": "Mocking", "sub": "ridicule", "sev": "Low", "sent": "Negative"},
    {"base": "You are trying too hard for attention.", "main": "Sexual Bullying", "sub": "inappropriate comments", "sev": "Medium", "sent": "Positive"},
    {"base": "You really embarrassed yourself.", "main": "Mocking", "sub": "sarcasm", "sev": "Low", "sent": "Positive"},
    {"base": "You are so annoying.", "main": "Harassment", "sub": "humiliation", "sev": "Low", "sent": "Negative"},
    {"base": "You should change your body.", "main": "Body Shaming", "sub": "appearance attacks", "sev": "Low", "sent": "Negative"},
    {"base": "You look awful today.", "main": "Body Shaming", "sub": "appearance attacks", "sev": "Low", "sent": "Negative"},
    {"base": "People only care about your looks.", "main": "Sexual Bullying", "sub": "inappropriate comments", "sev": "Low", "sent": "Neutral"},
    {"base": "Everybody is laughing at you.", "main": "Mocking", "sub": "ridicule", "sev": "Low", "sent": "Neutral"},
    {"base": "Nobody likes how you look.", "main": "Body Shaming", "sub": "appearance attacks", "sev": "Low", "sent": "Neutral"},
    {"base": "You behave like a fake troll online.", "main": "Sexual Bullying", "sub": "normal conversation", "sev": "Low", "sent": "Negative"},
    {"base": "People think you sound very annoying online.", "main": "Threat", "sub": "appearance attacks", "sev": "Low", "sent": "Negative"},
    {"base": "You are the most cringe person I have ever seen.", "main": "Mocking", "sub": "normal conversation", "sev": "Low", "sent": "Positive"}
]

# Random filler words to ensure uniqueness and match your data's footprint
filler_words = ["clear", "age", "enjoy", "for", "check", "kind", "ever", "father", "edge", "business", 
                "hard", "reach", "push", "audience", "great", "commercial", "career", "instead", "lawyer", 
                "nearly", "back", "safe", "cultural", "certain", "this", "according", "bit", "issue", 
                "night", "establish", "care", "book", "world", "writer", "ten", "candidate", "production", 
                "mother", "song", "add", "once", "peace", "its", "her", "response", "base", "message", 
                "leave", "interest", "himself", "brother", "prove", "another", "do", "next", "claim", 
                "their", "those", "public", "range", "four", "wife", "write", "act", "last", "race", 
                "magazine", "little", "same", "why", "size", "program", "wrong", "carry", "life", 
                "actually", "save", "floor", "blue", "officer"]

emojis = ["!", "!!", "🙂", "😡", "😂", "."]

generated_texts = set()
data = []

print("Generating data... Please wait.")

# Loop until we have 500,000 unique rows
while len(data) < NUM_ROWS:
    # 1. Pick a random base template
    template = random.choice(templates)
    
    # 2. Generate a unique randomized suffix
    num_fillers = random.randint(5, 12)
    chosen_fillers = random.sample(filler_words, min(num_fillers, len(filler_words)))
    filler_str = " ".join(chosen_fillers)
    chosen_emoji = random.choice(emojis)
    
    # 3. Create unique text ID/Reference to guarantee absolute uniqueness
    ref_id = f"Ref-{random.randint(100000, 999999)}"
    
    # Format text: Base string + Unique Ref + Filler + Emoji
    full_text = f"{template['base']} {ref_id}, {filler_str}. {chosen_emoji}"
    
    # Double check uniqueness
    if full_text not in generated_texts:
        generated_texts.add(full_text)
        
        # Calculate text metrics
        text_length = len(full_text)
        word_count = len(full_text.split())
        contains_slang = random.choice([True, False])
        
        # Append structured data row
        data.append({
            "text": full_text,
            "main_class": template["main"],
            "subcategory": template["sub"],
            "severity": template["sev"],
            "sentiment": template["sent"],
            "text_length": text_length,
            "word_count": word_count,
            "contains_slang": contains_slang
        })

# Convert to DataFrame
df_expanded = pd.DataFrame(data)

# Export to CSV
output_filename = "expanded_cyberbullying_dataset_5lakh.csv"
df_expanded.to_csv(output_filename, index=False)

print(f"Success! Generated {len(df_expanded)} completely unique rows.")
print(f"File saved as: {output_filename}")