import discord
import os
from discord.ext.commands import Bot
import requests
from bs4 import BeautifulSoup
from server import keep_running

client = Bot(command_prefix='$')
#bot=Bot(command_prefix='$'


@client.event
async def on_ready():
    print('We are logged in', client.user)


def live_score():
    res = requests.get(
        'https://m.cricbuzz.com/cricket-series/3472/indian-premier-league-2021'
    )
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(id='scag_live')
    head = data.find(class_='panel-heading').text.split('/')[1].strip()
    teams = data.find_all(class_='col-xs-5 col-lg-5 cb-col-no-padding')
    score = data.find_all(class_='col-xs-7 col-lg-7 cb-col-no-padding')
    status = data.find(class_='cb-match-status').text.strip()
    score1 = score[0].text
    score2 = score[1].text
    team1 = teams[0].text.strip()
    team2 = teams[1].text.strip()
    head += ' ' + '(' + team1 + ' vs ' + team2 + ' )'
    # s=team1+' vs '+team2+'\n'
    s = team1 + ' ' + score1 + '\n'
    s += team2 + ' ' + score2 + '\n'
    # print(team1+' vs '+team2)
    # print(team1+' '+ score1)
    # print(team2+' '+score2)
    if (status == ''):
        s += 'Match not started yet'
        #print('Match not started yet')
    else:
        s += status
        #print(status)
    #print(s)
    return s, head


def live_score2():
    res = requests.get(
        'https://m.cricbuzz.com/cricket-series/3472/indian-premier-league-2021'
    )
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(id='scag_live')
    head = data.find(class_='panel-heading').text.split('/')[1].strip()
    no = head.split()[0][:3]
    res = requests.get('https://www.cricbuzz.com/live-cricket-scores/35622/' +
                       no + '-match-indian-premier-league-2021')
    data = BeautifulSoup(res.text, 'html.parser')
    score = data.find(class_='cb-col cb-col-67 cb-scrs-wrp')
    team1 = score.find(class_='cb-text-gray cb-font-16').text.strip()
    team2 = score.find(class_='cb-min-bat-rw').find(
        class_='cb-font-20 text-bold').text.strip()
    status = score.find(class_='cb-text-inprogress').text.strip()
    rate = score.find_all(class_='cb-font-12 cb-text-gray')
    runrate = rate[0].span.next_sibling.text.strip()
    required = rate[1].span.next_sibling.text.strip()
    head = head + ' ( ' + team1.split()[0] + ' vs ' + team2.split()[0] + ' )'
    s = ''
    s += team1 + '\n'
    s += team2 + '\n'
    s += 'CRR: ' + runrate + ' , ' + 'REQ: ' + required + '\n'
    s += status
    # print(head)
    # print(team1)
    # print(team2)
    # print('CRR:',runrate,',','REQ:',required)
    # print(status)
    return s, head


def live_score3():
    res = requests.get(
        'https://m.cricbuzz.com/cricket-series/3472/indian-premier-league-2021'
    )
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(id='scag_live')
    head = data.find(class_='panel-heading').text.split('/')[1].strip()
    no = head.split()[0][:3]
    res = requests.get('https://www.cricbuzz.com/live-cricket-scores/35622/' +
                       no + '-match-indian-premier-league-2021')
    data = BeautifulSoup(res.text, 'html.parser')
    score = data.find(class_='cb-col cb-col-67 cb-scrs-wrp')
    s = ''
    team1 = score.find(class_='cb-min-tm').text.strip()
    team2 = score.find(
        class_='cb-min-tm').next_sibling.next_sibling.text.strip()
    s += team1 + '\n'
    s += team2 + '\n'
    status = data.find(class_='cb-text-inprogress')
    #print(status)
    if (status == None):
        status = data.find(class_='cb-text-complete').text.strip()
    else:
        status = status.text.strip()
    s += status + '\n'
    rate = score.find_all(class_='cb-font-12 cb-text-gray')
    if (len(rate) != 0):
        runrate = rate[0].span.next_sibling.text.strip()
        required = rate[1].span.next_sibling.text.strip()
        s += 'CRR:' + runrate + ',' + 'REQ:' + required + '\n'
    head = head + ' ( ' + team1.split()[0] + ' vs ' + team2.split()[0] + ' )'
    #     print(head)
    #     print(team1)
    #     print(team2)
    #     print('CRR:',runrate,',','REQ:',required)
    #     print(status)
    return s, head


