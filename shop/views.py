
import math
from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact

# Create your views here.
def index(request):
    # products=Product.objects.all()
    # n=len(products)
    # nSlides=n//4 + math.ceil((n/4) -(n//4))
    # allproducts=[[products,range(1,nSlides),nSlides],
    #              [products,range(1,nSlides),nSlides]]
    # params={'allproducts':allproducts}
    # params={'total_slides':nSlides,'range':range(1,nSlides),'product':products}
    
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html",params)
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    if(request.method=="POST"):
        # print(request)
        name=request.POST.get('fname','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        urself=request.POST.get('urself','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        chkbox=request.POST.get('chkbox','')
        contact=Contact(name=name,phone=phone,email=email,password=password,urself=urself,city=city,state=state,chkbox=chkbox)
        # print(name,phone,email,password,urself,city,state,chkbox)
        contact.save()
        
    return render(request,"shop/contact.html")
def tracker(request):
        return render(request,"shop/tracker.html")
def search(request):
        return render(request,"shop/search.html")
def productview(request,myid):
       product=Product.objects.filter(id=myid)

       return render(request,"shop/productview.html",{'product':product[0]})
def checkout(request):
       return render(request,"shop/checkout.html")
