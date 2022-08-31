from django import forms
from polls.modeks import User

class UserFrom(froms,Modelfroms):
    class Meta:
        model=User
        fields="__all__"
        widgets={
            "uname":froms.TextInput(attrs={"class":"form-control"}),
            "ufirst_name":froms.First_nameInput(attrs={"class":"from-control"}),
            "ulast_name":froms.last_nameInput(attrs={"class":"from-control"}),
            }