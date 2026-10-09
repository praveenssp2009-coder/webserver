from django.shortcuts import render


def name_ref_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        ref_number = request.POST.get('ref_number', '')
        return render(
            request,
            'form.html',
            {
                'name': name,
                'ref_number': ref_number,
                'submitted': True,
            },
        )

    return render(request, 'form.html', {'submitted': False})
