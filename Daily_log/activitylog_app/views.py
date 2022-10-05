from django.shortcuts import render, get_object_or_404,redirect
from .models import Comment
from .forms import  CommentForm
from .filters import CommentFilter
# from django.core.files.storage import FileSystemStorage
# Create your views here.

#list all the comments ,sorted by date time
def comment_list(request):
    comment = Comment.objects.all().order_by('date_time__year','date_time__month','date_time__day','date_time__hour','date_time__minute')
    # comment = Comment.objects.all().order_by('date','time')
    myFilter=CommentFilter(request.GET,queryset=comment)
    comment=myFilter.qs
    return render(request,'activitylog_app/comment/list.html',{'comment': comment,'myFilter':myFilter})

#full detail of comment post
def comment_detail(request,pk):
    comment = get_object_or_404(Comment,id=pk)                           
    return render(request,'activitylog_app/comment/detail.html',{'comment': comment})

#new comment via form input
def new_comment(request):
    form=CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            # automatically set the user as logged in user .....when a form is created
            print("form data:",form)
            form.user=request.user
            print(form.user)
            form.save()
            return comment_list(request) #return to comment_list all comments page
        else:
            print("ERROR FORM INVALID")
    else:
        form = CommentForm(initial={'user':request.user})  # new form to the user
    return render(request,'activitylog_app/comment/form.html',{'form':form})

def update_comment(request,pk):
    comment=Comment.objects.get(id=pk)
    print(comment)
    form=CommentForm(instance=comment)
    print(form)
    if request.method == 'POST':
        print("POST method")
        form = CommentForm(request.POST,request.FILES,instance=comment)
        print(form)
        # form = CommentForm(data=request.POST)
        if form.is_valid():
            # Save the comment to the database
            form.save(commit=True)
            return comment_list(request) #return to comment_list all comments page
        else:
            print("ERROR FORM INVALID")
    else:
        print("get method")
        form = CommentForm(instance=comment)  # new form to the user

    return render(request,'activitylog_app/comment/update_comment.html',{'form':form,'comment':comment})   
