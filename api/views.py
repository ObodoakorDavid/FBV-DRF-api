from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ChatSerializer
from .models import Chat

# Create your views here.

@api_view(['GET'])
def ChatList(request):
    ChatList = Chat.objects.all()
    serializer = ChatSerializer(ChatList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ChatDetail(request, pk):
    ChatDetail = Chat.objects.get(id=pk)
    print(ChatDetail)
    serializer = ChatSerializer(ChatDetail, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ChatCreate(request):
    if request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('/api')
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def ChatDelete(request, pk):
    ChatDelete = Chat.objects.get(id=pk)
    serializer = ChatSerializer(ChatDelete, many=False)
    if request.method == 'DELETE':
        ChatDelete.delete()
        return Response({"msg": "Message Deleted"})
    return Response(serializer.data)

@api_view(['GET','PUT'])
def ChatUpdate(request, pk):
    ChatDelete = Chat.objects.get(id=pk)
    serializer = ChatSerializer(ChatDelete, many=False)
    if request.method == 'PUT':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.data)


