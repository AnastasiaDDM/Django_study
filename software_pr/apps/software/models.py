from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from PIL import Image
from article.models import Article
import dbl


class Software(models.Model):
    name = models.CharField('Наименование ПО', max_length = 200)
    price = models.FloatField('Цена', blank=True, validators=[MinValueValidator(0)])
    is_free = models.BooleanField('Бесплатно/Платно', default=True, db_index=True)
    description = models.TextField('Описание')
    description_medium = models.TextField('Среднее описание', max_length = 400)
    description_small = models.TextField('Короткое описание', max_length = 50)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    modification = models.BooleanField('Возможность доработки', default=True)
    size = models.FloatField('Размер', blank=True, validators=[MinValueValidator(0)], null=True)
    date_of_delete = models.CharField('Дата удаления', blank=True, max_length = 20, null=True, db_index=True)
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


    # Ф-ия получения списка тегов 
    def get_tags(self):

        # Получаем список тегов данного ПО
        software_tag = Tag.objects.filter(softwares__id=self.id, visibility=True, date_of_delete=None)
        return software_tag


    # Ф-ия получения списка классификаций
    def get_classifications(self):

        # Хэш классификаций ПО
        classif = {}

        # Получение списка всех классификаций ПО из таблицы Software_Classification_Value
        software_classifications = Classification_Value.objects.filter(softwares__id = self.id)

        # Переменная для составления строки классификаций ПО (Грузоперевозки, перевозки)
        str_clas =""

        # Дальнейшие действия нужны для составления словаря классификаций данного ПО
        for clas_val in software_classifications:

            # Получение одной записи из Classification_Value
            # clas_val = Classification_Value.objects.get(id = clas.classification_value.id)

            if clas_val:
                
                # Получение одной записи из Classification для получения названия классификации
                clas = Classification.objects.get(id = clas_val.classification.id)

                if str(clas) == "Область применения" :

                    # Получаем значение ключа, если есть:
                    if classif.get("area"):

                        # Составляем строку значений классификации
                        str_clas = str(classif.get("area")) + ", " + str(clas_val)

                        # Добавляем ключ и значение в словарь
                        classif["area"] = str_clas

                    else:

                        # Добавляем ключ и значение в словарь
                        classif["area"] = clas_val


                elif str(clas) == "Вид" :

                    # Получаем значение ключа, если есть:
                    if classif.get("type"):

                        # Составляем строку значений классификации
                        str_clas = str(classif.get("type")) + ", " + str(clas_val)

                        # Добавляем ключ и значение в словарь
                        classif["type"] = str_clas

                    else:

                        # Добавляем ключ и значение в словарь
                        classif["type"] = clas_val


                elif str(clas) == "Тип использования" :

                    # Добавляем ключ и значение в словарь
                    classif["type_of_use"] = clas_val


                elif str(clas) == "Ограничение доступа" :

                    # Добавляем ключ и значение в словарь
                    classif["access"] = clas_val



                elif str(clas) == "Дополнительные установки" :

                    # Добавляем ключ и значение в словарь
                    classif["extra_install"] = clas_val


                elif str(clas) == "Установка" :

                    # Добавляем ключ и значение в словарь
                    classif["install"] = clas_val

        return classif   





     # Ф-ия получения списка областей применения
    def get_area(self):

        # Хэш классификаций ПО
        dbl.log(str(self))
        areas = []


        # Получение списка всех классификаций ПО из таблицы Software_Classification_Value
        software_classifications = Classification_Value.objects.filter(softwares__id = self.id)
        # software_classifications = Software_Classification_Value.objects.filter(software__id = self.id)


        

        # # Переменная для составления строки классификаций ПО (Грузоперевозки, перевозки)
        # str_clas =""

        # Дальнейшие действия нужны для составления словаря классификаций данного ПО
        for clas_val in software_classifications:


            # Получение одной записи из Classification_Value
            # clas_val = Classification_Value.objects.get(id = clas.classification_value.id)



            # Получение одной записи из Classification для получения названия классификации
            clas = Classification.objects.get(id = clas_val.classification.id)


            # clas = clas_val.filter(classification__name ="Область применения")


            if clas.name == "Область применения":


                
                areas.append(str(clas_val))

        # dbl.log(str(areas))

        return areas   


    

     # Ф-ия получения списка областей применения
    def get_type(self):

        # Хэш классификаций ПО

        areas = []

        # Получение списка всех классификаций ПО из таблицы Software_Classification_Value
        software_classifications = Classification_Value.objects.filter(softwares__id = self.id)


        

        # # Переменная для составления строки классификаций ПО (Грузоперевозки, перевозки)
        # str_clas =""

        # Дальнейшие действия нужны для составления словаря классификаций данного ПО
        for clas_val in software_classifications:


            # Получение одной записи из Classification_Value
            # clas_val = Classification_Value.objects.get(id = clas.value.id)

            # dbl.log("0000   "+str(clas_val))


            # Получение одной записи из Classification для получения названия классификации
            clas = Classification.objects.get(id = clas_val.classification.id)


            # clas = clas_val.filter(classification__name ="Область применения")


            if clas.name == "Вид":

                areas.append(str(clas_val))

        return areas   


class Addition(models.Model):
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО')
    name = models.CharField('Название', max_length = 50, null=True)
    kind = models.BooleanField('Тип (true - картинка)', default=True)
    size = models.BooleanField('Тип (true - большая картинка)', default=True)
    photo = models.ImageField('Фото', upload_to="soft/")
    is_main = models.BooleanField('Тип (true - главная)', default=False)
    # date_of_create = models.DateField('Дата создания', auto_now_add=True, blank=True)      
    date_of_delete = models.DateField('Дата удаления', blank=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'


# Область применения, вид
class Classification(models.Model):
    name = models.CharField('Название', max_length = 50)
    visibility = models.BooleanField('Видимость на сайте', default=True)
    date_of_delete = models.DateField('Дата удаления', blank=True)

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
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    softwares = models.ManyToManyField(Software)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Классификация_значение'
        verbose_name_plural = 'Классификация_значение'




# ПО №2: (Область применения: грузоперевозки)
# class Software_Classification_Value(models.Model):
#     software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО')
#     classification_value = models.ForeignKey(Classification_Value, on_delete = models.PROTECT, verbose_name='Классификация_значение')

#     # def __str__(self):
#     #     return self.value

#     class Meta:
#         verbose_name = 'Приложение_классификация'
#         verbose_name_plural = 'Приложения_классификация'



# Теги ПО и статей 
class Tag(models.Model):
    name = models.CharField('Название', max_length = 50, null=True)
    description = models.TextField('Описание', blank=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    date_of_delete = models.DateField('Дата удаления', blank=True)
    softwares = models.ManyToManyField(Software)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


# # ПО №2: (тег)
# class Software_Tag(models.Model):
#     software = models.ForeignKey(Software, on_delete = models.CASCADE, verbose_name='ПО')
#     tag = models.ForeignKey(Tag, on_delete = models.CASCADE, verbose_name='Тег')

#     # def __str__(self):
#     #     return self.tag

#     class Meta:
#         verbose_name = 'Приложение_тег'
#         verbose_name_plural = 'Приложения_теги'