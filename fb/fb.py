from fbchat import Client
from fbchat.models import *

client = Client('shivamkumarrajput56789@gmail.com', 'shivam1998@@')

print('Own id: {}'.format(client.uid))

client.send(Message(text='how r u'), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()

#%%
from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        #log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        #print(message_object)
        s = str(message_object)
        start = s.find(":")+1
        end = s.find(",", start)
        s1=s[start:end]
        print(s1)
        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot("shivamkumarrajput56789@gmail.com", "shivam1998@@")
client.listen()
#%%