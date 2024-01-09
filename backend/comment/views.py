from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer

class CommentView(APIView):

    def get(self, request, pk):
        comments = Comment.objects.filter(product_id=pk)
        print(comments)
        if comments:
            serializer = CommentSerializer(comments, many=True)
            return Response({'comments': serializer.data})
        return Response({'comments': 'null'})

    def post(self, request, pk):
        comments = Comment.objects.filter(product_id=pk, user_id=request.data.get('user_id'))
        if not comments:
            comment = Comment.objects.create(product_id=pk, user_id=request.data.get('user_id'),
                                             body=request.data.get('body'))
            comment.save()
            comments = Comment.objects.filter(product_id=pk)
            serializer = CommentSerializer(comments, many=True)
            return Response({'comments': serializer.data}, status=200)
        return Response({'comments': 'exist'}, status=205)