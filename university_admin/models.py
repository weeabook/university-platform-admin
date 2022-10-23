# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appeals(models.Model):
    id = models.AutoField(unique=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    title = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'appeals'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    id = models.AutoField(unique=True)
    content = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Comments(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groups(models.Model):
    id = models.AutoField(unique=True)
    content = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Lessons(models.Model):
    id = models.AutoField(unique=True)
    group = models.OneToOneField(Groups, models.DO_NOTHING)
    up_week = models.BooleanField()
    week_day = models.IntegerField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    classroom = models.TextField()
    subject = models.TextField()

    class Meta:
        managed = False
        db_table = 'lessons'


class News(models.Model):
    id = models.AutoField(unique=True)
    img_url = models.TextField()
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class NewsCategory(models.Model):
    id = models.AutoField(unique=True)
    news = models.OneToOneField(News, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'news_category'


class Roles(models.Model):
    id = models.AutoField(unique=True)
    role_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Schedulefile(models.Model):
    filename = models.FileField(upload_to ='uploads/')

    class Meta:
        managed = False
        db_table = 'schedulefile'


class SchemaMigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    dirty = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class UserComments(models.Model):
    id = models.AutoField(unique=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    comment = models.OneToOneField(Comments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_comments'


class UserGroup(models.Model):
    id = models.AutoField(unique=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    group = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_group'


class UserRole(models.Model):
    id = models.AutoField(unique=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    role = models.OneToOneField(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'


class Users(models.Model):
    id = models.AutoField(unique=True)
    username = models.TextField()
    surname = models.TextField()
    patronymic = models.TextField(blank=True, null=True)
    email = models.TextField()
    password_hash = models.TextField()
    recordbook = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
