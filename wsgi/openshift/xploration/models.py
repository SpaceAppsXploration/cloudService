from django.db import models



class Bodies(models.Model):
    TYPE = (1, "planet",
		    2, "asteroid",
		    3, "comet",
		    4, "satellite",
		    5, "sun",
		    6, "deepspace")
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=150)
    body_type       = models.CharField(max_length=25)
    temperature     = models.CharField(max_length=150)#kelvin
    mass            = models.CharField(max_length=150) 
    observ_area     = models.CharField(max_length=150)
    semi_major_axis = models.CharField(max_length=150)
    orbit_circumf   = models.CharField(max_length=150)
    eccentricity    = models.CharField(max_length=150)
    inclination     = models.CharField(max_length=150)


class Missions(models.Model):
    id              = models.AutoField(primary_key=True)
    hashed          = models.CharField(max_length=150)
    code            = models.CharField(max_length=150)
    goals           = models.CharField(max_length=1000)
    accomplished    = models.CharField(max_length=1000)
    link            = models.CharField(max_length=250)
    read_more       = models.CharField(max_length=250)
    key_dates       = models.CharField(max_length=250)
    headlines       = models.CharField(max_length=1000)
    mission_type    = models.CharField(max_length=50)
    image_url       = models.CharField(max_length=250)
    destination     = models.ForeignKey(Bodies)



