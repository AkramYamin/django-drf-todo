from taggit.managers import TaggableManager
from model_utils.models import TimeStampedModel
from django.db import models


class Category(TimeStampedModel):
    """
        The category model to describe category table.
        Inherit from TimeStampedModel to track creation and modification timestamps for table records
        Relations:
            - one owner per category.
    """
    # owner = models.ForeignKey('UserModel', related_name='categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"
        ordering = ('created',)


class Task(TimeStampedModel):
    """
        The task model to describe task table.
        Inherit from TimeStampedModel to track creation and modification timestamps for table records
        Relations:
            - one category per task.
            - multiple tags per task.
            - one owner per task.
    """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="task_category", blank=True,
                                 null=True)
    # owner = models.ForeignKey('UserModel', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=False)
    due_date = models.DateField()
    # For tagging I'll use a third-party package
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
