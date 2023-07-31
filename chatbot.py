import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|hola)', ['hello there', 'hi there', 'hey there']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*) (location|city) ?', 'I am not sure where that is.'],
    ['(.*) created you ?', ['I was created by a group of developers.']],
    ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    ['(.*) help (.*)', ['I am here to help you']],
    ['(.*)whats your name ?', ['My name is MyChatBot']],
    ['(.*) (sports|game) ?', ['I am a huge fan of football.']],
    ['(.*) (food|dish) ?', ['I love pizza!']],
    ['(.*) (movie|film) ?', ['My favorite movie is The Shawshank Redemption.']],
    ['(.*) (music|song) ?', ['I enjoy listening to all kinds of music.']],
    ['(.*) (book|novel) ?', ['My favorite book is To Kill a Mockingbird.']],
    ['(.*) (hobby|hobbies) ?', ['I love reading and playing chess.']],
    ['(.*) (job|work) ?', ['I am a chatbot, so my job is to talk to people like you!']],
    ['(.*) (age|old) ?', ["I'm just a computer program, so I don't have an age."]],
    ['(.*) (language|languages) ?', ["I can communicate in many languages, but my primary language is English."]],
    ['(.*) (family|siblings) ?', ["As a computer program, I don't have a family or siblings."]],
    ['(.*) (friend|friends) ?', ["As a chatbot, I'm here to talk to anyone who wants to chat with me!"]],
    ['(.*) (love|relationship) ?', ["As a computer program, I don't have personal relationships."]],
    ['(.*) (travel|vacation) ?', ["As a computer program, I don't travel or go on vacation."]],
    ['(.*) (animal|pet) ?', ["As a computer program, I don't have pets."]],
    ['(.*) (school|college) ?', ["As a computer program, I didn't attend school or college."]],
    ['(.*) (car|vehicle) ?', ["As a computer program, I don't drive or own a car."]],
    ['(.*) (phone|mobile) ?', ["As a computer program, I don't have a phone or mobile device."]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
