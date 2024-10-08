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
    
    def get_all_messages(self, request):
        all_messages =  Message.objects.all()
        return render(request, 'message_list.html', {'Messages': all_messages})
    
    def get_message_by_message_id(self,request, msg_id:int):
        message =  Message.objects.all(id=msg_id)
        return render(request, 'message_list.html', {'Message': message})

class AgentViews:
    def create_agent(self, request, division_id:int):
        agent = Agent(divisionid = division_id)
        agent.save()
        return redirect('Agent')
    
    def get_all_agents(self, request):
        all_agents = Agent.objects.all()
        return render(request, 'agent_list.html', {'Agents': all_agents})
    
    def get_agent_by_agent_id(self, request, agent_id:int):
        agent =  Agent.objects.all(id=agent_id)
        return render(request, 'agent_list.html', {'Agent': agent})

class DispatchViews:
    def get_all_dispatches(self, request):
        all_dispatches =  Dispatch.objects.all()
        return render(request, 'dispatches_list.html', {'Disaptches': all_dispatches})


