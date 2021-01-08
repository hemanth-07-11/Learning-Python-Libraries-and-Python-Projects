import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate

website = requests.get('https://www.cricbuzz.com/')
webpage = bs(website.content, 'lxml')

all_scores = webpage.find('div', class_='videos-list-carousal')
score_card_all = all_scores.find('ul', class_='cb-col')
score_card = score_card_all.find_all('li', class_='cb-col')
for sc in score_card:
    score_info = sc.select('a')
    Match_title = sc.find("a")["title"]
    a = sc.find("a")["href"]
    team_one = sc.select('div .cb-hmscg-bwl-txt .cb-ovr-flo')
    team_two = sc.select('div .cb-hmscg-bat-txt .cb-ovr-flo')
    result = sc.select('div .cb-ovr-flo')
    for i in range(4):
        print(
            '----------------------------------------------------------------------------------------------------------------------')

    if team_one and team_two and result:
        print(Match_title)
        print(team_one[0].text, team_one[1].text, team_two[0].text, team_two[1].text)
        print(result[5].text, '\n')
    else:
        print(Match_title)
        print()

    url = 'https://www.cricbuzz.com'
    a_rep = a.replace('live-cricket-scores', 'live-cricket-scorecard')
    score_url = url + a_rep

    # score_url = 'https://www.cricbuzz.com/live-cricket-scorecard/30854/nz-vs-pak-2nd-t20i-pakistan-tour-of-new-zealand-2020-21 '
    score_link_get = requests.get(score_url)
    score_page = bs(score_link_get.content, 'lxml')

    for i in range(1, 3):
        print('\n')
        print(f"                                INNINGS_{i}                                   ")
        print('\n')
        print('                                 BATTING                                       ')

        if score_page.find('div', id=f"innings_{i}"):
            innings_one_div = score_page.find('div', id=f"innings_{i}")
            innings_one_score_div = innings_one_div.find('div', class_='cb-col')

            values = innings_one_score_div.select('div[class="cb-col cb-col-100 cb-scrd-itms"]')

            #
            player_name = []
            out_by = []
            runs_scored = []
            player_score_info = []
            ball = []
            fours = []
            sixes = []
            strike_rate = []
            for val in values:
                if val.find('a'):
                    player_name.append(val.find('a').string.strip())

                if val.select('div[class="cb-col cb-col-33"]'):
                    out_by.append(val.select('div[class="cb-col cb-col-33"]')[0].text.strip())

                if val.select('div[class="cb-col cb-col-8 text-right text-bold"]'):
                    runs_scored.append(val.select('div[class="cb-col cb-col-8 text-right text-bold"]')[0].text)

                temp = []
                extra_info = val.select('div[class="cb-col cb-col-8 text-right"]')
                for i in range(len(extra_info) - 3):
                    if val.select('div[class="cb-col cb-col-8 text-right"]'):
                        ball.append(int(extra_info[i].text))
                        fours.append(int(extra_info[i + 1].text))
                        sixes.append(int(extra_info[i + 2].text))
                        strike_rate.append(float(extra_info[i + 3].text))

                player_score_info.append(temp)

            l = []
            column_names = ['Name', 'Out', ' Run', 'Balls', "4's", "6's", 'strike_rate']
            for i in range(len(runs_scored)):
                l.append([player_name[i], out_by[i], runs_scored[i], ball[i], fours[i], sixes[i], strike_rate[i]])

            df = pd.DataFrame(l, columns=column_names)
            print(tabulate(df, showindex=False, headers=df.columns))

            print('\n')
            print('                                   BOWLING                                                    ')
            innings_one_bowl_div = innings_one_div.find_all('div', {"class": "cb-col cb-col-100 cb-ltst-wgt-hdr"})
            bowl_info = innings_one_bowl_div[1].find_all('div', {"class": "cb-col cb-col-100 cb-scrd-itms"})

            bolwer_column_name = ['Name', 'Over', 'Maiden', 'Wide_ball', 'No_ball', 'Run', 'Economy', 'Wickets']
            Name = []
            over = []
            maiden = []
            wide_ball = []
            no_ball = []
            run = []
            economy = []
            wickets = []
            for bi in bowl_info:
                for name in bi.select('a'):
                    Name.append(name.text.strip())
                # print(bi.find_all('div',{"class":"cb-col cb-col-8 text-right"}))
                # print(bi.find_all('div', {"class": "cb-col cb-col-10 text-right"}))
                # print(bi.find_all('div', {"class": "cb-col cb-col-8 text-right text-bold"}))

                omwn_values = bi.find_all('div', {"class": "cb-col cb-col-8 text-right"})

                for i in range(len(omwn_values) - 3):
                    over.append(float(omwn_values[i].text))
                    maiden.append(int(omwn_values[i + 1].text))
                    wide_ball.append(int(omwn_values[i + 2].text))
                    no_ball.append(int(omwn_values[i + 3].text))

                re = bi.find_all('div', {"class": "cb-col cb-col-10 text-right"})
                for i in range(len(re) - 1):
                    run.append(int(re[i].text))
                    economy.append(float(re[i + 1].text))

                w = bi.find_all('div', {"class": "cb-col cb-col-8 text-right text-bold"})
                for i in range(len(w)):
                    wickets.append(int(w[i].text))

            l = []
            for i in range(len(Name)):
                l.append([Name[i], over[i], maiden[i], wide_ball[i], no_ball[i], run[i], economy[i], wickets[i]])

            df = pd.DataFrame(l, columns=bolwer_column_name)
            print(tabulate(df, showindex=False, headers=df.columns))

    if score_page.find('div', id="innings_3"):
        for i in range(3, 5):
            if f"innings_{i}":
                print('\n')
                print(f"                                    INNINGS_{i}                                   ")
                print('\n')
                print('                                     BATTING                                       ')

                if score_page.find('div', id=f"innings_{i}"):
                    innings_one_div = score_page.find('div', id=f"innings_{i}")
                    innings_one_score_div = innings_one_div.find('div', class_='cb-col')

                    values = innings_one_score_div.select('div[class="cb-col cb-col-100 cb-scrd-itms"]')

                    #
                    player_name = []
                    out_by = []
                    runs_scored = []
                    player_score_info = []
                    ball = []
                    fours = []
                    sixes = []
                    strike_rate = []
                    for val in values:
                        if val.find('a'):
                            player_name.append(val.find('a').string.strip())

                        if val.select('div[class="cb-col cb-col-33"]'):
                            out_by.append(val.select('div[class="cb-col cb-col-33"]')[0].text.strip())

                        if val.select('div[class="cb-col cb-col-8 text-right text-bold"]'):
                            runs_scored.append(val.select('div[class="cb-col cb-col-8 text-right text-bold"]')[0].text)

                        temp = []
                        extra_info = val.select('div[class="cb-col cb-col-8 text-right"]')
                        for i in range(len(extra_info) - 3):
                            if val.select('div[class="cb-col cb-col-8 text-right"]'):
                                ball.append(int(extra_info[i].text))
                                fours.append(int(extra_info[i + 1].text))
                                sixes.append(int(extra_info[i + 2].text))
                                strike_rate.append(float(extra_info[i + 3].text))

                        player_score_info.append(temp)

                    l = []
                    column_names = ['Name', 'Out', ' Run', 'Balls', "4's", "6's", 'strike_rate']
                    for i in range(len(runs_scored)):
                        l.append(
                            [player_name[i], out_by[i], runs_scored[i], ball[i], fours[i], sixes[i], strike_rate[i]])

                    df = pd.DataFrame(l, columns=column_names)
                    print(tabulate(df, showindex=False, headers=df.columns))

                    print('\n')
                    print(
                        '                                   BOWLING                                                    ')
                    print('\n')
                    innings_one_bowl_div = innings_one_div.find_all('div',
                                                                    {"class": "cb-col cb-col-100 cb-ltst-wgt-hdr"})
                    bowl_info = innings_one_bowl_div[1].find_all('div', {"class": "cb-col cb-col-100 cb-scrd-itms"})

                    bolwer_column_name = ['Name', 'Over', 'Maiden', 'Wide_ball', 'No_ball', 'Run', 'Economy', 'Wickets']
                    Name = []
                    over = []
                    maiden = []
                    wide_ball = []
                    no_ball = []
                    run = []
                    economy = []
                    wickets = []
                    for bi in bowl_info:
                        for name in bi.select('a'):
                            Name.append(name.text.strip())
                     
                        omwn_values = bi.find_all('div', {"class": "cb-col cb-col-8 text-right"})

                        for i in range(len(omwn_values) - 3):
                            over.append(float(omwn_values[i].text))
                            maiden.append(int(omwn_values[i + 1].text))
                            wide_ball.append(int(omwn_values[i + 2].text))
                            no_ball.append(int(omwn_values[i + 3].text))

                        re = bi.find_all('div', {"class": "cb-col cb-col-10 text-right"})
                        for i in range(len(re) - 1):
                            run.append(int(re[i].text))
                            economy.append(float(re[i + 1].text))

                        w = bi.find_all('div', {"class": "cb-col cb-col-8 text-right text-bold"})
                        for i in range(len(w)):
                            wickets.append(int(w[i].text))

                    l = []
                    for i in range(len(Name)):
                        l.append(
                            [Name[i], over[i], maiden[i], wide_ball[i], no_ball[i], run[i], economy[i], wickets[i]])

                    df = pd.DataFrame(l, columns=bolwer_column_name)
                    print(tabulate(df, showindex=False, headers=df.columns))
