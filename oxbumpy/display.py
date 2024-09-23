import matplotlib.pyplot as plt


class Display():

    def __init__(self, df):
        self.df = df
        self.initialise_figure()
        self.plot_peripherals()
        self.plot_histories()
        plt.savefig("Chart.pdf", format="pdf")

    def initialise_figure(self):
        self.fig = plt.figure(figsize=(2, 10))
        ax_m = self.fig.add_axes([0, 0.02, 0.5, 0.96])
        ax_f = self.fig.add_axes([0.5, 0.02, 0.5, 0.96])
        self.axes = {"men": ax_m, "women": ax_f}

    def plot_peripherals(self):
        #self.set_axis_limits()
        #self.set_axis_titles()
        self.turn_off_axis_labels()
        #self.turn_off_plot_spines()

    def set_axis_limits(self):
        for ax in self.axes.values():
            ax.set_aspect('equal')
            ax.set_xlim((-0.3, 4.3))
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
                    color="#808080", markersize=1, marker="o")
            self.plot_logos(ax, college, -group_df["Position"].values[0])

    def plot_logos(self, ax, college, position):
        circle = plt.Circle((0, position), 0.3, color='blue', zorder=2)
        ax.add_patch(circle)


























