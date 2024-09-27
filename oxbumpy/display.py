import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge, Rectangle, Circle


class Display():

    radius = 0.3
    small_radius = 0.15
    thin_width = 0.03
    thick_width = 0.07
    cross_width_small = 0.05
    cross_length_small = 0.18
    cross_width_large = thick_width
    cross_length_large = 0.32
    loop_width = 0.01
    line_height = 0.32
    outer_loop_radius = 0.32

    def __init__(self, df):
        self.df = df
        self.row_count = self.df["Position"].max()
        self.initialise_figure()
        self.plot()
        plt.savefig("Chart.pdf", format="pdf")

    def initialise_figure(self):
        self.patches = {"men": [], "women": []}
        self.fig = plt.figure(figsize=(2.5, self.row_count*300/1679))
        self.fig.patch.set_facecolor("#fafafa")
        self.set_axes()

    def set_axes(self):
        ax_m = self.fig.add_axes([0.05, 0.01, 0.45, 0.98])
        ax_f = self.fig.add_axes([0.55, 0.01, 0.45, 0.98])
        ax_m.set_facecolor("#fafafa")
        ax_f.set_facecolor("#fafafa")
        self.axes = {"men": ax_m, "women": ax_f}

    def plot(self):
        self.plot_peripherals()
        self.plot_histories()
        self.plot_logos()
        self.plot_division_lines()

    def plot_peripherals(self):
        self.set_axis_limits()
        #self.set_axis_titles()
        self.turn_off_axis_labels()
        self.turn_off_plot_spines()

    def set_axis_limits(self):
        for ax in self.axes.values():
            ax.set_aspect('equal')
            ax.set_xlim((-0.6, 4.6))
            ax.set_ylim((-self.df["Position"].max()-0.5, 0))
        
    def set_axis_titles(self):
        for sex, ax in self.axes.items():
            ax.set_title(sex.title(), y=0.99)

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
        self.draw_loop(*args, "white", self.outer_loop_radius)
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
            case "SMO": self.college_smo(*args)
            case "LIC": self.college_lic(*args)
            case "WRO": self.college_wro(*args)
            case "SAY": self.college_say(*args)
            case "SHI": self.college_shi(*args)
            case "SBH": self.college_sbh(*args)
            case "OSG": self.college_osg(*args)
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
    
    def college_smo(self, *args):
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
        self.draw_circle(*args, "blue")
        self.draw_thick_line(*args, "blue")
    
    def college_osg(self, *args):
        self.draw_circle(*args, "#ffffff")
        self.draw_loop(*args, "#000000", self.radius)
        self.draw_small_circle(*args, "#ba0a0a")
    

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
        self.draw_line(*args, self.thick_width)

    def draw_thin_line(self, *args):
        self.draw_line(*args, self.thin_width)

    def draw_thick_line_angle(self, patches, position, x, color, angle):
        patches.append({
            "Patch": Rectangle((x - self.thick_width, position - self.line_height),
                               2*self.thick_width, 2*self.line_height,
                               rotation_point="center", angle=angle),
            "Color": color, "Edge Color": "none"})

    def draw_line(self, patches, position, x, color, width):
        patches.append({
            "Patch": Rectangle((x - width, position - self.line_height),
                               2*width, 2*self.line_height),
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

    def plot_division_lines(self):
        pass
