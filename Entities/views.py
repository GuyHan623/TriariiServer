from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Division
# Create your views here.

from .models import Division, Message, Agent, Dispatch


class DivisionAccess:
    def create_division(self):
        division = Division()
        division.save()
        return division()

    def get_all_divisions(self):
        return Division.objects.all()
    
    def get_division_by_id(self, division_id: int):
        return Division.objects.get(id=division_id)
    
class MessageAccess:
    def create_message(self, division_id:int, msg_content:str, msg_done:bool):
        message = Message(divisionid = division_id, content=msg_content, done=msg_done)
        message.save()
        return message
    
    def get_all_messages(self):
        return Message.objects.all()

    def get_message_by_message_id(self, msg_id:int):
        return Message.objects.all(id=msg_id)
    
class AgentAcess:
    def create_agent(self, division_id:int):
        agent = Agent(divisionid = division_id)
        agent.save()
        return agent
    
    def get_all_agents(self):
        return Agent.objects.all()
    
    def get_agent_by_agent_id(self, agent_id:int):
        return Agent.objects.all(id=agent_id)

class DispatchAccess:
    def get_all_dispatches(self):
        return Dispatch.objects.all()



