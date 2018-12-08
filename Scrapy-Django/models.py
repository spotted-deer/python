from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=70)
    # 文章标题，CharField 表示对应数据库中表的列是用来存字符串的，'标题'是一个位置参数
    # （verbose_name），主要用于 django 的后台系统，不多做介绍。max_length 表示能存储的字符串
    # 的最大长度
    article_content = models.TextField('正文')
    # 文章正文，TextField 用来存储大文本字符
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 文章创建时间，DateTimeField用于存储时间，设定auto_now_add参数为真，则在文章被创建时会自动添加创建时间
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # 文章最后一次编辑时间，auto_now=True表示每次修改文章时自动添加修改的时间


    article_image = models.FileField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    # 图片存放位置

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status = models.CharField('文章状态', max_length=1,
                                         choices=STATUS_CHOICES)
    # STATUS_CHOICES，field 的 choices 参数需要的值，choices选项会使该field在被渲染成form时被渲染为一个select组件，
    # 这里我定义了两个状态，一个是Draft（草稿），一个是Published（已发布），
    # select组件会有两个选项：Draft 和 Published。
    # 但是存储在数据库中的值分别是'd'和'p'，
    # 这就是 choices的作用。
    ARTICLE_TYPES = (
        ('1', '国内新闻'),
        ('2', '国际新闻'),
        ('3', '科技'),
        ('4', '焦点'),
    )
    category = models.CharField('Category', max_length=1,
                                             choices=ARTICLE_TYPES)
    # 文章的分类，ForeignKey即数据库中的外键。
    # 外键的定义是：如果数据库中某个表的列的值是另外一个表的主键。
    # 外键定义了一个一对多的关系，这里即一篇文章对应一个分类，而一个分类下可能有多篇文章。
    # 详情参考django官方文档关于ForeinKey的说明，
    # on_delete=models.SET_NULL表示删除某个分类（category）后该分类下所有的Article的外键设为null（空）

    views = models.PositiveIntegerField('浏览量', default=0, null=True)
    # 阅览量，PositiveIntegerField存储非负整数

    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.title
