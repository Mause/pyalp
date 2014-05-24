from django.db import models
from django.conf import settings


class UserMetadata(models.Model):
    class Meta:
        verbose_name_plural = 'user metadata'
    # already provided by the parent User model
    # username varchar(40) NOT NULL,
    # first_name varchar(30) NOT NULL,
    # last_name varchar(30) NOT NULL,
    # passwd varchar(34) NOT NULL,
    # email varchar(60) NOT NULL,

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    # paid BOOL DEFAULT '0',
    paid = models.BooleanField(default=False)

    # language varchar(10) NOT NULL,
    language = models.CharField(max_length=10)

    # skin varchar(45) NOT NULL,
    skin = models.CharField(max_length=45)

    # dateformat varchar(45) NOT NULL,
    dateformat = models.CharField(max_length=45)

    # display_email BOOL NOT NULL,
    display_email = models.BooleanField(default=False)

    # gender varchar(10) NOT NULL,
    # do we really care? can we not?

    # gaming_group varchar(20) NOT NULL,
    gaming_group = models.CharField(max_length=20)

    # quote varchar(255) NULL,
    quote = models.CharField(max_length=255)

    # room_loc int(11) DEFAULT '0',
    room_loc = models.IntegerField()

    # really worth implementing?
    # caffeine_mg double(10,2) DEFAULT '0',
    caffeine_mg = models.FloatField()

    # proficiency int(4) NOT NULL,
    proficiency = models.IntegerField()

    # probably going to have to implement this via a non-blocking
    # middleware :/
    # recent_ip varchar(15) NOT NULL,
    recent_ip = models.CharField(max_length=15)

    # display_ip BOOL NOT NULL,
    display_ip = models.BooleanField(default=False)

    # privacy or privilege level?
    # priv_level int(5) NOT NULL,
    priv_level = models.IntegerField()

    # presuming this is a session id, don't bother
    # sesid varchar(34) NULL,

    # date_of_arrival datetime NOT NULL,
    date_of_arrival = models.DateTimeField()

    # date_of_departure datetime NULL,
    date_of_departure = models.DateTimeField()

    # sharename varchar(35) NULL,
    sharename = models.CharField(max_length=35)

    # ftp? hah!
    # ftp_server BOOL DEFAULT '0',

    # what is this?
    # ccode varchar(34) NULL,

    # marathon? do we care?
    # marathon_points int(5) DEFAULT '0',
    # marathon_points_tourney int(10) DEFAULT '0',
    # marathon_rank int(10) DEFAULT '0',

    def __str__(self):
        return 'metadata for {}'.format(self.user.username)


class ComputerSpecification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True
    )

    # comp_proc varchar(60) NULL,
    processor = models.CharField(max_length=60)

    # comp_proc_spd varchar(60) NULL,
    processor_speed = models.CharField(max_length=60)

    # comp_proc_type varchar(60) NULL,
    processor_type = models.CharField(
        max_length=60,
        help_text='x64, x86, amd64_x86, etc'
    )

    # comp_mem varchar(60) NULL,
    memory = models.CharField(max_length=60)

    # comp_mem_type varchar(60) NULL,
    memory_type = models.CharField(max_length=60)

    # comp_hdstorage varchar(60) NULL,
    harddrive_storage = models.CharField(max_length=60)

    # comp_gfx_gpu varchar(60) NULL,
    gpu = models.CharField(max_length=60)

    # comp_gfx_type varchar(60) NULL,
    gpu_type = models.CharField(max_length=60)

    def __str__(self):
        return 'computer specification for {}'.format(self.user.username)
