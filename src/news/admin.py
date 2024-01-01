from django.contrib import admin
from .models import News
from django.contrib.admin.sites import AdminSite

News._meta.verbose_name = "news"
News._meta.verbose_name_plural = "news"


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', "release_date")  # 在列表中显示的字段
    pass


# 使用admin.AdminSite的实例，而不是直接设置AdminSite的类属性
custom_admin_site = admin.AdminSite(name='custom_admin')
custom_admin_site.site_header = "后台管理系统"
custom_admin_site.site_title = "后台管理系统"
custom_admin_site.index_title = "管理员"
admin.site.register(News, NewsAdmin)
