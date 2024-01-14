from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import bench, squat, dead
from .forms import BenchForm, SquatForm, DeadForm
from django.db.models import Max, F
import plotly.express as px 
# Create your views here.


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def log(request):
    template = loader.get_template('pick.html')
    return HttpResponse(template.render())
    # total = bench.objects.all()
    # return render(request, 'here.html', {'total': total})



def bench_create (request):
    if request.method == 'POST':
        form = BenchForm(request.POST)

        if form.is_valid():
            b = form.save()

    else:
        form = BenchForm()
    return render(request, 'bench_create.html',{'form': form} )

def bench_update(request, id):
    b = bench.objects.get(id=id)
    if request.method == 'POST':
        form = BenchForm(request.POST, instance=b)
        #if form.is_valid():
        form.save()
    else:
        form=BenchForm(instance=b)
            

    return render(request, 'bench_update.html', {'form':form})

def squat_create (request):
    if request.method == 'POST':
        form = SquatForm(request.POST)

        if form.is_valid():
            b = form.save()

    else:
        form = SquatForm()
    return render(request, 'squat_create.html',{'form': form} )

def squat_update(request, id):
    b = squat.objects.get(id=id)
    if request.method == 'POST':
        form = SquatForm(request.POST, instance=b)
        #if form.is_valid():
        form.save()
    else:
        form=SquatForm(instance=b)
            

    return render(request, 'squat_update.html', {'form':form})

def dead_update(request, id):
    b = dead.objects.get(id=id)
    if request.method == 'POST':
        form = DeadForm(request.POST, instance=b)
        #if form.is_valid():
        form.save()
    else:
        form=DeadForm(instance=b)
            

    return render(request, 'dead_update.html', {'form':form})
def dead_create (request):
    if request.method == 'POST':
        form = DeadForm(request.POST)

        if form.is_valid():
            b = form.save()

    else:
        form = DeadForm()
    return render(request, 'dead_create.html',{'form': form} )

def bench_details(request):

    distinct_dates = bench.objects.order_by('-date').values('date').distinct()

    data_by_date = {}

    for date_entry in distinct_dates:
        date = date_entry['date']
        weights = bench.objects.filter(date=date)
        data_by_date[date] = weights

    max_entries = {}
    x = 0 
   
    maxW= 0
    for r in range(10,0, -1):
        
        
        max_w = bench.objects.filter(reps=r).aggregate(Max('weight'))
    
        if max_w["weight__max"]:
            x = 1
            
            max_date = bench.objects.filter(reps=r, weight = max_w["weight__max"]).first()
            
            for repps in range (r, 0,-1):
                if max_w["weight__max"] >= maxW:
                    maxW = max_w["weight__max"]
                    max_entries[repps] = {
                        'weight':max_w["weight__max"],
                        'date':max_date.date
                    }
                   
                
            
        elif x == 1:
            pass
        
        else:
                max_entries[r] = {
                    'weight': None,
                    'date': None
                }

        
    
    return render(request, 'bench_details.html',  {'data_by_date': data_by_date, "max_entries": max_entries})

def squat_details(request):

    distinct_dates = squat.objects.order_by('-date').values('date').distinct()

    data_by_date = {}

    for date_entry in distinct_dates:
        date = date_entry['date']
        weights = squat.objects.filter(date=date)
        data_by_date[date] = weights

    max_entries = {}
    x = 0 
   
    maxW= 0
    for r in range(10,0, -1):
        
        
        max_w = squat.objects.filter(reps=r).aggregate(Max('weight'))
    
        if max_w["weight__max"]:
            x = 1
            
            max_date = squat.objects.filter(reps=r, weight = max_w["weight__max"]).first()
            
            for repps in range (r, 0,-1):
                if max_w["weight__max"] >= maxW:
                    maxW = max_w["weight__max"]
                    max_entries[repps] = {
                        'weight':max_w["weight__max"],
                        'date':max_date.date
                    }
                   
                
            
        elif x == 1:
            pass
        
        else:
                max_entries[r] = {
                    'weight': None,
                    'date': None
                }

        
    
    return render(request, 'squat_details.html',  {'data_by_date': data_by_date, "max_entries": max_entries})

