from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import mixins, generics, permissions


class NotificationPost(mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotificationEmail(mixins.ListModelMixin,
                        generics.GenericAPIView):
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        mylist = self.list(request, *args, **kwargs)
        self.get_queryset().update(viewed=True)
        return mylist

    def get_queryset(self):
        return Notification.objects.filter(email=self.kwargs['email'], viewed=False).order_by('-pk')


class NotificationDetail(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NotificationHistory(mixins.ListModelMixin,
                          generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Notification.objects.filter(email=self.kwargs['email']).order_by('-pk')
