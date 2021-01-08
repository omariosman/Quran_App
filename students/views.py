from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Shaikh, Student, Student_Class, Surah_Quran
from .forms import Student_Class_Form
# Create your views here.

def add_student_class(request):
    current_shaikh = Shaikh.objects.get(user = request.user)
    
    checkbox = False
    surahs = Surah_Quran.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        #form = Student_Class_Form(request.POST) #if form.is_valid():
        #new_form = form.save(commit=False)
        #new_form.user = request.user
        
        
        att = checkbox
        mywerd = request.POST["surah_werd"]
        mywerd_grade = request.POST.get("werd_grade", False)
        myrevision = request.POST["surah_revision"]
        myrevision_grade = request.POST["revision_grade"]
        mystudent_code = request.POST["students_names"]
        
        mystudent = Student.objects.get(code=mystudent_code)
        
        data = Student_Class(student_code=mystudent, werd=mywerd, werd_grade=mywerd_grade, revision=myrevision, revision_grade=myrevision_grade, attendance=att)
        #form.save()
        data.save()
        return redirect('/students/add_student_class')

    else:
        form = Student_Class_Form()

    context = {
        "form": form, 
        "surahs": surahs,
        "students": students,
        "checkbox": checkbox,
        "current_shaikh": current_shaikh,
    
    }


    return render(request, "add_student_class.html", context)

   
def home(request):
    return render(request, "home.html", {})

