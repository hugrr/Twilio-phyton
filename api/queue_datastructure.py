from twilio.rest import Client
from random import randint

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure



class Queue:
    
    def __init__(self, mode='FIFO'):
        self.account_sid = 'AC7da26d078cf9402c764a5b4b8156e065'
        self.auth_token = '966588841413ac70bee087d2525b81e6'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []

        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode

    def enqueue(self, item):
        if self._mode =='FIFO':
            self._queue.insert(0, item)
            message = self.client.messages \
                        .create(
                            body="te agregaron y hay x personas antes",
                            from_='+56937610171',
                            to='+56964524232'
                        )
        print(message.sid)
       
        

         
        # fill this function with the logic needed to make it work
   

    def dequeue(self):
        if self._mode =='FIFO':
            # if self.zize > 0
            
            message = self.client.messages \
                        .create(
                            body="te eliminasmos de la cola",
                            from_='+56937610171',
                            to='+56964524232'
                        )
            print(message.sid)
   
       
        # fill this function with the logic needed to make it work
        return self._queue.pop()

    def get_all(self):
        return self._queue

    def size(self):
        return len(self._queue)

    
        

      
    

