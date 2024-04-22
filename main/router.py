from rest_framework.routers import DefaultRouter
from .views import *



router=DefaultRouter()
router.register(r'book',Bookview,)
router.register(r'course',Courseview)
router.register(r'review',ReviewView)
router.register(r'mentor',MentorView)
router.register(r'payment',PaymentView)
router.register(r'cart',CartView)
router.register(r'courseplaylist',CoursePlaylistView)


