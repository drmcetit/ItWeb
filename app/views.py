from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import status
from rest_framework import views

from .models import carouselModel,AssosiationMembersModel,PlacementModel
from .serializers import carouselSerializer,AssositationSerializer,PlacmentSerializer

# Create your views here.

class HomeView(views.APIView):
    permission_classes=[]
    authentication_classes=[]

    def get(self,request):

        #carousel display
        qs=carouselModel.objects.exclude(Display=False).order_by('-Date')[:5]
        carousel=carouselSerializer(qs,many=True).data

        return JsonResponse({"carousel":carousel},status=status.HTTP_200_OK)

HomeViewClass=HomeView.as_view()

class AssosationView(generics.ListAPIView):

    queryset=AssosiationMembersModel.objects.all()
    serializer_class=AssositationSerializer
    permission_classes=[]
    authentication_classes=[]

    def get(self, request, *args, **kwargs):
        qs=AssosiationMembersModel.objects.all()
        members=AssositationSerializer(qs,many=True)
        # return super().get(request, *args, **kwargs)

        return JsonResponse({"Members":members.data},status=status.HTTP_200_OK)

AssosationViewClass=AssosationView.as_view()

class PlacmentView(generics.ListAPIView):

    queryset=PlacementModel.objects.all()
    serializer_class=PlacmentSerializer
    permission_classes=[]
    authentication_classes=[]

    def get(self, request, *args, **kwargs):

        #Top3
        qs=PlacementModel.objects.filter(Placed=True).order_by("LPA")
        if(qs.count()<=3):
            return JsonResponse({"Count":"Less than 3"},status=status.HTTP_204_NO_CONTENT)
        serializer=PlacmentSerializer(qs,many=True).data

        #Batch List
        batchqs=PlacementModel.objects.values_list('Batch').distinct()
        batchList=[]
        for i in batchqs:
            batchList.append(i[0])
        # return super().get(request, *args, **kwargs)

        return JsonResponse({"top1":serializer[0],"top2":serializer[1],"top3":serializer[2],"batchList":batchList},status=status.HTTP_200_OK)
    
PlacmentViewClass=PlacmentView.as_view()

class PlacmentBatchView(generics.ListAPIView):

    queryset=PlacementModel.objects.all()
    serializer_class=PlacmentSerializer
    permission_classes=[]
    authentication_classes=[]

    def get(self, request,Batch=None, *args, **kwargs):

        qs=PlacementModel.objects.filter(Batch=Batch).order_by("-LPA")
        if(qs.count()<=3):
            return JsonResponse({"Count":"Less than 3"},status=status.HTTP_204_NO_CONTENT)
        
        serializer=PlacmentSerializer(qs,many=True).data
        return JsonResponse({"top3":serializer[:3],"others":serializer[3:]},status=status.HTTP_200_OK)
        #return super().get(request, *args, **kwargs)

PlacmentBatchViewClass=PlacmentBatchView.as_view()