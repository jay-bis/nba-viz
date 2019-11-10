from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt

def create_court(ax=None, color='black', linewidth=2, fig=None):
    if ax is None:
        fig, ax = plt.subplots()
        
    hoop = Circle((0, 0), radius=7.5, linewidth=linewidth, color=color, fill=False)
    
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=linewidth, color=color)
    
    outerPaintBox = Rectangle((-80, -47.5), 160, 190, linewidth=linewidth, color=color, fill=False)
    
    innerPaintBox = Rectangle((-60, -47.5), 120, 190, linewidth=linewidth, color=color, fill=False)
    
    topFreeThrow = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=linewidth, color=color, fill=False)
    
    bottomFreeThrow = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=linewidth, color=color, linestyle='dashed')
    
    # restricted zone
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=linewidth, color=color)
    
    # three point line corner A
    cornerThreeA = Rectangle((-220, -47.5), 0, 140, linewidth=linewidth, color=color)
    
    # three point line corner B
    cornerThreeB = Rectangle((220, -47.5), 0, 140, linewidth=linewidth, color=color)
    
    # 3 pt arc
    threeSemiCirc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=linewidth, color=color)
    
    # center court
    centerOuterArc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=linewidth, color=color)
    centerInnerArc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,linewidth=linewidth, color=color)
    
    # sideline out of bounds, baseline and half court line
    outLines = Rectangle((-250, -47.5), 500, 470, linewidth=linewidth ,color=color, fill=False)
    
    # put all court elements in list so they can easily be iterated over
    courtElements = [hoop, backboard, outerPaintBox, innerPaintBox, topFreeThrow, bottomFreeThrow, restricted, cornerThreeA,
                     cornerThreeB, threeSemiCirc, centerOuterArc, centerInnerArc, outLines]
    
    # now, add all court elements to plot
    for element in courtElements:
        ax.add_patch(element)
    
    return (fig, ax)