# def live_score_final():
#   res=requests.get('https://www.cricbuzz.com/cricket-match/live-scores')
#   url='https://www.cricbuzz.com'
#   data=BeautifulSoup(res.text,'html.parser')
#   data=data.find(class_='cb-mat-mnu')
#   link=data.a.next_sibling.get('href')
#   link=url+link
#   res=requests.get(link)
#   data=BeautifulSoup(res.text,'html.parser')
#   status1=data.find(class_='cb-text-inprogress')
#   status2=data.find(class_='cb-text-complete')
#   if(status1==None):
#     status1=data.find(class_='cb-text-inningsbreak')
#   head=data.find(class_='cb-nav-hdr cb-font-18 line-ht24')
#   match=head.text.strip().split(',')[0]
#   match_no=head.text.strip().split(',')[1]
#   match_no=match_no.strip().split('-')[0].strip()
#   data=data.find(class_='cb-col cb-col-67 cb-scrs-wrp')
#   head=match_no+' '+match
#   if(status1==None and status2==None):
#     data=BeautifulSoup(res.text,'html.parser')
#     data=data.find(class_='cb-nav-subhdr cb-font-12')
#     time=data.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.next_sibling.text.strip()
#     s='Match will be start from '+time
#     return s,head
#     print("Not Live any match")
#     return
#   if(status1!=None):
#     team1=''
#     team2=''
#     if(data.div.span==None):
#       team1=data.div.text.strip()
#       team2=data.span.text.strip()
#     else:
#       team1=data.div.span.text.strip()
#     s=''
#     if(team1!=''):
#         s+=team1+'\n'
#     if(team2!=''):
#         s+=team2+'\n'
#     s+=status1.text.strip()
#   else:
#     team1=data.div.text.strip()
#     team2=data.div.next_sibling.next_sibling.text.strip()
#     s=''
#     if(team1!=''):
#         s+=team1+'\n'
#     if(team2!=''):
#         s+=team2+'\n'
#     s+=status2.text.strip()
#   return s,head


