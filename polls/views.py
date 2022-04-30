from django.shortcuts import render
from polls.forms import PollForm, SearchByNameForm
from general.models import Poll, User, Vote
from scripts import login_required
from django.http import HttpResponseRedirect
from general.models import POLL_TYPES
import hashlib


@login_required
def create_poll_page(request):
    context = {}

    if request.method == 'POST':
        poll = Poll()
        form = PollForm(request.POST)
        if form.is_valid:
            poll.title = form.data['poll_name']
            poll.description = form.data['poll_description']
            poll.variants = '|'.join([form.data['first_var'], form.data['second_var']])
            poll.votes = '0 0 0'
            poll.author = User.objects.get(session=request.COOKIES['session'])
            poll.type = form.data['type']
            poll.save()
            return HttpResponseRedirect('/profile')

    form = PollForm()
    context['form'] = form
    return render(request, 'create_poll.html', context)


@login_required
def poll_page(request):
    context = {}
    
    if request.method == 'GET' and 'id' in request.GET and len(Poll.objects.filter(id=request.GET['id'])) == 1:
        poll = Poll.objects.get(id=request.GET['id'])
        user = User.objects.get(session=request.COOKIES['session'])

        voted = False
        if poll.type[0] == 'A':
            context['is_anonymous'] = True
            voted = False
        else:
            voted = (len(Vote.objects.filter(poll_id=poll.id, user_id=user.id)) > 0)
        
        if voted:
            context['error'] = 'You\'ve already voted'
            
            context['poll'] = poll
            context['ans'] = []
            for (v, p) in zip(poll.votes.split(' '), poll.variants.split('|')):
                context['ans'].append(p + ' - ' + v) 
            
            for short, long in POLL_TYPES:
                if short == poll.type:
                    context['type'] = long
                    break
        else:
            context['poll'] = poll
            context['variants'] = poll.variants.split('|')
            for short, long in POLL_TYPES:
                if short == poll.type:
                    context['type'] = long
                    break
    else:
        context['error'] = 'Wrong request. Please use built-in tools'

    if request.method == 'POST' and 'vote' in request.POST and 'poll_id' in request.POST:
        input_vote = request.POST['vote'].split(' ')
        poll = Poll.objects.get(id=request.POST['poll_id'])

        result_votes = []
        for (db_val, new_val) in zip(poll.votes.split(' '), input_vote):
            result_votes.append(str(int(db_val) + int(new_val)))
        poll.votes = ' '.join(result_votes)

        user = User.objects.get(session=request.COOKIES['session'])

        if poll.type[0] == 'A':
            if 'password' in request.POST:
                password = request.POST['password']
                if user.password_hash == hashlib.sha256((password+user.salt).encode('utf-8')).hexdigest():
                    if len(Vote.objects.filter(poll_id=poll.id, user_id=hashlib.sha256((user.username+password+poll.title).encode('utf-8')).hexdigest())) == 0:
                        poll.save()
                
                        vote = Vote()
                        vote.user_id = hashlib.sha256((user.username+password+poll.title).encode('utf-8')).hexdigest()
                        vote.poll_id = poll.id
                        vote.save()

                        return HttpResponseRedirect('/profile')
                    else:
                        context['error'] = 'You\'ve already voted'
                        
                        context['poll'] = poll
                        context['ans'] = []
                        for (v, p) in zip(poll.votes.split(' '), poll.variants.split('|')):
                            context['ans'].append(p + ' - ' + v) 
                        
                        for short, long in POLL_TYPES:
                            if short == poll.type:
                                context['type'] = long
                                break
                else:
                    context['error'] = 'Wrong password' if password else 'Enter password'
        else:
            poll.save()
    
            vote = Vote()
            vote.user_id = user.id
            vote.poll_id = poll.id
            vote.selected_options = request.POST['vote']
            vote.save()

            return HttpResponseRedirect('/profile')


    return render(request, 'poll_page.html', context)


@login_required
def search_poll(request):
    context = {'form': SearchByNameForm(), 'polls_to_show': []}

    for poll in Poll.objects.all():
        context['polls_to_show'].append("<a href='../poll/?id=" + str(poll.id) + "'>" + poll.title + "</a>")
    if request.method == 'POST':
        if request.POST.get('Find'):
            form = SearchByNameForm(request.POST)
            if form.is_valid():
                try:
                    poll = Poll.objects.get(title=form.data['name_to_find_poll'])
                    context['found_poll'] = "<a href='../poll/?id=" + str(poll.id) + "'>" + poll.title + "</a>"
                except:
                    context['error'] = 'No such poll'
    return render(request, 'search_poll_page.html', context)
