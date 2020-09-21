#the purpose of this is to write a chatbot for therapy, from a particular fictional character's perspective
import random
import time

class cowboybot:
    def __init__(self, mindfulness_qs, math_questions, therapist_qs):
        self._mindfulness_qs = mindfulness_qs
        self._math_qs = math_questions
        self._therapist_qs = therapist_qs

    @property
    def mindfulness_qs(self):
        return self._mindfulness_qs

    @mindfulness_qs.setter
    def mindfulness_qs(self, poem):
        if type(poem) is not list:
            raise ValueError("the inputted value for mindfulness qs isn't a list and it must be")
        self._mindfulness_qs = poem

    @property
    def math_questions(self):
        return self._math_qs

    @math_questions.setter
    def math_questions(self, math_questions):
        if type(math_questions) is not list:
            raise ValueError("the inputted value for math qs isn't a list and it must be")
        self._math_qs = math_qs

    @property
    def therapist_qs(self):
        return self._therapist_qs

    @therapist_qs.setter
    def therapist_qs(self, therapist_qs):
        if type(therapist_qs) is not list:
            raise ValueError("the inputted value for therapist qs isn't a list and it must be")
        self._therapist_qs = therapist_qs

    def rand_mindfulness_line(self):
        return random.choice(self.mindfulness_qs)

    def rand_math_line(self):
        return random.choice(self.math_questions)

    def rand_therapist_line(self):
        return random.choice(self.therapist_qs)

    def chat_nicer(self):
        safe_word = input("before we begin, what is your safeword?\n")
        chit_cat = input("I'll remember that. And I'll stop immediately if you say it.\n")
        chit_cat = input("about every 5 minutes, we'll have a math break, just hit enter when a math question comes up if you don't need a break at that moment \n")
        therapist_reply = ""
        mindfulness_reply = ""
        their_replies = []
        warning_words = ["fuck", "shit", "bitch",  "shut up", "cunt"]
        bad_language_reply = ""
        now = time.time()

        while therapist_reply.lower() != safe_word and mindfulness_reply.lower() != safe_word:
            oldtime = time.time()
            pseudo_rand_number = int(oldtime) % 2
            if pseudo_rand_number == 0:
                their_reply = input(self.rand_therapist_line() + "\n")
            else:
                their_reply = input(self.rand_mindfulness_line() + "\n")
            if time.time() - oldtime > 300:
                math_reply = input(self.rand_math_line())

            their_replies.append(their_reply)
            for w in warning_words:
                if w in mindfulness_reply or w in therapist_reply:
                    bad_language_reply = input(self.rand_therapist_line() + "\n")
                    their_replies.append(bad_language_reply)
        return

mindfulness_qs = 'mindfulness_qs.txt'
math_qs = 'math_qs.txt'
therapist_qs = 'therapist_qs.txt'
mindfulness_line_list = [line.rstrip('\n') for line in open(mindfulness_qs)]
math_line_list = [line.rstrip('\n') for line in open(math_qs)]
therapist_qs_line_list = [line.rstrip('\n') for line in open(therapist_qs)]

m = cowboybot(mindfulness_line_list, math_line_list, therapist_qs_line_list)
m.chat_nicer()