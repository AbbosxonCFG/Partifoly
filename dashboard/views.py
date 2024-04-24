from django.shortcuts import render,redirect
from main.models import *
from account.models import *


#!-------------------------------------------------CATEGORY CRUD-------------------------------------------------------TE

def category(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'base.html',context)




def category_add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        category=Category.objects.create(
            name=name
        )
        return redirect('category')
    return render(request,'category_add.html')



def category_delete(request,pk):
    category=Category.objects.get(id=pk)
    category.delete()
    return redirect('category')


#!---------------------------------------------Banner-----------------------------------------------------------


def banner(request):
    banner=Banner.objects.last()
    contex={
        'banner':banner
    }
    return render(request,'banner.html',contex)


def banner_add(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        is_active=request.POST.get('is_active')

        banner=Banner.objects.create(
            title=title,
            description=description,
            image=image,
            is_active=is_active,
        )
        return redirect('banner')
    return render(request,'banner_add.html')


def banner_update(request,pk):
    banner=Banner.objects.get(id=pk)
    title=request.POST.get('title')
    description=request.POST.get('description')
    image=request.FILES.get('image')
    is_active=request.POST.get('is_active')
    if request.method=='POST':
        banner.title=title
        banner.description=description
        banner.image=image
        banner.is_active=is_active
        banner.save()
        return redirect('banner')
    return render(request,'banner.update.html')


def banner_delete(request,pk):
    banner=Banner.objects.get(id=pk)
    banner.delete()
    return redirect('banner')


#!--------------------------------------------------------Book-----------------------------------------------------

def book(request):
    book=Book.objects.all()
    contex={
        "book":book
    }
    return render(request,'book.html',contex)

def book_add(request):
    if request.method=='POST':
        name=request.POST.get("name")
        price=request.POST.get('price')
        image=request.FILES.get('image')
        category_id=request.POST.get('category_id')
        raiting=request.POST.get('raiting')

        book=Book.objects.create(
            name=name,
            price=price,
            image=image,
            category_id=category_id,
            raiting=raiting
        )
        return redirect('book')
    return render(request,'book_add.html')

def book_update(request,pk):
    book=Book.objects.get(id=pk)
    name=request.POST.get("name")
    price=request.POST.get('price')
    image=request.FILES.get('image')
    category_id=request.POST.get('category_id')
    raiting=request.POST.get('raiting')
    if request.method=='POST':
        book.name=name
        book.price=price
        book.image=image
        book.category_id=category_id
        book.raiting=raiting
        book.save()
        return redirect('book')
    return render(request,'book_update.html')


def book_delete(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return redirect('book')

#!------------------------------------------------------Course------------------------------------------------------


def course(request):
    course=Course.objects.all()
    contex={
        'course':course
    }
    return render(request,'course.html',contex)

def course_detail(request,pk):
    course=Course.objects.get(id=pk)
    contex={
        'course':course
    }
    return render(request,'course_detail.html',contex)


def course_add(request):
    if request.method=='POST':
        title=request.POST.get("title")
        description=request.POST.get("description")
        image=request.FILES.get(" image")
        category_id=request.POST.get("category_id ")
        price=request.POST.get(" price")
        is_active=request.POST.get("is_active ")
        raiting=request.POST.get("raiting ")
        durations=request.POST.get(" durations")
        lessons=request.POST.get("lessons ")
        certificate=request.POST.get(" certificate")
        language=request.POST.get(" language")

        course=Course.objects.create(
            title=title,
            description=description,
            image=image,
            category_id=category_id,
            price=price,
            is_active=is_active,
            raiting=raiting,
            durations=durations,
            lessons=lessons,
            certificate=certificate,
            language=language
        )
        return redirect('course')
    return render (request,'course_add.html')


def course_update(request,pk):
    course=Course.objects.get(id=pk)
    title=request.POST.get("title")
    description=request.POST.get("description")
    image=request.FILES.get(" image")
    category_id=request.POST.get("category_id ")
    price=request.POST.get(" price")
    is_active=request.POST.get("is_active ")
    raiting=request.POST.get("raiting ")
    durations=request.POST.get(" durations")
    lessons=request.POST.get("lessons ")
    certificate=request.POST.get(" certificate")
    language=request.POST.get(" language")

    if request.method=='POST':
        course.title=title
        course.description=description
        course.image=image
        course.category_id=category_id
        course.price=price
        course.is_active=is_active
        course.raiting=raiting
        course.durations=durations
        course.lessons=lessons
        course.certificate=certificate
        course.language=language

        course.save()
        return redirect('course')
    return render(request,'course_update.html')


def course_delete(request,pk):
    course=Course.objects.get(id=pk)
    course.delete()
    return redirect('course')

#!----------------------------------------Courseplaylist------------------------------------------------------




def courseplaylist(request):
    courseplaylist=Courseplaylist.objects.all()
    contex={
        'courseplaylist':courseplaylist
    }
    return render(request,'courseplaylist.html',contex)


def courseplaylist_detail(request,pk):
    courseplaylist=Courseplaylist.objects.get(id=pk)
    contex={
        'courseplaylist':courseplaylist
    }
    return render(request,'courseplaylist_detail.html',contex)


def courseplaylist_add(request):
    if request.method=='POST':
        course_id=request.POST.get("course_id")
        title=request.POST.get(" title ")
        type=request.POST.get(" type")

        courseplaylist=Courseplaylist.objects.create(
            course_id=course_id,
            title=title,
            type=type
        )

        return redirect('courseplaylist')
    return render(request,'courseplaylist_add')

def courseplaylist_update(request,pk):
    courseplaylist=Courseplaylist.objects.get(id=pk)
    course_id=request.POST.get("course_id")
    title=request.POST.get(" title ")
    type=request.POST.get(" type")
    if request.method=='POST':
        courseplaylist.course_id=course_id
        courseplaylist.title=title
        courseplaylist.type=type
        courseplaylist.save()
        return redirect('courseplaylist')
    return render(request,'courselaylist_update.html')


def courseplaylist_delete(request,pk):
    courseplaylist=Courseplaylist.objects.get(id=pk)
    courseplaylist.delete()
    return redirect('courseplaylist')

#!----------------------------------------------------Review----------------------------------------------------


def review(request):
    review=Review.objects.all()
    contex={
        'review':review
    }
    return render(request,'review.html',contex)


def review_add(request):
    if request.method=='POST':

        feedback=request.POST.get('feedback')
        user_id=request.POST.get('user_id')
        book_id=request.POST.get('book_id')

        review=Review.objects.create(
            feedback=feedback,
            user_id=user_id,
            book_id=book_id
        )
        return redirect('review')
    return render (request,'review_add.html')

def review_update(request,pk):
    review=Review.objects.get(id=pk)
    feedback=request.POST.get('feedback')
    user_id=request.POST.get('user_id')
    book_id=request.POST.get('book_id')

    if request.method=='POST':
        review.feedback=feedback
        review.user_id=user_id
        review.book_id=book_id
        review.save()
        return redirect('review')
    return render(request,'review_update.html')

def review_delete(request,pk):
    review=Review.objects.get(id=pk)
    review.delete()
    return redirect('review')

#!-------------------------------------------------------Mentor------------------------------------------------------------------

def mentor(request):
    mentor=Mentor.objects.all()
    contex={
        'mentor':mentor
    }

    return render(request,'mentor.html',contex)

def mentor_detail(request,pk):
    mentor=Mentor.objects.get(id=pk)
    contex={
        "mentor":mentor

    }
    return render(request,'mentor_detail.html',contex)


def mentor_add(request):
    if request.method=='POST':
        user_id=request.POST.get("user_id ")
        image=request.FILES.get("image ")
        description=request.POST.get("description ")
        category_id=request.POST.get("category_id ")

        mentor=Mentor.objects.create(
            user_id=user_id,
            image=image,
            description=description,
            category_id=category_id
        )

        return redirect('mentor')
    return render(request,'mentor_add')


def mentor_update(request,pk):
    mentor=Mentor.objects.get(id=pk)
    user_id=request.POST.get("user_id ")
    image=request.FILES.get("image ")
    description=request.POST.get("description ")
    category_id=request.POST.get("category_id ")       

    if request.method=='POST':
        mentor.user_id=user_id
        mentor.image=image
        mentor.description=description
        mentor.category_id=category_id
        mentor.save()

        return redirect('mentor')
    return render(request,'mentor_update')


def mentor_delete(request,pk):
    mentor=Mentor.objects.get(id=pk)
    mentor.delete()
    return redirect('mentor')




#!-----------------------------------------------------Payment_________________________________________________________________________

def payment(request):
    payment=Payment.objects.all()
    contex={
        'payment':payment
    }
    return render(request,'payment.html',contex)


def payment_detail(request,pk):
    payment=Payment.objects.get(id=pk)
    return render(request,'payment_detail.html',{'payment':payment})

def payment_add(request):
    title=request.POST.get('title')
    type=request.POST.get('type')
    description=request.POST.get('description')
    price=request.POST.get('price')

    if request.method=='POST':
        payment=Payment.objects.create(
            title=title,
            description=description,
            type=type,
            price=price
        )
        return redirect('payment')
    return render(request,'payment_add')



def payment_update(request,pk):
    payment=Payment.objects.get(id=pk)
    title=request.POST.get('title')
    type=request.POST.get('type')
    description=request.POST.get('description')
    price=request.POST.get('price')

    if request.method=='POST':
        payment.title=title
        payment.type=type
        payment.description=description
        payment.price=price
        payment.save()
        
        return redirect('payment')
    return render(request,'payment_update.html')


def payment_delete(request,pk):

    payment=Payment.objects.get(id=pk)
    payment.delete()
    return redirect('payment')


#!---------------------------------------------------------Cart_________________________________________________________________________

def cart(request):
     cart=Cart.objects.all()
     return render(request,'cart.html',{'cart':cart})


def cart_delete(request,pk):
    cart=Cart.objects.get(id=pk)
    cart.delete()
    return redirect('cart')


