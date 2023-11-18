from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PlasticModel
from .serializers import PlasticSerializer
from rest_framework.parsers import JSONParser
import pickle
import numpy as np
#from .thinkspeak import *
# Create your views here.

@api_view(['GET', 'POST'])
def plastic(request):
    if request.method=='GET':
        pl=PlasticModel.objects.all()
        pl_s=PlasticSerializer(pl, many=True)
        return Response(pl_s.data)
    if request.method=='POST':
        pl2=JSONParser().parse(request)
        #Run AI Model; Give Data as type of plastic
        svm=pickle.load(open('api/model2.sav','rb'))
        x_pred=np.array([[pl2['reflectance'], pl2['distance']]])
        val=svm.predict(x_pred)
        d={0:'PP',1:'HDPE',2:'PET'}
        type_of_plastic=d[val[0]]
        print(type_of_plastic)
        p=PlasticModel.objects.get(type=type_of_plastic)
        p.count+=1
        p.save()
        return Response({
            'type':type_of_plastic
        })
    


