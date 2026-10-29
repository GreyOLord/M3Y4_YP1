import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Model_Users_Role.settings")

django.setup()

from User_and_Changer_role.models import User , Groups


# User.objects.create(
#     name = "Alex",
#     email = "alex@example.com",
#     role = "user")
# User.objects.create(
#     name = "Sofa",
#     email = "sofa@example.com",
#     role = "user")

# User.objects.create(
#     name = "Iosip",
#     email = "iosip@example.com",
#     role = "user")


user1 = User.objects.get(id = 1)
user2 = User.objects.get(id = 2)
user3 = User.objects.get(id = 3)
# user1.change_role('admin')
# print(user1.role)

# Groups.objects.create(
#     name  = "I like Jenifer",
#     topic  = "Witcher",
#     )
group_witcher = Groups.objects.get(id = 1)
# print(group_witcher)

# user2.group.add(group_witcher)
# group_witcher.admin.add(user1)