def live_score_final():
    res = requests.get('https://www.cricbuzz.com/cricket-match/live-scores')
    url = 'https://www.cricbuzz.com'
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(class_='cb-mat-mnu')
    link = data.a.next_sibling.get('href')
    link = url + link
    res = requests.get(link)
    data = BeautifulSoup(res.text, 'html.parser')
    inprogress=data.find(class_='cb-text-inprogress')
    complete=data.find(class_='cb-text-complete')
    abandon=data.find(class_='cb-text-abondon')
    stumps=data.find(class_='cb-text-stumps')
    inningsbreak=data.find(class_='cb-text-inningsbreak')
    rain=data.find(class_='cb-text-rain')
    badlight=data.find(class_='cb-text-badlight')
    lunch=data.find(class_='cb-text-lunch')
    tea=data.find(class_='cb-text-tea')
    wetoutfield=data.find(class_='cb-text-wetoutfield')
    # status1 = data.find(class_='cb-text-inprogress')
    # status2 = data.find(class_='cb-text-complete')
    # abandon = data.find(class_='cb-text-abandon')
    head = data.find(class_='cb-nav-hdr cb-font-18 line-ht24')
    match = head.text.strip().split(',')[0]
    match_no = head.text.strip().split(',')[1]
    match_no = match_no.strip().split('-')[0].strip()
    data = data.find(class_='cb-col cb-col-67 cb-scrs-wrp')
    batting = [['Batsman', 'R', 'B', '4s', '6s', 'SR']]
    bowling = [['Bowler', 'O', 'M', 'R', 'W', 'ECO']]
    s = ''
    head = match_no + ' ' + match

    if (abandon != None):
        s=abandon.text.strip()
        return s, head, '', ''
    if (inprogress!=None or inningsbreak!=None or stumps!=None or rain!=None or lunch!=None or tea!=None or badlight!=None or wetoutfield!=None):
        status=inprogress
        if(status==None):
            status=inningsbreak;
            if(status==None):
                status=stumps
                if(status==None):
                    status=lunch
                    if(status==None):
                        status=tea
                        if(status==None):
                            status=rain
                            if(status==None):
                              status=badlight
                              if(status==None):
                                status=wetoutfield
        team1 = ''
        team2 = ''
        if (data.div.span == None):
            team1 = data.div.text.strip()
            team2 = data.span.text.strip()
            runrate = data.find_all('span')
            crr = data.find_all('span')[3].text.strip()
            team2 += ' CRR: ' + crr
            if (len(runrate) > 6):
                reqrr = data.find_all('span')[6].text.strip()
                team2 += ' , REQ: ' + reqrr
        else:
            team1 = data.div.span.text.strip()
            crr = data.div.span.next_sibling.next_sibling.span.next_sibling.text.strip(
            )
            team1 += ' CRR: ' + crr
        s = ''
        if (team1 != ''):
            s += team1 + '\n'
        if (team2 != ''):
            s += team2 + '\n'
        s += status.text.strip()

        if ('Break' in status.text.strip()):
            return s, head, '', ''

        data = BeautifulSoup(res.text, 'html.parser')
        data = data.find(class_='cb-col-67 cb-col')
        bat = data.div
        bowl = data.div.next_sibling
        bat = bat.find_all(class_='cb-col cb-col-100 cb-min-itm-rw')
        bowl = bowl.find_all(class_='cb-col cb-col-100 cb-min-itm-rw')
        for i in bat:
            name = i.div
            run = name.next_sibling
            ball = run.next_sibling
            four = ball.next_sibling
            six = four.next_sibling
            sr = six.next_sibling
            batting.append([
                name.text.strip(),
                run.text.strip(),
                ball.text.strip(),
                four.text.strip(),
                six.text.strip(),
                sr.text.strip()
            ])
        for i in bowl:
            name = i.div
            over = name.next_sibling
            maiden = over.next_sibling
            runs = maiden.next_sibling
            wicket = runs.next_sibling
            eco = wicket.next_sibling
            bowling.append([
                name.text.strip(),
                over.text.strip(),
                maiden.text.strip(),
                runs.text.strip(),
                wicket.text.strip(),
                eco.text.strip()
            ])

        for i in range(len(batting)):
            for j in range(6):
                if (j == 0):
                    x = len(batting[i][j])
                    rem = 18 - x
                    for k in range(rem):
                        batting[i][j] += ' '
                elif (j == 1):
                    x = len(batting[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        batting[i][j] += ' '
                elif (j == 2):
                    x = len(batting[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        batting[i][j] += ' '
                elif (j == 3):
                    x = len(batting[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        batting[i][j] += ' '
                elif (j == 4):
                    x = len(batting[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        batting[i][j] += ' '
                else:
                    x = len(batting[i][j])
                    rem = 6 - x
                    for k in range(rem):
                        batting[i][j] += ' '

        for i in range(len(bowling)):
            for j in range(6):
                if (j == 0):
                    x = len(bowling[i][j])
                    rem = 18 - x
                    for k in range(rem):
                        bowling[i][j] += ' '
                elif (j == 1):
                    x = len(bowling[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        bowling[i][j] += ' '
                elif (j == 2):
                    x = len(bowling[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        bowling[i][j] += ' '
                elif (j == 3):
                    x = len(bowling[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        bowling[i][j] += ' '
                elif (j == 4):
                    x = len(bowling[i][j])
                    rem = 3 - x
                    for k in range(rem):
                        bowling[i][j] += ' '
                else:
                    x = len(bowling[i][j])
                    rem = 6 - x
                    for k in range(rem):
                        bowling[i][j] += ' '
        bat = ''
        bowl = ''
        for i in range(len(batting)):
            for j in range(len(batting[i])):
                bat += batting[i][j] + ' '
            if (i == 0):
                bat += '\n'
            bat += '\n'
        for i in range(len(bowling)):
            for j in range(len(bowling[i])):
                bowl += bowling[i][j] + ' '
            if (i == 0):
                bowl += '\n'
            bowl += '\n'
        return s, head, bat, bowl

    elif(complete!=None):
        status=complete
        team1 = data.div.text.strip()
        team2 = data.div.next_sibling.next_sibling.text.strip()
        data = BeautifulSoup(res.text, 'html.parser')
        mom = data.find(class_='cb-mom-itm')
        if (mom != None):
            mom = mom.a.text.strip()
        s = ''
        if (team1 != ''):
            s += team1 + '\n'
        if (team2 != ''):
            s += team2 + '\n'
        s += status.text.strip()
        if (mom != None):
            s += '\n' + 'Player of the Match: ' + mom
        return s, head, '', ''
    else:
        data = BeautifulSoup(res.text, 'html.parser')
        data = data.find(class_='cb-nav-subhdr cb-font-12')
        time = data.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.next_sibling.text.strip(
        )
        print(head)
        res = requests.get('https://m.cricbuzz.com/')
        data = BeautifulSoup(res.text, 'html.parser')
        toss = data.find(
            class_='cbz-ui-home')
        s = ''
        if (toss != None):
            toss = toss.text.strip()
            s += toss + '\n'
        #s += 'Match will be start from ' + time
        print('Match start from ', time)
        return s, head, '', ''


def point_table():
    res = requests.get(
        'https://m.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/points-table'
    )
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(class_='table')
    l = [['Teams', 'P', 'W', 'L', 'Pts', 'Nrr']]
    pt = data.find('tbody').find_all('td')
    i = 0
    i = 0
    while (i < len(pt)):
        team = pt[i].text
        if ('Bangalore' in team):
            team = 'RCB  '
        elif ('Chennai' in team):
            team = 'CSK  '
        elif ('Hyderabad' in team):
            team = 'SRH  '
        elif ('Delhi' in team):
            team = 'DC   '
        elif ('Kolkata' in team):
            team = 'KKR  '
        elif ('Punjab' in team):
            team = 'PBKS '
        elif ('Rajasthan' in team):
            team = 'RR   '
        else:
            team = 'MI   '
        played = pt[i + 1].text
        wins = pt[i + 2].text
        loss = pt[i + 3].text
        pts = pt[i + 4].text
        runrate = pt[i + 5].text
        l.append([team, played, wins, loss, pts, runrate])
        i += 6
    s = ""
    for i in l:
        for j in i:
            #print(j,end='\t')
            s += j + '\t'
        #print()
        s += '\n'
    return s


def schedule():
    res = requests.get('https://www.iplt20.com/matches/schedule/men')
    data = BeautifulSoup(res.text, 'html.parser')
    d = data.find_all(class_='match-list__item')
    match_data = []
    for i in d:
        team1 = i.find_all(
            class_='fixture__team')[0].text.strip().split('\n')[0].strip()
        team2 = i.find_all(
            class_='fixture__team')[1].text.strip().split('\n')[0].strip()
        team = team1 + ' vs ' + team2
        time = i.find(class_='fixture__time').text
        venue = i.find(class_='fixture__info').text.strip().split('\n')
        month = int(i.get('data-timestamp').split('T')[0].split('-')[1])
        day = i.get('data-timestamp').split('T')[0].split('-')[2]
        if (month == 4):
            month = 'Apr'
        else:
            month = 'May'
        date = day + ' ' + month
        # print(date)
        if (len(venue) == 2):
            venue = venue[1] + ', ' + date
        else:
            venue = venue[2] + ', ' + date + ' --> Live Now'
        match_data.append([team, time, venue])
    return match_data


def most_runs():
    res = requests.get('https://www.iplt20.com/stats/2021/most-runs')
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(class_='table table--scroll-on-tablet top-players')
    most_run = [['Pos', 'Player', 'Match', 'Inn', 'Runs', 'Hs', 'Avg', 'SR']]
    data = data.find_all(class_='js-row')
    for i in data:
        pos = i.find(class_='js-pos').text
        name = i.find(
            class_='top-players__player-name').text.strip().split('\n')[0]
        name += ' ' + i.find(class_='top-players__player-name').text.strip(
        ).split('\n')[1].strip()
        match = i.find(class_='top-players__m').text.strip()
        inngs = i.find(class_='top-players__inns').text.strip()
        runs = i.find(class_='top-players__r').text.strip()
        hs = i.find(class_='top-players__hs').text.strip()
        avg = i.find(class_='top-players__a').text.strip()
        strte = i.find(class_='top-players__sr').text.strip()
        most_run.append([pos, name, match, inngs, runs, hs, avg, strte])
    return most_run


def most_wickets():
    res = requests.get('https://www.iplt20.com/stats/2021/most-wickets')
    data = BeautifulSoup(res.text, 'html.parser')
    data = data.find(class_='table table--scroll-on-tablet top-players')
    most_wicket = [[
        'Pos', 'Player', 'Match', 'Inn', 'Wkts', 'Best', 'Econ', 'SR'
    ]]
    data = data.find_all(class_='js-row')
    for i in data:
        pos = i.find(class_='js-pos').text
        name = i.find(
            class_='top-players__player-name').text.strip().split('\n')[0]
        name += ' ' + i.find(class_='top-players__player-name').text.strip(
        ).split('\n')[1].strip()
        match = i.find(class_='top-players__m').text.strip()
        inngs = i.find(class_='top-players__inns').text.strip()
        wkts = i.find(class_='top-players__w').text.strip()
        best = i.find(class_='top-players__bbi').text.strip()
        eco = i.find(class_='top-players__e').text.strip()
        strte = i.find(class_='top-players__sr').text.strip()
        most_wicket.append([pos, name, match, inngs, wkts, best, eco, strte])
    return most_wicket


@client.command(name='runhelp')
async def run_command(ctx):
    await ctx.trigger_typing()
    s = '$ls -> For live score' + '\n'
    s += '$sc -> Scheduled Match [2,3,4 ....] in agrument to see scheduled match upto that number' + '\n'
    s += '$mr -> Most run [2,3,4,....] (ex: $mr 5) in agrument to see upto that number' + '\n'
    s += '$mw -> Most wicket [2,3,4,....] (ex: $mw 5) in agrument to see upto that number' + '\n'
    s += '$pt -> Point table'
    s = '```' + s + '```'
    embed = discord.Embed(title='Instruction to use the bot',
                          description=s,
                          color=0xbd6868)
    await ctx.send(embed=embed)


@client.command(name='pt')
async def embed(ctx):
    await ctx.trigger_typing()
    s = point_table()
    s = '```' + s + '```'
    embed = discord.Embed(title="IPL 2021 Point Table",
                          description=s,
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command(name='ls')
async def score(ctx):
    await ctx.trigger_typing()
    s, head, bat, bowl = live_score_final()
    title = ':cricket_game: Live Score'
    embed = discord.Embed(title=title, color=discord.Color.blue())
    s = '```' + s + '```'
    embed.add_field(name=head, value=s, inline=False)
    if (bat != ''):
        bat = '```' + bat + '```'
        embed.add_field(name='Current Batting', value=bat, inline=False)
    if (bowl != ''):
        bowl = '```' + bowl + '```'
        embed.add_field(name='Current Bowling', value=bowl, inline=False)
    await ctx.send(embed=embed)


@client.command(name='sc')
async def args(ctx, arg=1):
    await ctx.trigger_typing()
    res = ''
    matchdata = schedule()
    matchdata = matchdata[:(int(arg))]
    for i in matchdata:
        s = ''
        for j in i:
            s += j + '\n'
        s = '```' + s + '```'
        res += s + '\n'
    embed = discord.Embed(title='Scheduled Match',
                          description=res,
                          color=discord.Color.red())
    await ctx.send(embed=embed)


@client.command(name='mr')
async def runs(ctx, arg=0):
    await ctx.trigger_typing()
    if (arg == 0):
        arg = 6
    else:
        arg += 1
    most_run = most_runs()[:(int(arg))]
    for i in range(len(most_run)):
        for j in range(8):
            if (j == 0):
                x = len(most_run[i][j])
                rem = 3 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            elif (j == 1):
                x = len(most_run[i][j])
                rem = 18 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            elif (j == 2):
                x = len(most_run[i][j])
                rem = 5 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            elif (j == 3):
                x = len(most_run[i][j])
                rem = 3 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            elif (j == 4):
                x = len(most_run[i][j])
                rem = 5 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            elif (j == 5):
                x = len(most_run[i][j])
                rem = 4 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            elif (j == 6):
                x = len(most_run[i][j])
                rem = 6 - x
                for k in range(rem):
                    most_run[i][j] += ' '
            else:
                x = len(most_run[i][j])
                rem = 6 - x
                for k in range(rem):
                    most_run[i][j] += ' '
    res = ''
    for i in range(len(most_run)):
        s = ''
        for j in range(8):
            s += most_run[i][j] + ' '
        if (i == 1):
            res += '\n'
        res += s + '\n'

    res = '```' + res + '```'
    embed = discord.Embed(title='IPL 2021 Most Runs',
                          description=res,
                          color=discord.Color.red())

    await ctx.send(embed=embed)


@client.command(name='mw')
async def wickets(ctx, arg=0):
    await ctx.trigger_typing()
    if (arg == 0):
        arg = 6
    else:
        arg += 1
    most_wicket = most_wickets()[:(int(arg))]
    for i in range(len(most_wicket)):
        for j in range(8):
            if (j == 0):
                x = len(most_wicket[i][j])
                rem = 3 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            elif (j == 1):
                x = len(most_wicket[i][j])
                rem = 19 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            elif (j == 2):
                x = len(most_wicket[i][j])
                rem = 5 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            elif (j == 3):
                x = len(most_wicket[i][j])
                rem = 3 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            elif (j == 4):
                x = len(most_wicket[i][j])
                rem = 5 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            elif (j == 5):
                x = len(most_wicket[i][j])
                rem = 5 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            elif (j == 6):
                x = len(most_wicket[i][j])
                rem = 6 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
            else:
                x = len(most_wicket[i][j])
                rem = 6 - x
                for k in range(rem):
                    most_wicket[i][j] += ' '
    res = ''
    for i in range(len(most_wicket)):
        s = ''
        for j in range(8):
            s += most_wicket[i][j] + ' '
        if (i == 1):
            res += '\n'
        res += s + '\n'

    res = '```' + res + '```'
    embed = discord.Embed(title='IPL 2021 Most wickets',
                          description=res,
                          color=discord.Color.red())

    await ctx.send(embed=embed)


keep_running()
client.run(os.getenv('TOKEN'))

# @client.event
# async def on_message(message):
#   if(message.author==client.user):
#     return

#   if message.content == '$pt':
#     s=point_table()
#     print(s)
#     embed=discord.Embed(title="IPL 2021 Point Table",description=s,color=discord.Color.blue())
#     embed.add_field(value='"Matches","Teams"',inline=False,name='score')
#     # embed.set_author(name=message.author,url=message.author.avatar_url,icon_url=message.author.avatar_url)
#     #await message.channel.send(f"hello  {message.author.mention} hi")
#     await message.channel.send(embed=embed)

# @bot.command(name='hello')
# async def stts(ctx):
#     await ctx.trigger_typing()
#     await ctx.send(f"Namaste {ctx.author.mention}")

# import discord
# from discord.ext.commands import Bot
# import os

# bot = Bot(command_prefix='$')
# TOKEN = '<INSERT TOKEN HERE>'

# @bot.event
# async def on_ready():
# 	print(f'Bot connected as {bot.user}')

# @bot.event
# async def on_message(message):
# 	if message.content == '$test':
# 		await message.channel.send('Testing 1 2 3!')

# @bot.command(name='server')
# async def fetchServerInfo(context):
# 	guild = context.guild
# 	await context.send(f'Server Name: {guild.name}')
# 	await context.send(f'Server Size: {len(guild.members)}')
# 	await context.send(f'Server Name: {guild.owner.display_name}')

# bot.run(os.getenv('TOKEN'))
