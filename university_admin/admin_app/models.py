from django.db import models


class Schedulefile(models.Model):
    filename = models.FileField("Документ", upload_to ='uploads/')

    class Meta:
        managed = False
        db_table = 'schedulefile'
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"


class Appeals(models.Model):
    user_id = models.IntegerField("ID Пользователя", blank=True, null=True)
    title = models.TextField("Название", blank=True, null=True)
    content = models.TextField("Текст", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appeals'
        verbose_name = "Обращение к ректору"
        verbose_name_plural = "Обращения к ректору"


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
    content = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Comments(models.Model):
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
    content = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Lessons(models.Model):
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
    img_url = models.TextField("Ссылка на фото")
    title = models.TextField("Название")
    content = models.TextField("Текст")
    created_at = models.DateTimeField("Дата",blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsCategory(models.Model):
    news = models.OneToOneField(News, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'news_category'


class Roles(models.Model):
    role_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SchemaMigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    dirty = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class UserComments(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING)
    comment = models.OneToOneField(Comments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_comments'


class UserGroup(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING)
    group = models.ForeignKey('Users', models.DO_NOTHING, related_name="group1")

    class Meta:
        managed = False
        db_table = 'user_group'


class UserRole(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING)
    role = models.OneToOneField(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'


class Users(models.Model):
    username = models.TextField('Имя')
    surname = models.TextField("Фамилия")
    patronymic = models.TextField('Отчество', blank=True, null=True)
    email = models.TextField('E-mail',)
    password_hash = models.TextField('Пароль',)
    recordbook = models.IntegerField('Новер зачетной книги', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
