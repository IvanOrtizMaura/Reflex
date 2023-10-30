import os
import openai
import reflex as rx

openai.api_key = os.environ("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

class QA(rx.Base):
    """ A question and anser pair """

    question: str
    answer: str
    
    DEFAULT_CHATS = {
        "Intros": [],
    }

class State(rx.State):
    """ The app state."""

    chats: dict[str, list[QA]] = DEFAULT_CHATS

    current_chat= "Intros"

    quetion: str 

    processing: bool = False    

    new_chat_name:str = ""  

    drawer_open: bool = False

    modal_open: bool = False    

def create_chats(self):
    """Create a new chat"""

    self.current_chat = self.new_chat_name
    self.chats[self.new_chat_name] = []

    self.modal_open = False
def toggle_modal(self):
    """Toggel the new chat modal"""

    self.modal_open = not self.modal_open

def toggle_drawer(self):
    """Toggle the drawer"""

    self.drawer_open = not self.drawer_open
    