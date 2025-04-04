import random
from core.text_to_speech import speak

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and now it won’t stop sending me vacation ads.",
    "Why do cows have hooves instead of feet? Because they lactose!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I asked my AI assistant for a joke. It said: 'I am the joke!'"
]

fun_facts = [
    "Did you know honey never spoils? Archaeologists found 3000-year-old honey in Egyptian tombs, and it was still good!",
    "Bananas are berries, but strawberries aren’t!",
    "The Eiffel Tower can grow more than 6 inches during summer due to heat expansion.",
    "Octopuses have three hearts. Imagine getting triple heartbreaks!"
]

def tell_joke():
    """Tells a random joke and speaks it properly."""
    joke = random.choice(jokes)
    speak(joke)

def tell_fun_fact():
    """Tells a random fun fact and speaks it properly."""
    fact = random.choice(fun_facts)
    speak(fact)
