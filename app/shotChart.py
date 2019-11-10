# Developer: Jack Biscupski
# Used http://savvastjortjoglou.com/nba-shot-sharts.html as a reference

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from .createCourt import create_court
from nba_api.stats.endpoints import shotchartdetail

#sns.set_style('white')
#sns.set_color_codes()

# temporary fix for HTTP timeout bug in nba_api:
# put these headers in the headers kwarg for any
# async request (like ShotChartDetail)
headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# James Harden
# team_id =1610612745, player_id=201935

def create_shot_chart(pid, tid, name):
    career = shotchartdetail.ShotChartDetail(team_id=tid, player_id=pid, headers=headers)
    shots = career.get_data_frames()[0]

    cmap = plt.cm.get_cmap('gist_heat_r')

    joint_shot_chart = sns.jointplot(shots.LOC_X, shots.LOC_Y, stat_func=None, kind='hex', space=0, color=cmap(.2), cmap=cmap, gridsize=26, height=8)
    joint_shot_chart.fig.set_size_inches(12,11)
    ax = joint_shot_chart.ax_joint
    fig = joint_shot_chart.fig

    ax.set_xlim(-235, 235)
    ax.set_ylim(295, -20)

    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom='off', labelleft='off')

    ax.set_title('{} FGA, 2018-2019 Regular Season'.format(name), y=1.2)
    return create_court(ax, fig=fig)

