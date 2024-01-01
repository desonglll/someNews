# Django 新闻管理后台项目 Readme

## 项目简介
这是一个基于 Django 框架开发的新闻管理后台项目，旨在提供一个简单而功能强大的平台，用于管理和发布新闻内容。项目包含以下主要模型：

- `title`: 用于存储新闻标题的字符字段。
- `content`: 用于存储新闻内容的文本字段，支持 null 值。
- `release_date`: 用于存储新闻发布日期的日期时间字段。
- `nid`: 用于存储新闻类型的字符字段，提供了预定义的选项。
- `image`: 用于存储上传的标题图的图像字段。
- `photo`: 用于存储上传的图片的图像字段。
- `price`: 用于存储新闻价格的整数字段，支持默认值和可选的空白值。

## 项目配置

### 数据库设置
确保在项目根目录的 `settings.py` 文件中配置数据库连接，以及执行数据库迁移：

```bash
python manage.py makemigrations
python manage.py migrate
```

### 媒体文件配置
配置媒体文件的存储路径，确保在 `settings.py` 中设置了以下内容：

```python
# settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
```

## 如何使用

1. 在 Django 管理后台中创建新的新闻条目。
2. 填写新闻标题、内容、发布日期、类型等信息。
3. 上传标题图和图片，可选填价格字段。
4. 保存并发布新闻。

## 注意事项

- 确保在部署时配置好媒体文件的静态服务，以便正确显示上传的图片和标题图。
- 定期备份数据库以防止数据丢失。

## 示例代码

```python
# models.py

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="新闻标题")
    content = models.TextField(null=True, blank=True, default="Coming soon...orz", verbose_name="新闻内容")
    release_date = models.DateTimeField(verbose_name="发布日期")
    nid = models.CharField(max_length=100, choices=choices, verbose_name="新闻类型")
    image = models.ImageField(blank=True, upload_to="uploads", verbose_name="上传标题图")
    photo = models.ImageField(blank=True, upload_to="uploads", verbose_name="上传图片")
    price = models.IntegerField(blank=True, default=0, verbose_name="价格")
```

这是一个简要的 Readme 文件，你可以根据实际情况进行修改和扩展。如果有其他问题，欢迎提出。