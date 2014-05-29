from django.db import models
from django.conf import settings

# Create your models here.


class TechSupportRequest(models.Model):
    """
    "techsupport" => "
        userid BIGINT NOT NULL,
        itemid BIGINT NOT NULL AUTO_INCREMENT,
        itemtime datetime NULL,
        severity int(2) DEFAULT '0',
        fixed BOOL DEFAULT '0',
        fixer BIGINT DEFAULT '0',
        info TEXT,
                result TEXT,
                assigned_to BIGINT(20) NOT NULL,
        PRIMARY KEY (itemid)",
    """
    # userid BIGINT NOT NULL,
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user')

    # itemtime datetime NULL,
    itemtime = models.DateTimeField()

    # severity int(2) DEFAULT '0',
    severity = models.IntegerField()

    # fixed BOOL DEFAULT '0',
    fixed = models.BooleanField()

    # fixer BIGINT DEFAULT '0',
    fixer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='fixer'
    )

    # info TEXT,
    info = models.TextField()

    # result TEXT,
    result = models.TextField()

    # assigned_to BIGINT(20) NOT NULL,
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='assigned_to'
    )
