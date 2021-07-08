from django.http import HttpResponse

# Mixin classes can be imported from rest_framework.mixins
# Mixin classes provide action methods rather than handler methods such a .get(), .post()
from rest_framework.mixins import (
    ListModelMixin, # .list(request, *args, **kwargs), 200 OK
    
    CreateModelMixin, # .create(request, *args, **kwargs), 201 Created, 400 Bad Request (if provided data is invalid)
    
    RetrieveModelMixin, # .retrieve(request, *args, **kwargs), 200 OK, 404 Not Fount (Otherwise it will return )
    
    UpdateModelMixin, # .update(request, *args, **kwargs), 200 OK. 400 Bad Request (if provided data is invalid)
                      # .partial_update(request, *args, **kwargs), this is similar with update method , except that all 
                      # fields for the update will be optional. This allows support for HTTP PUTCH request.
    
    DestroyModelMixin, # .destroy(request, *args, **kwargs), 204 No Content, 404 Not Found (Otherwise)
)

# Generic View Classes can be imported from rest_framework.generics
from rest_framework.generics import (
    CreateAPIView, # used for create-only endpoints. post() method handler, extends: GenericAPIView, CreateModelMixin
    
    ListAPIView, # used for read-only endpoints to represent a collection of model instances, 
                 # get() method handler, extends: GenericAPIView, ListModelMixin

    RetrieveAPIView, # used for read-only endpoints to represent a single model instance
                     # get() method handler, GenericAPIView, RetrieveModelMixin
    
    DestroyAPIView, # used for delete-only endpoints for a single model instance
                    # delete() method handler, extends: GenericAPIView, DestroyModelMixin

    UpdateAPIView, # used for update-only endpoints for a single model instance
                   # put() and patch() method handler, extends: GenericAPIView, UpdateModelMixin
    
    ListCreateAPIView, # used for read-write endpoints to represent a collection of model instances
                       # get(), post() method handlers, extends: GenericAPIView, ListModelMixin, CreateModelMixin

    RetrieveUpdateAPIView, # used read-update endpoint to represent a single model instance
                           # get(), put() and patch() handler methods, extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin 

    RetrieveDestroyAPIView, # used for read-delete endpoints to represent a single model instance
                            # get(), delete() handler methods, extends: GenericAPIView, RetrieveModelInstance, DestroyModelInstance

    RetrieveUpdateDestroyAPIView, # used for read-write-delete endpoints to represent a single model instance
                                  # get(), put(), patch() and delete() method handlers, extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

)

# from rest_framework.paginations import (
    
# )

from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser,
)
from portfolio.models import Portfolio
from .serializers import (
    PortfolioSerializer, 
)

class ListPortfolioApiView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated,]

    # def list(self, request):
    #     # Note the use of 'self.get_queryset()' instead of self.queryset
    #     queryset = self.get_queryset()
    #     serializer = PortfolioSerializer(queryset, many=True)
    #     return HttpResponse(serializer.data)


class DetailPortfolioApiView(RetrieveAPIView):
    queryset=Portfolio.objects.all()
    serializer_class=PortfolioSerializer
    permission_classes=[IsAuthenticated,]
    lookup_field='pk' # define lookup field name of object of model instances, default value is pk
    lookup_url_kwarg = 'pk_field' # define lookup name in urlConfigure, if not set, default name is lookup name 