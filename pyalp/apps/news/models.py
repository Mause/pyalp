from django.db import models
from django.conf import settings

# Create your models here.


class NewsItem(models.Model):
    """
    "news" => "userid BIGINT NOT NULL,
        itemid BIGINT NOT NULL AUTO_INCREMENT,
        itemtime datetime NULL,
        headline varchar(60) NULL,
        news_article BLOB NULL,
        hide_item BOOL NOT NULL,
        PRIMARY KEY (itemid)",
    """

    # userid BIGINT NOT NULL,
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False
    )

    # itemtime datetime NULL,
    itemtime = models.DateTimeField()

    # headline varchar(60) NULL,
    headline = models.CharField(max_length=60)

    # news_article BLOB NULL,
    news_article = models.CharField(max_length=1500)

    # hide_item BOOL NOT NULL,
    hide_item = models.BooleanField(db_index=True)

    def __str__(self):
        return '{} by {}'.format(
            self.headline,
            self.author
        )
