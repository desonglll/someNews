from django.db import models

op = {
    "0": "创建",
    "1": "购买"
}


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='产品名称')
    description = models.TextField(blank=True, null=True, default="Coming soon...orz", verbose_name='产品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    quantity = models.IntegerField(default=0, verbose_name='数量')
    name = models.CharField(max_length=255, verbose_name='收件人姓名')
    address = models.CharField(max_length=255, verbose_name='地址')
    phone = models.CharField(max_length=255, verbose_name="电话号码")
    buy_date = models.DateTimeField(verbose_name='购买日期')
    operation = models.CharField(max_length=255, choices=op, default="0", verbose_name='操作')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
