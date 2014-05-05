from django.db import models

class Targets(models.Model):
    BODY_TYPE = ((1, "planet"), 
        (2, "asteroid"),
        (3, "comet"),
        (4, "satellite"),
        (5, "sun"),
        (6, "deepspace"),
        (7, "extra-terrestrial")
        )
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=150)
    slug            = models.CharField(max_length=50, null=True, blank=True)
    body_type       = models.IntegerField(max_length=3, choices=BODY_TYPE)  # planet, asteroids, outer space
    image_url       = models.CharField(max_length=150)
    characteristics = models.CharField(max_length=3000, null=True, blank=True, default='')
    curiosities     = models.CharField(max_length=3000, null=True, blank=True, default='')
    sim_related     = models.CharField(max_length=3000, null=True, blank=True, default='')
    use_in_sim      = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Targets'

class Missions(models.Model):
    ERA = (
        (1, 'Past'),
        (2, 'Present'),
        (3, 'Future'),
        (0, 'Concept')
        )

    id              = models.AutoField(primary_key=True, db_index=True)
    target          = models.ForeignKey(Targets, db_index=True)
    era             = models.IntegerField(max_length=3, choices=ERA, db_index=True)
    name            = models.CharField(max_length=80)
    codename        = models.CharField(max_length=50, null=True, blank=True)
    hashed          = models.CharField(max_length=150)
    image_url       = models.CharField(max_length=250)
    launch_dates    = models.CharField(max_length=80, null=True, blank=True)
    twitter         = models.CharField(max_length=45, null=True, blank=True)
    fb_page         = models.CharField(max_length=150, null=True, blank=True)
    
    # ALTER TABLE xploration_missions ADD COLUMN twitter character varying(45);
    #ALTER TABLE xploration_missions ADD COLUMN fb_page character varying(150);

    def __unicode__(self):
        return self.codename

    class Meta:
        verbose_name_plural = 'Missions'
        ordering = ['codename']

class Details(models.Model):
    DETAIL_TYPE = (
        (1, 'goal'),
        (2, 'accomplishment'),
        (3, 'read_more'),
        (4, 'mission_link'),
        (5, 'event'),
        (6, 'fact'),
        (7, 'status'),
        (8, 'article'),
        (9, 'publications'),
        (10, 'archive_link'),
        (11, 'news')
        )

    id              = models.AutoField(primary_key=True, db_index=True)
    mission         = models.ForeignKey(Missions, db_index=True)
    detail_type     = models.IntegerField(max_length=3, choices=DETAIL_TYPE)
    header          = models.CharField(max_length=150, db_index=True)
    body            = models.CharField(max_length=3000)
    date            = models.DateTimeField(null=True, blank=True, db_index=True)
    image_link      = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return str(self.mission.name)+' - '+str(self.header)

    class Meta:
        verbose_name_plural = 'Details'
        ordering = ['mission__name']

class Planets(models.Model):

    id          = models.AutoField(primary_key=True)
    target      = models.ForeignKey(Targets)
    discover    = models.CharField(max_length=20, null=True, blank=True)
    rings       = models.BooleanField()         
    light       = models.CharField(max_length=50)   
    mass        = models.CharField(max_length=50)   
    diameter    = models.CharField(max_length=50)   
    density     = models.CharField(max_length=50)
    gravity     = models.CharField(max_length=50)   
    l_day       = models.CharField(max_length=50)   
    l_year      = models.CharField(max_length=50)   
    eccent      = models.CharField(max_length=50)   
    distance    = models.CharField(max_length=50)   
    perihelion  = models.CharField(max_length=50)   
    aphelion    = models.CharField(max_length=50)   
    inclination = models.CharField(max_length=10)   
    active      = models.BooleanField()         
    atmosphere  = models.CharField(max_length=50)
     
    def __unicode__(self):
        return str(self.target.name)

    class Meta:
        verbose_name_plural = 'Planets Physics'
        ordering = ['target__name']


class PayloadBusTypes(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100)
    category    = models.CharField(max_length=10)
    description = models.CharField(max_length=1500)
    link        = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return str(self.category)+' '+str(self.name)

    class Meta:
        verbose_name_plural = 'PL and BUS Types'
        ordering = ['name']


class PayloadBusComps(models.Model):
    id          = models.AutoField(primary_key=True)
    pbtype      = models.ManyToManyField(PayloadBusTypes)
    name        = models.CharField(max_length=100)
    category    = models.CharField(max_length=10) #payload or bus
    description = models.CharField(max_length=1500)
    slug        = models.CharField(max_length=80)
    link        = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return str(self.category)+' '+str(self.name)

    class Meta:
        verbose_name_plural = 'PL and BUS Components'
        ordering = ['name']
