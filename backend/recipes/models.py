from django.db import models


# class Recipe(models.Model):
#     name = models.CharField(
#         'название',
#         max_length=200,
#         db_index=True
#     )
#     year = models.PositiveIntegerField(
#         'год',
#         validators=(validate_year, ),
#         db_index=True
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.SET_NULL,
#         related_name='titles',
#         verbose_name='категория',
#         null=True,
#         blank=True
#     )
#     description = models.TextField(
#         'описание',
#         max_length=255,
#         null=True,
#         blank=True
#     )
#     genre = models.ManyToManyField(
#         Genre,
#         related_name='titles',
#         verbose_name='жанр'
#     )

#     class Meta:
#         verbose_name = 'Произведение'
#         verbose_name_plural = 'Произведения'

#     def __str__(self):
#         return self.name