def dead_details(request):

    distinct_dates = dead.objects.order_by('-date').values('date').distinct()

    data_by_date = {}

    for date_entry in distinct_dates:
        date = date_entry['date']
        weights = dead.objects.filter(date=date)
        data_by_date[date] = weights

    max_entries = {}
    x = 0 
   
    maxW= 0
    for r in range(10,0, -1):
        
        
        max_w = dead.objects.filter(reps=r).aggregate(Max('weight'))
    
        if max_w["weight__max"]:
            x = 1
            
            max_date = dead.objects.filter(reps=r, weight = max_w["weight__max"]).first()
            
            for repps in range (r, 0,-1):
                if max_w["weight__max"] >= maxW:
                    maxW = max_w["weight__max"]
                    max_entries[repps] = {
                        'weight':max_w["weight__max"],
                        'date':max_date.date
                    }
                   
                
            
        elif x == 1:
            pass
        
        else:
                max_entries[r] = {
                    'weight': None,
                    'date': None
                }

        
    
    return render(request, 'dead_details.html',  {'data_by_date': data_by_date, "max_entries": max_entries})

def bench_delete(request, id):
    b = bench.objects.get(id=id)

    if request.method == 'POST':
        b.delete()

        return redirect('bench-details')
    return render(request, 'bench_delete.html', {'b':b})

def squat_delete(request, id):
    b = squat.objects.get(id=id)

    if request.method == 'POST':
        b.delete()

        return redirect('squat-details')
    return render(request, 'squat_delete.html', {'b':b})


def dead_delete(request, id):
    b = dead.objects.get(id=id)

    if request.method == 'POST':
        b.delete()

        return redirect('dead-details')
    return render(request, 'dead_delete.html', {'b':b})


def bench_graph(request):
    entry = bench.objects.all()
    h =[]
    v = []
    i=-1
    for w in entry:

        if w.date in h:
            
            if w.estimate > v[i]:
                v.pop()
                v.append(w.estimate)
                


        else:
            h.append(w.date)
            v.append(w.estimate)
            i += 1
        
    
    fig = px.line(
        x= h,  
        y = v, 
        title = 'Bench One Rep Max estimation Progress',
        labels={'x':'Workout Date', 'y': 'One Rep Max Estimation'}

    )

    fig.update_layout(title = {
        'font_size': 10,
        'xanchor':'center',
        'x':0.5
    }
                      )

    chart = fig.to_html()

    context = {"chart": chart}

   

    return render(request, 'graph.html', context)

def squat_graph(request):
    entry = squat.objects.all()
    
    h =[]
    v = []
    i=-1
    for w in entry:

        if w.date in h:
            
            if w.estimate > v[i]:
                v.pop()
                v.append(w.estimate)
                


        else:
            h.append(w.date)
            v.append(w.estimate)
            i += 1
        
    
    fig = px.line(
        x= h,  
        y = v, 
        title = 'Squat One Rep Max estimation Progress',
        labels={'x':'Workout Date', 'y': 'One Rep Max Estimation'}

    )

    fig.update_layout(title = {
        'font_size': 10,
        'xanchor':'center',
        'x':0.5
    }
                      )

    chart = fig.to_html()

    context = {"chart": chart}

   

    return render(request, 'graph.html', context)

def dead_graph(request):
    entry = dead.objects.all()
    h =[]
    v = []
    i=-1
    for w in entry:

        if w.date in h:
            
            if w.estimate > v[i]:
                v.pop()
                v.append(w.estimate)
                


        else:
            h.append(w.date)
            v.append(w.estimate)
            i += 1
        
    
    fig = px.line(
        x= h,  
        y = v, 
        title = 'Deadlift One Rep Max estimation Progress',
        labels={'x':'Workout Date', 'y': 'One Rep Max Estimation'}

    )

    fig.update_layout(title = {
        'font_size': 10,
        'xanchor':'center',
        'x':0.5
    }
                      )

    chart = fig.to_html()

    context = {"chart": chart}

   

    return render(request, 'graph.html', context)