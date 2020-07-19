

class logit:

    _log_file = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " Was Called"
        print(log_string)

        with open(self._log_file, 'a')as opened_file:
            opened_file.write(log_string+ '\n')
        
        self.notify()

        return self.func(*args)

    def notify(self):
        print("Email Sent")
        pass


class email_logit(logit):
    def __init__(self, email='admin@gmail.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)


logit._log_file = 'out1.log'
@email_logit
def myfunc1():
    pass

myfunc1()