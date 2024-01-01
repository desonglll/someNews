from datetime import datetime

from django.db import models


class News(models.Model):
    """News Model

    This model represents a news item in the system.

    Attributes:
        choices (list): A list of tuples representing the available choices for the 'nid' field.

    Fields:
        title (str): The title of the news.
        content (str): The content of the news.
        release_date (datetime): The date and time when the news is released.
        nid (int): The type of the news, chosen from predefined choices.
        image (ImageField): An optional image field for uploading a title image.
        photo (ImageField): An optional image field for uploading additional images.
        price (int): The price associated with the news.

    Example:
        news_item = News.objects.create(
            title="Breaking News",
            content="This is a breaking news article.",
            release_date=datetime.now(),
            nid=1,  # representing '国内'
            image="path/to/title_image.jpg",
            photo="path/to/additional_image.jpg",
            price=10
        )

    """
    choices = {
        "0": "全部",
        "1": "国内",
        "2": "国际",
        "3": "娱乐",
        "4": "体育",
        "5": "财经",
        "6": "科技",
        "7": "时尚",
        "8": "购物"
    }

    title = models.CharField(max_length=100, verbose_name="新闻标题")
    content = models.TextField(null=True, blank=True, default="Coming soon...orz", verbose_name="新闻内容")
    release_date = models.DateTimeField(verbose_name="发布日期")
    nid = models.CharField(max_length=100, choices=choices, verbose_name="新闻类型")
    image = models.ImageField(blank=True, upload_to="uploads", verbose_name="上传标题图")
    photo = models.ImageField(blank=True, upload_to="uploads", verbose_name="上传图片")
    buy = models.CharField(max_length=100, blank=True, default=0, verbose_name="是否可购买")
    price = models.IntegerField(blank=True, default=0, verbose_name="价格")

    def __str__(self):
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object based on its title.

        Example:
            >>> obj = YourClassName(title="example")
            >>> print(obj)
            'example'
        """
        return self.title
