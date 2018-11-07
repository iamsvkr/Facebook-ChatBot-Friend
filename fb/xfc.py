from fbchat import Client
from fbchat.models import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def mesend(s):
	client = Client('shivamkumarrajput56789@gmail.com', 'shivam1998@@')
	client.send(Message(text=str(s)), thread_id=client.uid, thread_type=ThreadType.USER)
	client.logout()

class EchoBot(Client):
        def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
            self.markAsDelivered(thread_id, message_object.uid)
            self.markAsRead(thread_id)
    
            s = str(message_object)
            start = s.find(":")+1
            end = s.find(",", start)
            s1=s[start:end]
            #print(s1)
            
            bot = ChatBot('Bot')
            bot.set_trainer(ListTrainer)
            message = s1
            reply = bot.get_response(message)
            mesend(reply)
            
            if author_id != self.uid:
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)

while True:
    cl = EchoBot("shivamkumarrajput56789@gmail.com", "shivam1998@@")
    cl.listen()


