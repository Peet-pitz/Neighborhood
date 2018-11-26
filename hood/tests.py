# from django.test import TestCase
# from .models import Hood,User, Business

# # Create your tests here.

# class HoodTestClass(TestCase):
#     #Set up method
#     def setUp(self):
#         self.new_hood =Hood(name="ghost",location="Nairobi",count = "2")

#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_hood,Hood))

#     #Testing Save Method
#     def test_save_method(self):
#         self.new_hood.save_hood()
#         hood=Hood.objects.all()
#         self.assertTrue(len(hood)>0)

#     def test_delete_method(self):
#         self.new_hood.save_hood()
#         self.new_hood.delete_hood()

#     def test_update_hood(self):
#         self.new_hood.save_hood()
#         self.new_hood = Hood.objects.get(id = 3 )
#         self.new_hood.update_hood('Nairobi')
#         self.updated_hood = Hood.objects.get(id = 3)
#         self.assertEqual(self.updated_hood.location,"Nairobi")

#     def test_update_hood(self):
#         self.new_hood.save_hood()
#         self.new_hood = Hood.objects.get(id = 3 )
#         self.new_hood.update_hood('2')
#         self.updated_hood = Hood.objects.get(id = 3)
#         self.assertEqual(self.updated_hood.count,2)

# class UserTestClass(TestCase):
#     #Set up method
#     def setUp(self):
#         self.new_userstatus =UserStatus(user_image="ghost.jpeg",user_email = "njoroge.pitz@gmail.com@gmail.com")

#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_userstatus,UserStatus))

#     #Testing Save Method
#     def test_save_method(self):
#         self.new_userstatus.save_userstatus()
#         userstatus = UserStatus.objects.all()
#         self.assertTrue(len(userstatus)>0)

#     def test_delete_method(self):
#         self.new_userstatus.save_userstatus()
#         self.new_userstatus.delete_userstatus()

# class BusinessTestClass(TestCase):
#     #Set up method
#     def setUp(self):
#         self.new_business =Business(business_name="shopkeeper",business_email = "njoroge.pitz@gmail.com@gmail.com")

#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_business,Business))

#     #Testing Save Method
#     def test_save_method(self):
#         self.new_business.save_business()
#         business = Business.objects.all()
#         self.assertTrue(len(business)>0)

#     def test_delete_method(self):
#         self.new_business.save_business()
#         self.new_business.delete_business()

#     def test_update_business(self):
#         self.new_business.save_business()
#         self.new_business= Business.objects.get(id = 3 )
#         self.new_business.update_business('shopkeeper')
#         self.updated_business = Business.objects.get(id = 3)
#         self.assertEqual(self.updated_business.business_name,"shopkeeper")