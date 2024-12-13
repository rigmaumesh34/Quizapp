import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    class Meta:
        abstract=True



class Category(BaseModel):
    cat_name=models.CharField(max_length=100)

class Question(BaseModel):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)
    
    
class Answer(BaseModel):
    question=models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=True)