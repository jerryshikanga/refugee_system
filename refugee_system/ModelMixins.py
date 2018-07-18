class ModelMixin(object):
    def get_fields(self):
        field_list = [[field.name, field.value_to_string(self)] for field in self._meta.fields if field.name is not "id"]
        return field_list
