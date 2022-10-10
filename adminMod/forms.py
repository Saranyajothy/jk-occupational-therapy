import datetime
# from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from .models import appointment

CURRENT_DATE = str(datetime.date.today())


class AppointmentForm(forms.ModelForm): 
    class Meta:
        model = appointment
        fields = ['firstname', 'lastname', 'email', 'mobile_ext', 'mobile', 'date', 'time', 'symptoms', 'address']
        
        labels = {
            'firstname': 'Firstname',
            'lastname': 'Lastname',
            'email': 'Email',
            'mobile_ext': 'Mobile_ext',
            'mobile': 'Mobile',
            'date': 'Date',
            'time': 'Time',
            'symptoms': 'Symptoms',
            'address': 'Address',
            }

        widgets = {
            # 'date': DatePickerInput(
            #     options={
            #         "format": "DD/MM/YYYY",
            #         "showClose": True,
            #         "showClear": True,
            #         "showTodayButton": True,
            #         'minDate': CURRENT_DATE,
            #     }
            # ),
            'firstname': forms.Textarea(attrs={'rows': 1, 'cols': 35,
                                                'placeholder':
                                                'Firstame(required)',
                                                'class': 'form-control',
                                                  },
                                           ), 
             
            'lastname': forms.Textarea(attrs={'rows': 1, 'cols': 25,
                                                  'placeholder':
                                                  'Lastame(required)',
                                                  'class': 'form-control',
                                                  },
                                           ),
            'email': forms.Textarea(attrs={'rows': 1, 'cols': 25, 
                                                  'placeholder':
                                                  'Email(required)',
                                                  'class': 'form-control',
                                                  'type': 'email'
                                                  },
                                           ), 
            'mobile_ext': forms.NumberInput(attrs={'rows': 1, 'cols': 25,
                                                  'placeholder':
                                                  'Code(required)',
                                                  'class': 'form-control',
                                                  },
                                           ),  
            'mobile': forms.NumberInput(attrs={'rows': 1, 'cols': 25,
                                                  'placeholder':
                                                  'Number(required)',
                                                  'class': 'form-control',
                                                  },
                                           ), 
                                           
            'time': forms.TimeInput(attrs={'rows': 1, 'cols': 25,
                                                  'placeholder':
                                                  '(required)',
                                                  'class': 'form-control',
                                                  'type': 'time'
                                                  },
                                           ), 
           
            'symptoms': forms.Textarea(attrs={'rows': 2, 'cols': 25,
                                                  'placeholder':
                                                  '(required)',
                                                  'class': 'form-control',
                                                  },
                                           ),   
            'address': forms.Textarea(attrs={'rows': 1, 'cols': 25,
                                                  'placeholder':
                                                  '(required)',
                                                  'class': 'form-control',
                                                  },
                                           ),                                                                                                                                                                                                  
        }