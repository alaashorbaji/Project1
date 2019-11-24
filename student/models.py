from django.db import models




class Dr(models.Model):
    Dr_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Dr_name

class Subjects(models.Model):
    Sub_name = models.CharField(max_length=100)
    Dr_name = models.ForeignKey(Dr,on_delete=models.CASCADE)

    def __str__(self):
        return self.Sub_name

class Students(models.Model):
    S_name = models.CharField(max_length=100)
    Dr_name = models.ForeignKey(Dr, on_delete=models.CASCADE)
    Sub_name = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    def __str__(self):
        return self.S_name

