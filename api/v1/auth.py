from django.contrib.sites import requests
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from regis.models import User


class RegisView(GenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data

        nott = ["first_name", "last_name", "password", "phone"]
        s = ' '.join(x for x in nott if x not in data)

        # for i in nott:
        #     if i not in data:
        #         s += f" {i} "
        #
        if s.strip():
            return Response({
                "Error": f"Datada {s} to`liq emas"
            })

        if len(str(data['phone'])) != 12:
            return Response({
                "Error": "tel raqam + ni olib tashalaganda 12 ta bo`lishi kerak"
            })

        if not str(data['phone']).isdigit():
            return Response({
                "Error": "telefon raqamingiz to`liq sonlardan iborat bo`lishi kerak"
            })
        if len(str(data['password'])) < 6:
            return Response({
                "Error": "password ni murakkabroq qilib kiriting "
            })

        user = User.objects.create_user(
            phone=data['phone'],
            password=data.get('password', ''),
            first_name=data.get('first_name', ''),
            last_name=data.get('password', ''),
        )

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key
        })


class LoginView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        if data is None:
            return Response({
                "Error": "data to`ldirilmagan"
            })

        nott = 'phone' if 'phone' not in data else 'password' if 'password' not in data else None

        if nott:
            return Response({
                "Error": f"{nott} to`ldirilmagan"
            })

        user = User.objects.filter(phone=data["phone"]).first()

        if not user:
            return Response({
                "Error": "bunday foydalanuvchi topilmadi"
            })

        if not user.check_password(data["password"]):
            return Response({
                "Error": "password xato"
            })

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
            "user": user.format()
        })




