from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from PIL import Image
from django.db.models import Q
from article.models import Article
import dbl
from user.models import CustomUser


class Software(models.Model):
    name = models.CharField('Наименование ПО', max_length = 200)
    name_small = models.CharField('Мини-Наименование ПО', max_length = 50, blank=True, null=True)
    price = models.FloatField('Цена', blank=True, validators=[MinValueValidator(0)])
    is_free = models.BooleanField('Бесплатно/Платно', default=True, db_index=True)
    description = models.TextField('Описание')
    description_medium = models.TextField('Среднее описание', max_length = 400)
    description_small = models.TextField('Короткое описание', max_length = 150)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    modification = models.BooleanField('Возможность доработки', default=True)
    size = models.FloatField('Размер', blank=True, validators=[MinValueValidator(0)], null=True)
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, null=True)
    date_of_delete = models.CharField('Дата удаления', blank=True, max_length = 20, null=True, db_index=True)
    file = models.FileField('Ссылка на программу', upload_to="file_software/", blank=True, null=True)
	# soft_image = models.ImageField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ПО'
        verbose_name_plural = 'Каталог'

    # Ф-ия получения списка приложений
    def get_addition(self):

        # Получаем список приложений данного ПО (ФАЙЛЫ, ФОТОГРАФИИ)
        software_img = Addition.objects.filter(software__id = self.id, date_of_delete=None)
        return software_img


    # Ф-ия получения главного фото ПО для каталога
    def get_main_photo(self):
        try:

            main_img = Addition.objects.filter(software__id = self.id, date_of_delete=None, is_main=True)[:1]

            if not main_img:

                main_img = Addition.objects.filter(software__id = self.id, date_of_delete=None)[:1]

        except:

            return None

        return main_img

    # Ф-ия получения списка тегов 
    def get_tags(self):

        # Получаем список тегов данного ПО
        software_tag = Tag.objects.filter(softwares__id=self.id, visibility=True, date_of_delete=None)
        return software_tag


    # Ф-ия получения списка классификаций
    def get_classifications(self):

        # Хэш классификаций ПО
        classif = {}
        # Строка фильтра для хлебных крошек
        str_filter_for_breadcrumb = ""

        # Получение списка всех классификаций ПО из таблицы Software_Classification_Value
        software_classifications = Classification_Value.objects.filter(softwares__id = self.id)

        # Переменная для составления строки классификаций ПО (Грузоперевозки, перевозки)
        str_clas = ""

        # Дальнейшие действия нужны для составления словаря классификаций данного ПО
        for clas_val in software_classifications:

            if clas_val:
                
                # Получение одной записи из Classification для получения названия классификации
                clas = Classification.objects.get(id = clas_val.classification.id)

                if clas.id == 1 :

                    # Получаем значение ключа, если есть:
                    if classif.get("type"):

                        # Составляем строку значений классификации
                        str_clas = str(classif.get("type")) + ", " + str(clas_val)
                        # Составляем строку для хлeбных крошек
                        str_filter_for_breadcrumb = str_filter_for_breadcrumb + "&" + "classification_1_value_"+str(clas_val.id)+"="+str(clas_val.id)

                        # Добавляем ключ и значение в словарь
                        classif["type"] = str_clas

                    else:

                        # Добавляем ключ и значение в словарь
                        classif["type"] = clas_val
                        # Добавляем строку для хлeбных крошек
                        str_filter_for_breadcrumb = "classification_1_value_"+str(clas_val.id)+"="+str(clas_val.id)

                elif clas.id == 2 :

                    # Получаем значение ключа, если есть:
                    if classif.get("area"):

                        # Составляем строку значений классификации
                        str_clas = str(classif.get("area")) + ", " + str(clas_val)

                        # Добавляем ключ и значение в словарь
                        classif["area"] = str_clas

                    else:

                        # Добавляем ключ и значение в словарь
                        classif["area"] = clas_val

                elif clas.id == 3 :

                    # Добавляем ключ и значение в словарь
                    classif["type_of_use"] = clas_val

                elif clas.id == 4 :

                    # Добавляем ключ и значение в словарь
                    classif["access"] = clas_val

                elif clas.id == 5 :

                    # Добавляем ключ и значение в словарь
                    classif["extra_install"] = clas_val

                elif clas.id == 6 :

                    # Добавляем ключ и значение в словарь
                    classif["install"] = clas_val

        return classif, str_filter_for_breadcrumb   


    # Ф-ия получения списка областей применения
    def get_area(self):

        # Массив классификаций ПО
        areas = []

        # Получение списка всех классификаций ПО из таблицы Software_Classification_Value
        software_classifications = Classification_Value.objects.filter(softwares__id = self.id)

        # Дальнейшие действия нужны для составления словаря классификаций данного ПО
        for clas_val in software_classifications:

            # Получение одной записи из Classification для получения названия классификации
            clas = Classification.objects.get(id = clas_val.classification.id)

            if clas.id == 2:

                areas.append(str(clas_val))



        return areas   
    

    # Ф-ия получения списка видов ПО
    def get_type(self):

        # Хэш классификаций ПО
        types = []
                # Строка фильтра для хлебных крошек
        str_filter_for_breadcrumb = ""

        # Получение списка всех классификаций ПО из таблицы Software_Classification_Value
        software_classifications = Classification_Value.objects.filter(softwares__id = self.id)

        # Дальнейшие действия нужны для составления словаря классификаций данного ПО
        for clas_val in software_classifications:


            # Получение одной записи из Classification для получения названия классификации
            clas = Classification.objects.get(id = clas_val.classification.id)

            if clas.id == 1:

                types.append(str(clas_val))

                # Составляем строку для хлeбных крошек
                str_filter_for_breadcrumb = str_filter_for_breadcrumb + "&" + "classification_1_value_"+str(clas_val.id)+"="+str(clas_val.id)

        return types, str_filter_for_breadcrumb


    # Ф-ия проверки является ли данное ПО избранным у конкретного клиента
    def is_favourite(self, client):
        try:
            return Favourite.objects.filter(software=self.id, client=client )
        except:
            return None


    @staticmethod
    # Ф-ия получения списка избранных по клиенту
    def get_favourites_by_user(client):
        # return Software.objects.filter(classification__id = self.id, visibility=True).order_by('value')
        return Software.objects.filter(favourite__client=client.id)

    
    @staticmethod
    # Ф-ия получения списка загрузок в Download таблице по клиенту
    def get_downloads_by_user(client):
        return Software.objects.filter(download__client=client.id)


    @staticmethod
    # Ф-ия получения списка ПО по тегам
    def get_softwares_by_tags(soft_list, list_tags):
        return soft_list.filter(tag__name__in=list_tags).distinct()


    # Ф-ия получения списка похожих ПО
    def get_similars(self):
        software_id = int(self.id)
        software_list = []
        soft_raw = Software.objects.raw('''select softwares.*
                                        from software_software softwares
                                        inner join software_tag_softwares st on st.software_id = softwares.id 
                                        and st.tag_id in 
                                        (select tag_id from software_tag_softwares where software_id = %s) 
                                        where softwares.id != %s
                                        group by softwares.id
                                        order by count(st.id) desc ''', [software_id, software_id] )

        for p in soft_raw:
            software_list.append(p)
        
        return software_list


    # Ф-ия получения облака тегов для ПО
    def get_similars_tags(self):
        software_id = int(self.id)
        tag_list = []
        tag_raw = Tag.objects.raw('''select distinct tags.*
                                        from new_db.software_tag tags
                                        inner join new_db.software_tag_softwares st on st.tag_id = tags.id 
                                        and st.software_id in 
                                        (select softwares.id
                                        from new_db.software_software softwares
                                        inner join new_db.software_tag_softwares st on st.software_id = softwares.id 
                                        and st.tag_id in 
                                        (select tag_id from new_db.software_tag_softwares where software_id = %s))
                                        group by tags.name
                                        order by tags.name''', [software_id] )

        for p in tag_raw:
            tag_list.append(p)   
        return tag_list


    # Ф-ия фильтрации По по одной классификации (по её id)
    @staticmethod
    def software_list_by_type(cl_val=None):
    
        # Проверка значения поля формы поиска
        if str(cl_val) !="" and str(cl_val).isdigit():

            soft_list = Software.objects.filter(date_of_delete=None, visibility=True)

            # Добавление условия фильтрации
            cond =Q(classification_value=int(cl_val))

            # Фильтрация списка всех ПО по выбранной классификации
            return soft_list.filter(cond)

        return None

    # Методы получения новинок, популярных и другое( для виджетов)
    @staticmethod
    # Ф-ия получения новинок
    def get_new():
        return Software.objects.filter(date_of_delete=None, visibility=True).order_by('date_joined')[:6]


    # Ф-ия получения списка ПОПУЛЯРНЫХ ПО
    @staticmethod
    def get_popular():
        software_list = []
        soft_raw = Software.objects.raw('''SELECT distinct * from new_db.software_software AS softwares
        where softwares.id in 
        ((select software_id
        from new_db.order_order
        where software_id is not null
        group by software_id
        order by count(*) DESC)
        UNION
        (select software_id
        from new_db.software_download
        where software_id is not null
        group by software_id
        order by count(*) DESC)
        )
        limit 15 ''' )

        for p in soft_raw:
            software_list.append(p)
        
        return software_list



