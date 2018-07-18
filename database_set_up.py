from refugee.models import Gender
from django.contrib.auth.models import Group, Permission


def main():
    gender_items = [{"name": "Male"}, {"name": "Female"}]

    for item in gender_items:
        gender, created = Gender.objects.get_or_create(name=item.get("name"), )
        gender.save()

    group_items = [
        {"name":"custom_admin", "permissions":[
            "custom_can_add_user", "custom_can_edit_user", "custom_can_delete_user",
            "can_allocate_distribution", "can_clear_distribution",
            "custom_can_add_food_unit", "custom_can_delete_food_unit", "custom_can_update_food_unit",
            "custom_can_add_food", "custom_can_delete_food", "custom_can_update_food",
            "custom_can_add_gender", "custom_can_update_gender", "custom_can_delete_gender",
            "custom_can_add_refugee", "custom_can_update_refugee", "custom_can_delete_refugee",
          ]},
        {"name":"project_manager", "permissions":[
            "can_allocate_distribution", "can_clear_distribution",
            "custom_can_add_food_unit", "custom_can_delete_food_unit",
            "custom_can_update_food_unit",
            "custom_can_add_food", "custom_can_delete_food", "custom_can_update_food",
            "custom_can_add_gender", "custom_can_update_gender", "custom_can_delete_gender",
            "custom_can_add_refugee", "custom_can_update_refugee", "custom_can_delete_refugee",
        ]},
        {"name":"enumerator", "permissions":[
            "can_clear_distribution",
            "custom_can_add_refugee", "custom_can_update_refugee", "custom_can_delete_refugee",
        ]}
    ]

    for item in group_items :
        group, created = Group.objects.get_or_create(name=item.get("name"))
        permissions = [Permission.objects.get(codename=permission_name) for permission_name in item.get("permissions")]
        [group.permissions.add(permission) for permission in permissions]
        group.save()
