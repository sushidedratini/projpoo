class Notifier:
    def notify(self, user, message):
        raise NotImplementedError

class EmailNotifier(Notifier):
    def notify(self, user, message):
        print(f"Sending email to {user.name}: {message}")

class SMSNotifier(Notifier):
    def notify(self, user, message):
        print(f"Sending SMS to {user.name}: {message}")