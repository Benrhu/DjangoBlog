from django.db import models

class Post(models.Model):
    category = models.TextField()
    image = models.ImageField(upload_to="static/images")
    title = models.CharField(max_length=255)
    intro = models.TextField()
    slug = models.SlugField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def _str_(self):
        return self.title + ' | ' + str(self.auhor)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    mensaje = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

        