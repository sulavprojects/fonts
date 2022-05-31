from msilib.schema import Font
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .models import Fonts
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def fonts(request):

    #footer = Footer.objects.all()  
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    #websitedata = Modification.objects.latest('websitediscription')


    allfonts = Fonts.objects.filter(publish = True)
    p = Paginator(allfonts, 5)
    page = request.GET.get('page')
    fontsfinal = p.get_page(page)
    

    context = {'fontsfinal': fontsfinal, 
                #'footer': footer, 
                'copyright': copyright,
                'websitedata': websitedata
    
    }
    return render(request , 'theme/index.html',context)




def allfonts(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.filter(publish = True)
    p = Paginator(allfonts, 2)
    page = request.GET.get('page')
    fontsfinal = p.get_page(page)
    

    context = {'fontsfinal': fontsfinal,
               'title': 'all fonts',
               'websitedata': websitedata, 
                
    }

    return render(request , 'fonts/allfonts.html',context)



def fonts_details(request, slug):

    #snippet = get_object_or_404(snippet, slug=slug)

     
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.order_by('-Total_downloads')
    title = Fonts.objects.filter(slug = slug).first()
    
    context = {
        'allfonts': allfonts[:2],
        'title': title,
        'websitedata': websitedata, 
        'copyright': copyright,
        
        
    }
    try:
        fonts_obj = Fonts.objects.filter(slug = slug).first()
        context['fonts_obj'] = fonts_obj
    except Exception as e:
        print(e) 

        
        
    return render(request , 'fonts/fonts_details.html' , context)



def contact(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    context = {
        
        'websitedata': websitedata,
        
        
        
    }


    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, subject, message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "your message has been send to us")
        return redirect('/')
        
    
    return render(request , 'theme/contact.html', context )   
         
    



def termsandcondition(request):

    
    discription = Pages.objects.latest('termsandcondition')
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )

    context = {
        'discription': discription,
        'websitedata': websitedata,
        
        
        
    }
    return render(request, 'theme/termsandcondition.html', context)


def privacypolicy(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    discription = Pages.objects.latest('privacypolicy')
    context = {'discription': discription, 'websitedata': websitedata,}  
    return render(request, 'theme/privacypolicy.html', context)




    
def pages(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    discription = Pages.objects.latest('ourpages')
    context = {'discription': discription, 'websitedata': websitedata,} 
    return render(request, 'theme/pages.html', context)

def aboutus(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    discription = Pages.objects.latest('aboutus')
    context = {'discription': discription, 'websitedata': websitedata,} 
    return render(request, 'theme/aboutus.html', context)