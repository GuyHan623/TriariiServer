from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Division
# Create your views here.

from .models import Division, Message, Agent, Dispatch


class DivisionViews:
    def create_division(self, request):
        division = Division()
        division.save()
        return redirect('Division')

    def get_all_divisions(self, request):
        all_divisions = Division.objects.all()
        return render(request, 'division_list.html', {'divisions': all_divisions})
        

    def get_division_by_id(self, request, division_id: int):
        division = Division.objects.get(id=division_id)
        return render(request, 'division_list.html', {'division': division})
    
class MessageViews:
    def create_message(self, request,  division_id:int, msg_content:str, msg_done:bool):
        message = Message(divisionid = division_id, content=msg_content, done=msg_done)
        message.save()
        return redirect('Message')
    
    def get_all_messages(self):
        return Message.objects.all()

    def get_message_by_message_id(self, msg_id:int):
        return Message.objects.all(id=msg_id)
    
class AgentViews:
    def create_agent(self, division_id:int):
        agent = Agent(divisionid = division_id)
        agent.save()
        return agent
    
    def get_all_agents(self):
        return Agent.objects.all()
    
    def get_agent_by_agent_id(self, agent_id:int):
        return Agent.objects.all(id=agent_id)

class DispatchViews:
    def get_all_dispatches(self):
        return Dispatch.objects.all()



