from django import forms
from django.utils.translation import gettext_lazy as _

class CouponApplyForm(forms.Form):
    code = forms.CharField(label=_('Coupon'),widget=forms.TextInput(attrs={'style': 'width:250px;font-size:17px;margin-bottom:10px;margin-left:10px;padding:10px 12px;border:2px solid #5993bb ;background:#efefef;color:rgb(0, 0, 0);border-radius:4px;'}))
