from django.shortcuts import redirect, render
from dataset.disease import Prediction
from prediction.forms import HistoricsForm
from  prediction.models import Historics

# Create your views here.
def index(request):
    form= HistoricsForm()
    predictions = Historics.objects.all()
    context ={'form':form, 'predictions':predictions}

    if request.method == "POST":
        form= HistoricsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            #form.save()
            name = request.POST.get('name')
            symptom_n1 = request.POST.get('symptom_n1')
            symptom_n2 = request.POST.get('symptom_n2')
            symptom_n3 = request.POST.get('symptom_n3')
            psymptoms = [symptom_n1, symptom_n2, symptom_n3]
            prediction, accuracy = Prediction().DecisionTree(name,psymptoms)
            Historics.objects.create(name=name,
                                    symptom_n1 = symptom_n1,
                                    symptom_n2 = symptom_n2,
                                    symptom_n3 = symptom_n3,
                                    prediction= prediction)

            print(prediction)
            context ={'form':form,
             'predictions':predictions,
             'actualpredition':prediction,
             'precision':round(accuracy,3)*100
             }
            return render(request,
            'prediction/index.html',
            context
            )
        else:
            context = {'form':form}
            return render(request,
            'prediction/index.html',
            context)

    return render(request,
            'prediction/index.html',
            context
            )

def contact(request):
    form= HistoricsForm()
    predictions = Historics.objects.all()
    if request.method == "POST":
        form= HistoricsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/prediction/contact')
        
    context ={'form':form, 'predictions':predictions}
    return render(request,
    'prediction/contact.html',
    context
    )