from django.db import models

class Forum(models.Model):

    forum_id = models.AutoField(primary_key=True)
    forum_title = models.CharField(max_length=50)
    forum_text = models.TextField(default='none')
    forum_date = models.DateField(auto_now_add=True)


    def __unicode__(self):
        return self.forum_id

class Comments (models.Model):
    forum_id = models.AutoField(primary_key=True)
    comment_id = models.ForeignKey(Forum, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=50)
    comment_text = models.TextField(default='none')
    comment_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.comment_id
