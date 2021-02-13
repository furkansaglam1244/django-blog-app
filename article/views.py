from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Article,Comment
from .forms import ArticleForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})
def index(request):
    #return HttpResponse("Anasayfa")
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles =Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
#article'ı oluşturduktan sonra bu makaleye bir user vermeliyiz burada bu işlem gerçekleşiyor. kimin yazdığını belirtiyoruz.

        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("article:dashboard")
    context={
        "form":form
    }
    return render(request,"addarticle.html",context)

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)

    comments=article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

#burdaki filter bize bir obje dönüyor biz burda ilk objemizi almak için first fonksiyonunu kullandık.
#get_object_or_404 bize yine bir tane o id li bir tane makalemiz varsa onun objesini bu şekilde döndürecek
#ancak yoksa boş bir 404 sayfası gönderecek. İlk değeri veri çekdiğimiz modeldir. ikincide id si id olan
#articleyi çek diyoruz. o id de article yoksa 404 sayfası gönderiyor.

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,request.FILES or None, instance = article)
    if(article.author!= request.user):
        messages.info(request,"Bu işleme yetkiniz yok. Lütfen bilgilerinizi tekrar kontrol ediniz!!")
        return redirect("index")
    elif form.is_valid():

        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

#instance sayesinde articledeki bütün bilgiler formumuzda görünecektir.

@login_required(login_url = "user:login")
def deleteArticle(request,id):
        article = get_object_or_404(Article, id=id)
        if(article.author!= request.user):
            messages.info(request,"Bu işleme yetkiniz yok. Lütfen bilgilerinizi tekrar kontrol ediniz!!")
            return redirect("index")
        else:
            article.delete()
            messages.success(request,"Makale Başarı ile Silindi.")
            return redirect("article:dashboard")
#article uygulamasının altındaki dashboarda git demiş oluyorum.

def addComment(request,id):
    article=get_object_or_404(Article, id=id)
    form =CommentForm(request.POST or None)
    if form.is_valid():
        if request.method=="POST":
            comment_author=request.POST.get("comment_author")
            comment_content=request.POST.get("comment_content")
            comment_author_email=request.POST.get("comment_author_email")

            newComment=Comment(comment_author = comment_author,comment_content = comment_content,comment_author_email=comment_author_email)
            newComment.article=article
            newComment.save()
            messages.success(request,"Yorum Başarı ile Eklendi.")
        return redirect(reverse("article:detail",kwargs={"id":id}))
    else:        
        messages.info(request,"İsminiz 50 karekterden yorumunuz 300 karekterden fazla olamaz ve lütfen geçerli bir mail adresi giriniz.")
        return redirect(reverse("article:detail",kwargs={"id":id}))



