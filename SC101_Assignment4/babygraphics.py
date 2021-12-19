"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    margin_range = width - 2*GRAPH_MARGIN_SIZE
    margin = margin_range / len(YEARS)
    x_coordinate = int(GRAPH_MARGIN_SIZE+margin*year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # draw basic lines
    # top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # left line
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    # interval line
    for i in range(0, len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # Write your code below this line
    # 定義不同名次的高度位置係數，rank+1,高度加(CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)/1000)
    rank_height_index = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / 1000
    color_index = 0
    for i in lookup_names:
        # color choose
        color = COLORS[color_index % len(COLORS)]
        color_index += 1
        for j in range(0,len(YEARS)):
            YEARS[j] = str(YEARS[j])
            #
            if YEARS[j] not in name_data[i].keys():
                # text: 未在排名內，則畫出*
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH,j) + TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text=i+' *'
                                   ,anchor=tkinter.SW)
                # line: 取得j+1年的沒有排名的高度位置
                if j < len(YEARS)-1 and str(YEARS[j+1]) not in name_data[i].keys():
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH,j),CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH,j+1),CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       fill = color,width = LINE_WIDTH)
                # line: 取得j+1年的有排名的高度位置
                elif j < len(YEARS)-1:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, j + 1),
                                       GRAPH_MARGIN_SIZE+(int(name_data[i][str(YEARS[j+1])])-1)*rank_height_index,
                                       fill = color,width = LINE_WIDTH)
            else:
                # text: 有排名的年份，標示出name 及排名
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH,j) + TEXT_DX,
                                   # 高度取出rank後，乘以rank_height_index
                                   GRAPH_MARGIN_SIZE+(int(name_data[i][YEARS[j]])-1)*rank_height_index
                                   ,text=i+' '+name_data[i][YEARS[j]]
                                   ,anchor=tkinter.SW)
                # line: 取得j+1年的沒有排名的高度位置
                if j < len(YEARS)-1 and str(YEARS[j+1]) not in name_data[i].keys():
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH,j),
                                       GRAPH_MARGIN_SIZE+(int(name_data[i][YEARS[j]])-1)*rank_height_index,
                                       get_x_coordinate(CANVAS_WIDTH,j+1),CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       fill = color,width = LINE_WIDTH)
                # line: 取得j+1年的有排名的高度位置
                elif j < len(YEARS)-1:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + (int(name_data[i][YEARS[j]]) - 1) * rank_height_index,
                                       get_x_coordinate(CANVAS_WIDTH, j + 1),
                                       GRAPH_MARGIN_SIZE+(int(name_data[i][str(YEARS[j+1])])-1)*rank_height_index,
                                       fill = color,width = LINE_WIDTH)





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
