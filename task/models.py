from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=50)
    taskDescription=models.TextField()
    taskAssignDate=models.DateField(auto_now=False, auto_now_add=False)
    is_completed=models.BooleanField()
    
    def __str__(self):
        return f"{self.taskTitle}"

class TaskCategory(models.Model):
    CategoryName=models.CharField(max_length=50)
    task=models.ForeignKey(TaskModel, verbose_name="Category", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.CategoryName}"
        