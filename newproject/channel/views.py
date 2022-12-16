from django.shortcuts import render, redirect, get_object_or_404
from .models import Channel, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import CreateChannel, CreateComment

def channel_list(request):
    channel = Channel.objects.all().order_by('date')
    return render(request, 'channel/channel_list.html', {'channel': channel})

def channel_detail(request,slug):
    #return HttpResponse(slug)
    channel = Channel.objects.get(slug=slug)

    if request.method == 'POST':
        form = CreateComment(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.channelname = channel
            obj.save()

            return redirect('channel:detail', slug=channel.slug)
    else:
        form = CreateComment()

    context = {
        'channel' : channel,
        'form' : form,
    }

    return render(request, 'channel/channel_detail.html', context)

@login_required(login_url="/accounts/login/")
def my_channel(request):
    channel = Channel.objects.filter(author=request.user)
    return render(request, 'channel/my_channel.html', {'channel': channel})

@login_required(login_url="/accounts/login/")
def channel_create(request):
    if request.method == 'POST':
        form = CreateChannel(request.POST, request.FILES)
        if form.is_valid():
            # save channel to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('channel:myChannel')
    else:
        form = CreateChannel()
    return render(request, "channel/channel_create.html", {'form':form})

@login_required(login_url="/accounts/login/")
def update_channel(request, channel_id):
    channel_id = int(channel_id)
    try:
        channel_sel = Channel.objects.get(id=channel_id)
    except Channel.DoesNotExist:
        return redirect('channels:myChannel')
    form = CreateChannel(request.POST or None, instance=channel_sel)
    if form.is_valid():
        form.save()
        return redirect('channel:myChannel')
    return render(request, 'channel/channel_create.html', {'form': form})

def delete_channel(request, channel_id):
    channel_id = int(channel_id)
    try:
        channel_sel = Channel.objects.get(id = channel_id)
    except Channel.DoesNotExist:
        return redirect('channel:myChannel')
    channel_sel.delete()
    return redirect('channel:myChannel')