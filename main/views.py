from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework  import status
from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework .viewsets import ModelViewSet

@api_view(['GET'])
def category(request):
    category_id=request.GET.get('category_id')
    if category_id:
        category=Category.objects.filter(id=category_id)
        if category.exists():
            category=category[0]
            serializer=CategorySerializer(category)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message':'No such as category'},status=status.HTTP_404_NOT_FOUND)
    categories=Category.objects.all()
    serializer=CategorySerializer(categories,many=True)
    return Response(serializer.data,status=200)




@api_view(['POST','PUT','DELETE'])
def category_ped(request):
    category_id=request.POST.get('category_id')
    name=request.POST.get('name')
    is_active=request.POST.get('is_active')
    if request.method=='PUT':
        category=Category.objects.filter(id=category_id)
        if category.exists():
            category=category[0]
            if name and is_active is not None:
                category.name=name
                category.is_active=is_active
                category.save()
                serializer=CategorySerializer(category)
                data={
                    'message':'category has successfully updated',
                    'data':serializer.data
                }
                return Response(data,status=status.HTTP_201_CREATED)
            else:
                return Response('message : You should fill all the field of the category', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'No such as category'},status=404)
        

    if request.method=='POST':
        category=Category.objects.filter(name=name)
        if not category.exists():
            category=Category.objects.create(
                name=name,
                is_active=is_active
            )
            serializer=CategorySerializer(category)
            data={
                    'message':'category has successfully created',
                    'data':serializer.data
                }
            return Response(data=data,status=201)
        return Response('message : category has already exsists',status=400)
    

    if request.method=='DELETE':
        category=Category.objects.filter(id=category_id).first()
        if category:
            category.delete()
            return Response('message : category has deleted')


        
@api_view(['GET'])
def banner(request):
    banner_id=request.GET.get('banner_id')
    if banner_id:
        banner=Banner.objects.filter(id=banner_id).first()
        if banner:
            serializer=BannerSerializer(banner)
            return Response(serializer.data,status=200)
    banners=Banner.objects.all()
    serializer=BannerSerializer(banners,many=True)
    return Response(serializer.data,status=200)




@api_view(['POST','PUT','DELETE'])
def banner_ped(request):
    banner_id=request.POST.get('banner_id')
    title=request.POST.get('title')
    description=request.POST.get('description')
    image=request.FILES.get('image')
    is_active=request.POST.get('is_active')
    if request.method=='PUT':
        banner=Banner.objects.filter(id=banner_id).first()
        if banner:
            banner.title=title
            banner.description=description
            banner.image=image
            banner.is_active=is_active
            banner.save()
                
            serializer=BannerSerializer(banner)
            data={
                'message':'banner has successfully updated',
                'data':serializer.data
            }

            return Response(data,status=201)
        else:
            return Response('message : no such as banner')
    if request.method=='POST':
        if title and description and image and is_active is not None:
            banner=Banner.objects.create(
                title=title,
                description=description,
                image=image,
                is_active=is_active
            )        

            serializer=BannerSerializer(banner)
            data={
                'message':'banner has successfully created',
                'data':serializer.data
            }
            return Response(data=data,status=201)
    if request.method=='DELETE':
        banner=Banner.objects.filter(id=banner_id)
        if banner.exists():
            banner[0].delete()
            return Response('message : banner has deleted')
        







class Bookview(ModelViewSet):
    serializer_class=BookSerailizer
    queryset=Book.objects.all()
    
    @action(detail=False, methods=['POST'])
    def search(self, request, pk=None):
        category_id = request.data.get('category_id')
        name = request.data.get('name')
        if category_id is not None and name is not None:
            books = Book.objects.filter(category_id=category_id, name__icontains=name)
        elif category_id is not None:
            books = Book.objects.filter(category_id=category_id)
        elif name is not None:
            books = Book.objects.filter(name__icontains=name)
        else:
            books = []
        serializer=BookSerailizer(books,many=True).data
        return Response(serializer,status=200)
        








class Courseview(ModelViewSet):
    serializer_class=CoursePlaylistSerializer
    queryset=Course.objects.all()

    @action(detail=False, methods=['POST'])
    def search(self, request, pk=None):
        category_id = request.data.get('category_id')
        title = request.data.get('title')
        if category_id is not None and title is not None:
            courses = Course.objects.filter(category_id=category_id, title__icontains=title)
        elif category_id is not None:
            courses = Course.objects.filter(category_id=category_id)
        elif title is not None:
            courses = Course.objects.filter(title__icontains=title)
        else:
            courses = []
        serializer=CourseSerializer(courses,many=True).data
        return Response(serializer,status=200)
        
           





class CoursePlaylistView(ModelViewSet):
    serializer_class=CoursePlaylistSerializer
    queryset=Courseplaylist.objects.all()    





class ReviewView(ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()




class MentorView(ModelViewSet):
    serializer_class=MentorSerializer
    queryset=Mentor.objects.all()




class PaymentView(ModelViewSet):
    serializer_class=PaymentSerailizer
    queryset=Payment.objects.all()



class CartView(ModelViewSet):
    serializer_class=CartSerializer
    queryset=Cart.objects.all()