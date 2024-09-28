import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge, Rectangle, Circle
from numpy import cumsum


class Display():

    radius = 0.3
    small_radius = 0.15
    thin_width = 0.03
    thick_width = 0.07
    thicker_width = 0.15
    cross_width_small = 0.05
    cross_length_small = 0.18
    cross_width_large = thick_width
    cross_length_large = 0.32
    loop_width = 0.01
    line_height = 0.32
    outer_loop_radius = 0.32

    def __init__(self, df, divs):
        self.df, self.divs = df, divs
        self.row_count = self.df["Position"].max()
        self.initialise_figure()
        self.plot()
        plt.savefig(f"{self.df.name}.pdf", format="pdf")

    def initialise_figure(self):
        self.patches = {"men": [], "women": []}
        self.fig = plt.figure(figsize=(2.7, self.row_count * 0.1837233487734804))
        self.fig.patch.set_facecolor("#fafafa")
        self.set_axes()

    def set_axes(self):
        ax_m = self.fig.add_axes([0.05, 0.01, 0.45, 0.965])
        ax_f = self.fig.add_axes([0.52, 0.01, 0.45, 0.965])
        ax_m.set_facecolor("#fafafa")
        ax_f.set_facecolor("#fafafa")
        self.axes = {"men": ax_m, "women": ax_f}

    def plot(self):
        self.plot_peripherals()
        self.plot_histories()
        self.plot_logos()
        self.plot_divisions()
        self.plot_boat_numbers()

    def plot_peripherals(self):
        self.set_titles()
        self.set_axis_limits()
        self.turn_off_axis_labels()
        self.turn_off_plot_spines()

    def set_axis_limits(self):
        for ax in self.axes.values():
            ax.set_aspect('equal')
            ax.set_xlim((-1.3, 5.6))
            ax.set_ylim((-self.df["Position"].max()-0.5, 0))
        
    def set_titles(self):
        self.fig.suptitle(self.df.name, fontsize=10, y=0.99)
        for sex, ax in self.axes.items():
            ax.set_title(sex.title(), y=0.99, fontsize=6)

    def turn_off_axis_labels(self):
        for ax in self.axes.values():
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xticklabels([])
            ax.set_yticklabels([])

    def turn_off_plot_spines(self):
        for ax in self.axes.values():
            for direction in ["top", "right", "bottom", "left"]:
                ax.spines[direction].set_visible(False)
                    

    def plot_histories(self):
        for (college, sex, _), group_df in self.df.groupby(['College', 'Sex', 'Boat']):
            ax = self.axes[sex]
            ax.plot(group_df["Day"], -group_df["Position"], linewidth=0.8,
                    color="#808080", markersize=1, marker="o", zorder=-1)
            self.plot_logo(college, self.patches[sex], -group_df["Position"].values[0], -0.25)
            self.plot_logo(college, self.patches[sex], -group_df["Position"].values[-1], len(group_df["Position"].values)-0.75)

    def plot_logo(self, college, *args):
        self.draw_loop(*args, "#fafafa", self.outer_loop_radius)
        match college:
            case "ORO": self.college_oro(*args)
            case "PMB": self.college_pmb(*args)
            case "SCO": self.college_sco(*args)
            case "CHB": self.college_chb(*args)
            case "SEH": self.college_seh(*args)
            case "BAL": self.college_bal(*args)
            case "WOO": self.college_woo(*args)
            case "KEB": self.college_keb(*args)
            case "WAD": self.college_wad(*args)
            case "TRO": self.college_tro(*args)
            case "MAG": self.college_mag(*args)
            case "UCO": self.college_uco(*args)
            case "BRC": self.college_brc(*args)
            case "RPC": self.college_rpc(*args)
            case "SHG": self.college_shg(*args)
            case "LIN": self.college_lin(*args)
            case "EXC": self.college_exc(*args)
            case "QCO": self.college_qco(*args)
            case "HEC": self.college_hec(*args)
            case "NEC": self.college_nec(*args)
            case "JEO": self.college_jeo(*args)
            case "MER": self.college_mer(*args)
            case "SJO": self.college_sjo(*args)
            case "LMH": self.college_lmh(*args)
            case "MAN": self.college_man(*args)
            case "COO": self.college_coo(*args)
            case "SPC": self.college_spc(*args)
            case "GTM": self.college_gtm(*args)
            case "SAC": self.college_sac(*args)
            case "SOM": self.college_som(*args)
            case "LIC": self.college_lic(*args)
            case "WRO": self.college_wro(*args)
            case "SAY": self.college_say(*args)
            case "SHI": self.college_shi(*args)
            case "SBH": self.college_sbh(*args)
            case "OSG": self.college_osg(*args)
            case "REC": self.college_rec(*args)
            case _: self.college_blank(*args)

    def college_oro(self, *args):
        self.draw_circle(*args, "#1c4882")
        self.draw_thin_line(*args, "white")
        self.draw_small_circle(*args, "white")
        
    def college_pmb(self, *args):
        self.draw_circle(*args, "white")
        self.draw_thick_line(*args, "#ff727d")
        
    def college_sco(self, *args):
        self.draw_circle(*args, "#46bada")
        self.draw_small_circle(*args, "#761b2e")
    
    def college_chb(self, *args):
        self.draw_circle(*args, "#12266e")
        
    def college_seh(self, *args):
        self.draw_circle(*args, "#ffea00")
        self.draw_small_cross(*args, "#981206")
        
    def college_bal(self, *args):
        self.draw_circle(*args, "#0f2e61")
        self.draw_thick_line(*args, "#c91a17")
        
    def college_woo(self, *args):
        self.draw_circle(*args, "#e9cb07")
        self.draw_thick_line(*args, "#9d0505")
    
    def college_keb(self, *args):
        self.draw_circle(*args, "#f0f0f0")
        self.draw_thick_line(*args, "#c40606")
    
    def college_wad(self, *args):
        self.draw_circle(*args, "#79b0e7")
        self.draw_small_cross(*args, "#ffffff")
    
    def college_tro(self, *args):
        self.draw_circle(*args, "#00007f")
        self.draw_thick_line(*args, "#ffffff")
    
    def college_mag(self, *args):
        self.draw_circle(*args, "#000000")
        self.draw_small_circle(*args, "#ffffff")
    
    def college_uco(self, *args):
        self.draw_circle(*args, "#00007f")
        self.draw_small_cross(*args, "#ffff00")
    
    def college_brc(self, *args):
        self.draw_circle(*args, "#000102")
    
    def college_rpc(self, *args):
        self.draw_circle(*args, "#ed1212")
        self.draw_large_cross(*args, "#ffffff")
    
    def college_shg(self, *args):
        self.draw_left_semicircle(*args, "#ffff00")
        self.draw_right_semicircle(*args, "#00007f")
        self.draw_thick_line(*args, "#ffffff")
    
    def college_lin(self, *args):
        self.draw_circle(*args, "yellow")
        self.draw_thick_line_angle(*args, "black", 45)
        self.draw_thick_line_angle(*args, "black", 135)
    
    def college_exc(self, *args):
        self.draw_circle(*args, "#c30b0b")
    
    def college_qco(self, *args):
        self.draw_circle(*args, "#03035c")
        self.draw_thick_line_angle(*args, "#fafafa", 90)
    
    def college_hec(self, *args):
        self.draw_circle(*args, "#9e1616")
        self.draw_thick_line(*args, "#f0f0f0")
    
    def college_nec(self, *args):
        self.draw_circle(*args, "#a54a8d")
        self.draw_thick_line(*args, "#f3df04")
    
    def college_jeo(self, *args):
        self.draw_circle(*args, "#0e922b")
    
    def college_mer(self, *args):
        self.draw_circle(*args, "#f0f0f0")
        self.draw_small_cross(*args, "#834898")
    
    def college_sjo(self, *args):
        self.draw_circle(*args, "#ffffff")
        self.draw_large_cross(*args, "#00007f")
    
    def college_lmh(self, *args):
        self.draw_circle(*args, "#0f277f")
        self.draw_thin_line(*args, "#e9dc07")
    
    def college_man(self, *args):
        self.draw_circle(*args, "#c30b0b")
        self.draw_small_cross(*args, "#dec30a")
    
    def college_coo(self, *args):
        self.draw_circle(*args, "#121078")
        self.draw_thick_line(*args, "#740404")
    
    def college_spc(self, *args):
        self.draw_left_semicircle(*args, "#e9cb07")
        self.draw_right_semicircle(*args, "#1c6810")
        self.draw_thick_line(*args, "#ffffff")
    
    def college_gtm(self, *args):
        self.draw_left_semicircle(*args, "#235f11")
        self.draw_right_semicircle(*args, "#2a5c7e")
        self.draw_thin_line(*args, "#dbae11")
    
    def college_sac(self, *args):
        self.draw_circle(*args, "#ed1212")
        self.draw_thick_line(*args, "#cccccc")
    
    def college_som(self, *args):
        self.draw_circle(*args, "#ed1212")
        self.draw_thick_line(*args, "#000000")
    
    def college_lic(self, *args):
        self.draw_circle(*args, "#2c6484")
        self.draw_thick_line(*args, "#40b8ca")
    
    def college_wro(self, *args):
        self.draw_circle(*args, "#000000")
        self.draw_small_cross(*args, "#ff00ff")
    
    def college_say(self, *args):
        self.draw_left_semicircle(*args, "#e6b810")
        self.draw_right_semicircle(*args, "#ff0000")
        self.draw_thick_line(*args, "#000000")
    
    def college_shi(self, *args):
        self.draw_sector(*args, "#00007f", 225, 405)
        self.draw_sector(*args, "#ffffff", 45, 225)
    
    def college_sbh(self, *args):
        self.draw_circle(*args, "#ffffff")
        self.draw_thick_line(*args, "#15468a")
    
    def college_osg(self, *args):
        self.draw_circle(*args, "#ffffff")
        self.draw_loop(*args, "#000000", self.radius)
        self.draw_small_circle(*args, "#ba0a0a")

    def college_rec(self, *args):
        self.draw_left_semicircle(*args, "#0d0e48")
        self.draw_right_semicircle(*args, "#00992c")
        self.draw_line(*args, "#ffffff", self.radius, self.thicker_width)
    

    def college_blank(self, *args):
        pass

    def draw_small_circle(self, *args):
        self.draw_sector(*args, angle_1=0, angle_2=360, radius=self.small_radius)
    
    def draw_left_semicircle(self, *args):
        self.draw_sector(*args, angle_1=90, angle_2=270)

    def draw_right_semicircle(self, *args):
        self.draw_sector(*args, angle_1=270, angle_2=450)

    def draw_sector(self, patches, position, x, color, angle_1=None, angle_2=None, radius=None):
        if radius is None:
            radius = self.radius
        patches.append({
            "Patch": Wedge((x, position), radius,
                           angle_1, angle_2, linewidth=0),
            "Color": color, "Edge Color": "none"})

    def draw_circle(self, patches, position, x, color, radius=None):
        if radius is None:
            radius = self.radius
        patches.append({
            "Patch": Circle((x, position), radius),
            "Color": color, "Edge Color": "none"})

    def draw_loop(self, patches, position, x, color, radius=None):
        if radius is None:
            radius = self.radius
        patches.append({
            "Patch": Circle((x, position), radius,
                            linewidth=self.loop_width),
            "Color": "none", "Edge Color": color})

    def draw_thick_line(self, *args):
        self.draw_line(*args, self.line_height, self.thick_width)

    def draw_thin_line(self, *args):
        self.draw_line(*args, self.line_height, self.thin_width)

    def draw_thick_line_angle(self, patches, position, x, color, angle):
        patches.append({
            "Patch": Rectangle((x - self.thick_width, position - self.line_height),
                               2*self.thick_width, 2*self.line_height,
                               rotation_point="center", angle=angle),
            "Color": color, "Edge Color": "none"})

    def draw_line(self, patches, position, x, color, height, width):
        patches.append({
            "Patch": Rectangle((x - width, position - height),
                               2*width, 2*height),
            "Color": color, "Edge Color": "none"})

    def draw_small_cross(self, *args):
        self.draw_cross(*args,
                        self.cross_width_small,
                        self.cross_length_small)

    def draw_large_cross(self, *args):
        self.draw_cross(*args,
                        self.cross_width_large,
                        self.cross_length_large)

    def draw_cross(self, patches, position, x, color, width, length):
        patches += [
            {"Patch": Rectangle((x - length, position - width),
                2*length, 2*width), "Color": color, "Edge Color": "none"},
            {"Patch": Rectangle((x - width, position - length),
                2*width, 2*length), "Color": color, "Edge Color": "none"}]
        
    def plot_logos(self):
        for sex in ["men", "women"]:
            patches = [patch["Patch"] for patch in self.patches[sex]]
            colors = [patch["Color"] for patch in self.patches[sex]]
            edge_colors = [patch["Edge Color"] for patch in self.patches[sex]]
            patch_collection = PatchCollection(patches)
            patch_collection.set_facecolor(colors)
            patch_collection.set_edgecolor(edge_colors)
            self.axes[sex].add_collection(patch_collection)

    def plot_divisions(self):
        for sex, divs_sex in self.divs.items():
            ax = self.axes[sex]
            div_sizes = [div["size"] for div in divs_sex]
            div_times = [div["time"] for div in divs_sex]
            div_sizes_cumulative = [0] + list(cumsum(div_sizes)[:-1])
            self.plot_division_lines(ax, div_sizes_cumulative[1:])
            self.plot_division_times(ax, div_sizes_cumulative, div_times)
            

    def plot_division_lines(self, ax, div_sizes_cumulative):
        for div_position in div_sizes_cumulative:
            x = [-2*self.radius, 4 + 2*self.radius]
            y = [-div_position - 0.5, -div_position - 0.5]
            ax.plot(x, y, color="k", linewidth=1)

    def plot_division_times(self, ax, positions, times):
        for index, (position, time) in enumerate(zip(positions, times)):
            ax.text(4.8, -position-0.45, f"Division {roman(index+1)}: {time}",
                    va="top", rotation=-90, fontsize=7)

    def plot_boat_numbers(self):
        for sex, ax in self.axes.items():
            positions = self.df.loc[self.df["Sex"] == sex]["Position"].max()
            for position in range(positions):
                ax.text(-1.3, -position-1, f"{position+1}.",
                        ha="left", va="center", fontsize=4.5)


def roman(n):
    if n in roman_lookup:
        return roman_lookup[n]
    else:
        return str(n)

roman_lookup = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
    16: "XVI",
    17: "XVII",
    18: "XVIII",
    19: "XIX",
    20: "XX"}
