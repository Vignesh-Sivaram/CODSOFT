class EmergencyBot:
    responses = {
        "1": "Connecting you to Police services...\n Visit: https://services.india.gov.in/service/detail/register-online-complaints-tamil-nadu-police",
        "2": "Connecting you to Fire Rescue services...\n Visit: https://services.india.gov.in/service/detail/fire-rescue-services",
        "3": "Connecting you to Ambulance services...\n Visit: https://services.india.gov.in/service/detail/ambulance-services",
        "4": "Connecting you to Disaster Management services...\n Visit: https://services.india.gov.in/service/detail/disaster-management",
        "5": "Connecting you to the Women's Helpdesk...\n Visit: http://www.ncw.nic.in/helplines",
        "6": "Connecting you to the Child Helpdesk...\n Visit: https://services.india.gov.in/service/detail/child-helpline-services",
        "7": "Connecting you to the Senior Citizen Helpdesk...\n Visit: https://services.india.gov.in/service/detail/senior-citizen-helpline",
        "8": "Connecting you to Cyber Crime services...\n Visit: https://cyberpolice.nic.in/",
    }

    exit_commands = ("quit", "exit", "goodbye", "bye", "stop")

    def __init__(self):
        self.greeted = False

    def greet(self):
        if not self.greeted:
            print("Hi, I'm your Emergency Helpline Bot! How can I assist you today?")
            print(
                """Please select an option by typing the corresponding number:
1. Connect with Police
2. Connect with Fire Rescue
3. Connect with Ambulance
4. Connect with Disaster Management
5. Connect with Women Helpdesk
6. Connect with Child Helpdesk
7. Connect with Senior Citizen Helpdesk
8. Connect with Cyber Crime
(Type 'exit' to quit.)"""
            )
            self.greeted = True

    def handle_input(self, user_input):
        user_input = user_input.strip().lower()

        if user_input in self.exit_commands:
            print("Thank you for using the Emergency Helpline Bot. Stay safe!")
            return True 

        if user_input in self.responses:
            print(self.responses[user_input])
        else:
            print("I'm sorry, I didn't understand that. Please enter a valid option or type 'exit' to quit.")
        return False

    def start(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if self.handle_input(user_input):
                break

if __name__ == "__main__":
    emergency_bot = EmergencyBot()
    emergency_bot.start()
