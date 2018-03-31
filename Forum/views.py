from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Forum.models import category, forum, message
# Create your views here.
def listing(request, c_id=None):
    if request.user.is_authenticated():
        username = request.user.username

    # get category list
    head_cat = category.objects.all()

    # identify whether user selected category
    if c_id is not None:
        try:
            cat = category.objects.get(id=c_id)
        except:
            # default get the category id=0
            cat = None
            messages.add_message(request, messages.ERROR, '該類別不存在.')

        if cat is not None:
            # filting the forum article by category id
            article_list = forum.objects.filter(category=cat)
        else:
            article_list = forum.objects.all()
    else:
        article_list = forum.objects.all()

    # setting the paginator
    paginator = Paginator(article_list, 6) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        current_article = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        current_article = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_article = paginator.page(paginator.num_pages)

    return render(request, 'Forum/listing.html', locals())


def details(request, f_id=None):
    if request.user.is_authenticated():
        username = request.user.username

    # get the specific article detail informations
    try:
        contents = forum.objects.get(id=f_id)
    except:
        contents = None
        # error message
        messages.add_message(request, messages.WARNING, '這篇文章不存在!')

    # get the specific article messages
    if contents is not None:
        msgs = message.objects.filter(forum_id=f_id)

    return render(request, 'Forum/details.html', locals())

