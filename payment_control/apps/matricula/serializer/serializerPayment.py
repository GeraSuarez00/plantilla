from apps.matricula.models import Payment, month_choices
from rest_framework import fields,serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Payment
        fields= ['id','pay_month','pay_date','pay_value','pay_discount','pay_total_value','payment_type','item_type','payment_method_type','reg_id']
    pay_month= fields.MultipleChoiceField(choices=month_choices)
    
    def to_representation(self, instance):
        return {
           'id': instance.id,
           'pay_month':instance.pay_month,
           'pay_date':instance.pay_date,
           'pay_value':instance.pay_value,
           'pay_discount':instance.pay_discount,
           'pay_total_value':instance.pay_total_value,
           'payment_type': {
            'nombre': instance.payment_type.maes_names,
            'id': instance.payment_type.id
            },
           'item_type': {
            'nombre': instance.item_type.maes_names,
            'id': instance.item_type.id
            },
           'payment_method_type': {
            'nombre': instance.payment_method_type.maes_names,
            'id': instance.payment_method_type.id
            },
           'reg_id': {
            'identificación': instance.reg_id.stu_id.per_id.per_identity_number, 
            'nombre': instance.reg_id.stu_id.per_id.per_names, 
            'apellidos': instance.reg_id.stu_id.per_id.per_surnames, 
            # 'id': instance.reg_id.stu_id.per_id.id
            'id': instance.reg_id.id
            }
        }
    