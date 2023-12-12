from random import choice

def generate_sentence():
    """Generate a random sentence from a select set."""
    nouns = [
        "Mark",
        "Adam",
        "Angela",
        "Larry",
        "Jose",
        "Matt",
        "Jim"
    ]
    verbs = [
        "runs",
        "skips",
        "sings",
        "leaps",
        "jumps",
        "climbs",
        "fires a Civil War cannon",
        "swims",
        "argues",
        "giggles"
    ]
    phrases = [
        "in a tree",
        "through every room in the house",
        "very loudly",
        "around the bush",
        "while reading the newspaper",
        "very badly",
        "while skipping",
        "instead of grading",
        "while programming Python"
    ]
    return f"{choice(nouns)} {choice(verbs)} {choice(phrases)}."

def sentence():
    return generate_sentence()
