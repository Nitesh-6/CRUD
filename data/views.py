from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from data.models import User, Details
from data.forms import MyForm
from django.contrib import messages
# Create your views here.

def process_data(req):
    if req.method == 'POST':
        form = MyForm(req.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            existing_record = Details.objects.filter(username=username)
            if existing_record.exists():
                return render(req, "index1.html", {'form': form, 'error_message': 'Username already exists.'})
            else:
                Details.objects.create(firstname=firstname, lastname=lastname, username=username, city=city, state=state, zipcode=zipcode)
                return redirect('/data/getdetails/')
    else:
        form = MyForm()
    
    return render(req, "index1.html", {'form': form})


def get_details(req):
    det = Details.objects.values()
    return render(req, 'getdata.html',{'det':det})

    
def update_content(req, id):
    if req.method=="POST":
        upd =  Details.objects.get(pk=id)
        fm = MyForm(req.POST, instance=upd)
        if fm.is_valid():
            fm.save()
            messages.success(req, f"data updated successfully")
            return HttpResponseRedirect('/data/{}'.format(id))
    else:
        upd =  Details.objects.get(pk=id)
        fm = MyForm(instance=upd)
        return render(req, 'update.html', {'form': fm})

def delete_rec(req, id):
    if req.method=='POST':
        delete = Details.objects.get(pk = id)
        delete.delete()
        return HttpResponseRedirect('/data/getdetails/')