from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.formats.format import prod_res
from api.v1.serializer import CrudSerializer
from regis.models import Product


class CrudView(GenericAPIView):
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,
    serializer_class = CrudSerializer

    def get(self, requests,  pk=None, *args, **kwargs):
        if pk:
            products = Product.objects.get(pk=pk).first()
            if not products:
                return Response({
                    "Error": "Product topilmadi"
                })
            return Response({"Natija": prod_res(products)})

        prod = Product.objects.all()
        l =[]
        for i in prod:
            l.append(prod_res(i))
        return Response({
            "items": l
        })

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()

        return Response({
            "result": prod_res(root)
        })

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = Product.objects.filter(pk=pk).first()

        if not root:
            return Response({
                "Error": "Product topilmadi"
            })

        serializer = self.get_serializer(data=data, instance=root)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response({
            "result": prod_res(root)
        })

    def delete(self, requests, pk, *args, **kwargs):
        root = Product.objects.filter(pk=pk).first()
        root.delete()
        return Response({
            "result": f"{pk} Product deleted"
        })
