class ReadOnlyFieldsMixin:
    readonly_fields = ()

    def apply_readonly(self):
        for field_name in self.readonly_field_names:
            self.fields[field_name].widget.attrs["readonly"] = ["readonly"]

    @property
    def readonly_field_names(self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()
        return self.readonly_fields

class DisabledFieldsMixin:
    disabled_fields = ()

    def apply_disabled(self):
        for field_name in self.disabled_field_names:
            self.fields[field_name].widget.attrs["disabled"] = ["disabled"]

    @property
    def disabled_field_names(self):
        if self.disabled_fields == "__all__":
            return self.fields.keys()
        return self.disabled_fields



