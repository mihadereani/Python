from django.shortcuts import render
from .models import Sale
# to protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale


# Create your views here.


def home(request):
    return render(request, 'sales/home.html')

# define function-based view - records(records()


def records(request):
    # create an instance of SalesSearchForm that you defined in sales/forms.py
    form = SalesSearchForm(request.POST or None)

    # check if the button is clicked
    if request.method == 'POST':
        # read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        # display in terminal - needed for debugging during development only
        print(book_title, chart_type)

        print('Exploring querysets:')
        print('Case 1: Output of Sale.objects.all()')
        qs = Sale.objects.all()
        print(qs)

        print('Case 2: Output of Sale.objects.filter(book_name=book_title)')
        qs = Sale.objects.filter(book__name=book_title)
        print(qs)

        print('Case 3: Output of qs.values')
        print(qs.values())

        print('Case 4: Output of qs.values_list()')
        print(qs.values_list())

        print('Case 5: Output of Sale.objects.get(id=1)')
        obj = Sale.objects.get(id=1)
        print(obj)

    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
    }

    # load the sales/record.html page using the data that you just prepared
    return render(request, 'sales/records.html', context)
