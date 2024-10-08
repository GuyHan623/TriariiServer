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
    
    def delete_division_by_id(self, division_id: int):
        division = Division.objects.get(id=division_id)
        division.delete()


class MessageAccess:
    def create_message(self, division_id:int, msg_content:str, msg_done:bool):
        message = Message(divisionid = division_id, content=msg_content, done=msg_done)
        message.save()
        return message
    
    def get_all_messages(self):
        return Message.objects.all()

    def get_message_by_message_id(self, msg_id:int):
        return Message.objects.all(id=msg_id)
    
    def update(self, msg_id=None, new_content=None, new_done=None):
        if msg_id is None:
            return
        else:
            message = Message.objects.get(id=msg_id)
            if new_content is not None:
                message.content = new_content
            if new_done is not None:
                message.done = new_done
            return message
    
    def delete_message_by_message_id(self, msg_id: int):
        message = Message.objects.get(id=msg_id)
        message.delete()

class AgentAcess:
    def create_agent(self, division_id:int):
        agent = Agent(divisionid = division_id)
        agent.save()
        return agent
    
    def get_all_agents(self):
        return Agent.objects.all()
    
    def get_agent_by_agent_id(self, agent_id:int):
        return Agent.objects.all(id=agent_id)
    
    def delete_agent_by_agent_id(self, agent_id: int):
        agent = Agent.objects.get(id=agent_id)
        agent.delete()

class DispatchAccess:
    def create_dispatch(self, msg_id:int, agent_id:int):
        dispatch = Dispatch(messageid=msg_id, agentid=agent_id)
        dispatch.save()
        return dispatch
    
    def get_all_dispatches(self):
        return Dispatch.objects.all()

    def get_dispatch_by_dispatch_id(self, dispatch_id:int):
        return Dispatch.objects.all(id=dispatch_id)
    
    def delete_dispatch_by_dispatch_id(self, dispatch_id: int):
        dispatch = Dispatch.objects.get(id=dispatch_id)
        dispatch.delete()
