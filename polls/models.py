from django.db import models

# Create your models here.


class Question(models.Model):
    # 字符字段被表示为 CharField ，定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length 参数。这个参数的用处不止于用来定义数据库结构，也用于验证数据，我们稍后将会看到这方面的内容。
    question_text = models.CharField(max_length=200)
    # 日期时间字段被表示为 DateTimeField 。
    pub_date = models.DateTimeField('date published')

    # 每个Field类实例变量的名字（例如question_text或pub_date ）也是字段名，所以最好使用对机器友好的格式。你将会在Python代码里使用它们，而数据库会将它们作为列名。


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
