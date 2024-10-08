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


    
    

