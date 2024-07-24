import re
import random



class CODSOFTBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_questions = (
        "What brings you here today?",
        "What specific IT challenges are you facing?",
        "Are you considering IT consultancy services?",
        "Have you worked with IT consultants before?",
        "How important is cybersecurity for your business?",
        "Are you looking to migrate to cloud services?",
        "What are your thoughts on digital transformation?",
        "Do you have concerns about IT infrastructure scalability?",
        "How do you currently handle data privacy and compliance?",
        "Are you exploring AI or machine learning solutions for your business?",
        "What are your expectations from IT consultancy?",
    )

    def __init__(self):
        self.codsoft_babble = {
            'describe_services_intent': r'.*\s*services.*',
            'answer_why_intent': r'why\sare.*',
            'about_codsoft': r'.*\s*codsoft.*',
            'pricing_intent': r'.*\s*pricing.*',
            'technology_stack_intent': r'.*\s*technology.*',
            'client_experience_intent': r'.*\s*experience.*',
            'partnerships_intent': r'.*\s*partnerships.*',
            'future_outlook_intent': r'.*\s*future.*',
            'industry_expertise_intent': r'.*\s*industry.*',
        }

    def greet(self):
        self.name = input("Hello! Welcome to CODSOFT. May I have your name?\n")
        will_help = input(f"Hi {self.name}, do you want to continue?\n")
        if will_help in self.negative_responses:
            print("Have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Thank you for visiting CODSOFT. Have a wonderful day!")
                return True

    def chat(self):
        print(f"I'm CODBot. How can CODSOFT assist you today?")
        reply = input(f"Do you have anything specific in mind?")
        if reply in self.negative_responses:
            reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_rep(reply))

    def match_rep(self, reply):
        for intent, regex_pattern in self.codsoft_babble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_services_intent':
                return self.describe_services()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why()
            elif found_match and intent == 'about_codsoft':
                return self.about_codsoft()
            elif found_match and intent == 'pricing_intent':
                return self.pricing()
            elif found_match and intent == 'technology_stack_intent':
                return self.technology_stack()
            elif found_match and intent == 'client_experience_intent':
                return self.client_experience()
            elif found_match and intent == 'partnerships_intent':
                return self.partnerships()
            elif found_match and intent == 'future_outlook_intent':
                return self.future_outlook()
            elif found_match and intent == 'industry_expertise_intent':
                return self.industry_expertise()

        if not found_match:
            return self.no_match()

    def describe_services(self):
        responses = ("CODSOFT provides comprehensive IT consultancy services.\n",
                     "Our services include IT strategy, cybersecurity, cloud solutions, and more.\n")
        return random.choice(responses)

    def answer_why(self):
        responses = ("CODSOFT is here to optimize your IT operations.\n",
                     "We aim to enhance your business efficiency through IT consultancy.\n")
        return random.choice(responses)

    def about_codsoft(self):
        responses = (
        "CODSOFT is a leading IT consultancy firm specializing in empowering businesses with technology.\n",
        "We are committed to delivering cutting-edge IT solutions tailored to your needs.\n")
        return random.choice(responses)

    def pricing(self):
        responses = ("Our pricing model is designed to be flexible and competitive.\n",
                     "We offer transparent pricing based on the scope and complexity of the project.\n")
        return random.choice(responses)

    def technology_stack(self):
        responses = ("We leverage state-of-the-art technologies to deliver robust solutions.\n",
                     "Our technology stack includes leading platforms and frameworks.\n")
        return random.choice(responses)

    def client_experience(self):
        responses = ("Client satisfaction is at the heart of everything we do.\n",
                     "We have a proven track record of delivering exceptional client experiences.\n")
        return random.choice(responses)

    def partnerships(self):
        responses = ("We collaborate with top-tier partners to offer you the best solutions.\n",
                     "Our partnerships with industry leaders ensure you get cutting-edge technology.\n")
        return random.choice(responses)

    def future_outlook(self):
        responses = ("We are constantly innovating to meet future challenges.\n",
                     "Our vision is to lead the way in IT consultancy and technology solutions.\n")
        return random.choice(responses)

    def industry_expertise(self):
        responses = ("With deep industry expertise, we understand your specific needs.\n",
                     "Our consultants bring extensive knowledge across various sectors.\n")
        return random.choice(responses)

    def no_match(self):
        responses = ("Could you please provide more details?\n",
                     "I'd love to learn more about that.\n",
                     "Interesting. Could you elaborate further?\n",
                     "Tell me more!\n")
        return random.choice(responses)


codsoft_bot = CODSOFTBot()
codsoft_bot.greet()
