#!/usr/bin/env python3

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from random import choice
import getpass

from web_actions import *
from chat_vocabular import *

api = {"api": "Hi! I'm just a small ChatBot, "
               "but I can search on google for you, "
               "play music on youtube, "
               "look for a helpful answers on stackoverflow "
               "and open several websites. "
               "Try me -> Enter 'google'/'youtube'/'stackoverflow' and what to find or "
               "enter 'sport'/'news'/'themarker'/geektime'/'facebook' and I'll open them for you", }

STANDARD_MSG = 50


class Chatbot:
    def __init__(self, title):
        self.top = Tk()
        self.top.title(title)
        
        self.messages_frame = Frame(self.top)
        
        self.my_msg = StringVar()  # For the messages to be sent.
        self.my_msg.set("")
        self.scrollbar = Scrollbar(self.messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = Listbox(self.messages_frame, height=15, width=50, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.msg_list.pack(side=LEFT, fill=BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()

        self.entry_field = Entry(self.top, textvariable=self.my_msg)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack()
        
        self.send_button = Button(self.top, text="Send", command=self.send)
        self.send_button.pack()

        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

    @staticmethod
    def start():
        mainloop()
        
    def analyze(self, msg):
        answer = Chatbot.analyzer(self, msg).get_message()
        if answer is list:
            self.write_list("Bot", answer)
        elif isinstance(answer, str):
            if len(answer) > STANDARD_MSG:
                self.write_in_chunks("Bot", answer, STANDARD_MSG)
            else:
                self.msg_list.insert(END, "Bot: %s" % answer)
            if answer in bye:
                self.top.quit()
        else:
            print (type(answer))

    def send(self, event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = self.my_msg.get().lower()
        self.my_msg.set("")  # Clears input field.
        self.msg_list.insert(END, "You: %s" % msg)
        self.analyze(msg)

    def on_closing(self, event=None):
        """This function is to be called when the window is closed."""
        self.top.quit()
        
    def write_list(self, name, list_of_sentences):
        self.msg_list.insert(END, '%s: %s' % (name, list_of_sentences[0]))
        for sent in list_of_sentences[1:]:
            self.msg_list.insert(END, '%s' % sent)
        
    def write_in_chunks(self, name, msg, chunk_size):
        self.write_list(name, list(self.chunkstring(msg, chunk_size)))

    @staticmethod
    def chunkstring(string, length):
        return (string[0+i:length+i] for i in range(0, len(string), length))

    @staticmethod
    def open_web(msg):
        for web_key in web_actions:
            if web_key in msg:
                if web_key in web_searces.keys():
                    search = '+'.join(msg.replace('%s' % web_key, '').split())
                    search_url(web_searces[web_key], search)
                    return 'Opening %s in a new tab for you, looking for %s' % (web_key, search)
                
                elif web_key in web_sites.keys():
                    open_url(web_sites[web_key])
                    return 'Opening %s in a new tab for you' % web_key
                    
    class analyzer:
        def __init__(self, chatbot, msg):
            self.chatbot = chatbot
        
            #words = msg.split()
            if any(word in msg for word in hi):
                self.answer = choice(greet) + ' ' + getpass.getuser()
            elif any(word in msg for word in bye):
                self.answer = choice(bye)
            elif any(word in msg for word in web_actions):
                self.answer = chatbot.open_web(msg)
            elif any(word in msg for word in thanks):
                self.answer = choice(thanks_res)
            elif any(word in msg for word in api.keys()):
                self.answer = api["api"]
            else:
                self.answer = choice(error)
            
        def get_message(self):
            return self.answer
        

if __name__ == '__main__':
    chatbot = Chatbot("Chatbot")
    chatbot.start()
