from django.http import HttpResponse
# from rest_framework.paginations import (
    
# )
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
)
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
    pagination_class = 2
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
    lookup_field='pk'
    lookup_url_kwarg = 'pk_field'