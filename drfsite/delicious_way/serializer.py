from rest_framework import serializers
from .models import DeliciousWay
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class DeliciousWayModel:     # (для примера) класс, который будет имитировать класс модели фреймворка Django
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class DeliciousWaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliciousWay
        fields = ("__all__")


# здесь  создаем объект-модель класса DeliciousWayModel, затем, он сериализуется путем создания объекта
# класса DeliciousWaySerializer, на вход которого мы передаем объект model. Далее, объект сериализованных данных
# преобразуется в обычную JSON-строку и результат выводится в консоль.
#
# def encode():
#     model = DeliciousWayModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = DeliciousWaySerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#  обратный процесс преобразование из JSON-строки в объект:
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = DeliciousWaySerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