class Addition(models.Model):
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО')
    name = models.CharField('Название', max_length = 50, null=True)
    kind = models.BooleanField('Тип (true - картинка)', default=True)
    size = models.BooleanField('Тип (true - большая картинка)', default=True)
    photo = models.ImageField('Фото', upload_to="soft/")
    is_main = models.BooleanField('Тип (true - главная)', default=False)
    # date_of_create = models.DateField('Дата создания', auto_now_add=True, blank=True)      
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'


# Область применения, вид
class Classification(models.Model):
    name = models.CharField('Название', max_length = 50)
    visibility = models.BooleanField('Видимость на сайте', default=True)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Классификация'
        verbose_name_plural = 'Классификации'

    # Ф-ия получения списка значений классификации
    def get_values(self):
        return Classification_Value.objects.filter(classification__id = self.id, visibility=True).order_by('value')


# Область применения: грузоперевозки, ...
class Classification_Value(models.Model):
    classification = models.ForeignKey(Classification, on_delete = models.PROTECT, verbose_name='Классификация')
    value = models.CharField('Значение классификации', max_length = 200)
    softwares = models.ManyToManyField(Software)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Классификация_значение'
        verbose_name_plural = 'Классификация_значение'


# Теги ПО и статей 
class Tag(models.Model):
    name = models.CharField('Название', max_length = 50, null=True)
    description = models.TextField('Описание', null=True, blank=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True)
    softwares = models.ManyToManyField(Software, null=True, blank=True)
    articles = models.ManyToManyField(Article, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


# Избранные - ПО №2: (клиент)
class Favourite(models.Model):
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Клиент')
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    @staticmethod
    # Ф-ия получения списка избранных в Favourite таблице по клиенту
    def get_favourites_by_user(client):
        return Favourite.objects.filter(client=client.id)



# Избранные - ПО №2: (клиент)
class Download(models.Model):
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Клиент')
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Загрузка'
        verbose_name_plural = 'Загрузки'


