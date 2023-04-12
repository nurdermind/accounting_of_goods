from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ExtraActionMixin(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    extra_serializers = {}

    def __init__(self, *args, **kwargs):
        super(ExtraActionMixin, self).__init__(*args, **kwargs)
        assert all(self.extra_serializers.values()), "All extra serializers must be defined"

    def get_serializer_class(self):
        if self.action in self.extra_serializers:
            return self.extra_serializers[self.action]
        return super().get_serializer_class()

    def apply_changes(self, request, get_new_value_func):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        fields_for_increase = serializer.Meta.fields

        for field_for_increase in fields_for_increase:
            if serializer.validated_data.get(field_for_increase) is not None:
                serializer.validated_data[field_for_increase] = get_new_value_func(
                    original_value=getattr(instance, field_for_increase),
                    other_value=serializer.validated_data[field_for_increase]
                )

        self.perform_update(serializer)
        return Response(serializer.validated_data)


class IncreaseActionMixin(ExtraActionMixin):
    extra_serializers = ExtraActionMixin.extra_serializers
    extra_serializers.update({
        'increase': None
    })

    @action(methods=['patch'], detail=True, url_path='increase')
    def increase(self, request, *args, **kwargs):
        return self.apply_changes(request,
                                  lambda original_value, other_value: original_value + other_value
                                  )


class ReduceActionMixin(ExtraActionMixin):
    extra_serializers = ExtraActionMixin.extra_serializers
    extra_serializers.update({
        'reduce': None
    })

    @action(methods=['patch'], detail=True, url_path='reduce')
    def reduce(self, request, *args, **kwargs):
        return self.apply_changes(request,
                                  lambda original_value, other_value: original_value - other_value
                                  )
