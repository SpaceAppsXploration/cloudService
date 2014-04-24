from django.db import models

class Targets(models.Model):
    BODY_TYPE = ((1, "planet"), 
        (2, "asteroid"),
        (3, "comet"),
        (4, "satellite"),
        (5, "sun"),
        (6, "deepspace"))
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=150)
    body_type       = models.IntegerField(max_length=3, choices=BODY_TYPE)  # planet, asteroids, outer space
    image_url       = models.CharField(max_length=150)
    characteristics = models.CharField(max_length=3000, null=True, blank=True, default='')
    curiousities    = models.CharField(max_length=3000, null=True, blank=True, default='')
    sim_related     = models.CharField(max_length=3000, null=True, blank=True, default='')



class Missions(models.Model):
    ERA = (
        (1, 'Past'),
        (2, 'Present'),
        (3, 'Future'),
        (0, 'Concept')
        )

    id              = models.AutoField(primary_key=True)
    target          = models.ForeignKey(Targets)
    era             = models.IntegerField(max_length=3, choices=ERA)
    name            = models.CharField(max_length=80)
    codename        = models.CharField(max_length=50)
    hashed          = models.CharField(max_length=150)
    image_url       = models.CharField(max_length=250)
    launch_date     = models.DateTimeField(null=True, blank=True)
    

class Details(models.Model):
    DETAIL_TYPE = (
        (1, 'goals'),
        (2, 'accomplished'),
        (3, 'link'),
        (4, 'read_more'),
        (5, 'key_dates'),
        (6, 'headlines')
        )

    id              = models.AutoField(primary_key=True)
    mission         = models.ForeignKey(Missions)
    detail_type     = models.IntegerField(max_length=3, choices=DETAIL_TYPE)
    mission_type    = models.CharField(max_length=50)
    header          = models.CharField(max_length=150)
    body            = models.CharField(max_length=3000)
    date            = models.DateTimeField()        
     



