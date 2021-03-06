from django.db import models


class Module(models.Model):
    """
    "modules" => "`moduleid` int(10) unsigned NOT NULL auto_increment,
                `file` varchar(45) NOT NULL default '',
                `ordernum` int(10) unsigned NOT NULL default '0',
                `description` varchar(45) NOT NULL default '',
                `required` varchar(45) default NULL,
                PRIMARY KEY  (`moduleid`)",
    """

    # `file` varchar(45) NOT NULL default '',

    # in this implementation, we store the name of a
    # template tag instead
    name = models.CharField(max_length=45)

    # `ordernum` int(10) unsigned NOT NULL default '0',
    ordernum = models.IntegerField()

    # in the original php based implementation, you would set
    # ordernum to 0 to disable a module. this is cleaner
    enabled = models.BooleanField(default=True)

    # `description` varchar(45) NOT NULL default '',
    description = models.CharField(max_length=45)

    # `required` varchar(45) default NULL,
    required = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return '{} {} at position {}'.format(
            'enabled' if self.enabled else 'disabled',
            self.name,
            self.ordernum
        )
