from django.db import models


# class employee(models.Model):
#     name = models.CharField(max_length= 255, null= True)
#     email = models.EmailField(max_length= 255, null= True)
#     password = models.CharField(max_length= 255, null= True)

#     class Meta:
#         ordering = ['email']

#     def __str__(self):
#         return self.email

# class employeeInfo(models.Model):
#     employee_data = models.ForeignKey(employee, null = True, on_delete=models.CASCADE)

# class employee_details(models.Model):
#     headline = models.CharField(max_length=100)
#     employeeInfo = models.ManyToManyField(employee)

#     class meta:
#         ordering = ['headline']

#     def __str__(self):
#         return self.headline

