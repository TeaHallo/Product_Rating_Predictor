import matplotlib.pyplot as plt


class Graphs:

    def __init__(self):
        pass

    def plot_graphs(self, cereal_data):
        fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
        fig.suptitle("Rating vs Sugar, Calories, and Fat")
        plt.get_current_fig_manager().set_window_title("Data History")

        x = cereal_data["Sugar (g)"]
        y = cereal_data["Rating"]
        axs[0, 0].scatter(x, y)
        plt.setp(axs[0, 0], xlabel='Sugar (g)')
        plt.setp(axs[0, 0], ylabel='Rating')

        x2 = cereal_data["Calories"]
        y2 = cereal_data["Rating"]
        axs[0, 1].scatter(x2, y2)
        plt.setp(axs[0, 1], xlabel='Calories')
        plt.setp(axs[0, 1], ylabel='Rating')

        x3 = cereal_data["Fat (g)"]
        y3 = cereal_data["Rating"]
        axs[1, 0].bar(x3, y3)
        plt.setp(axs[1, 0], xlabel='Fat (g)')
        plt.setp(axs[1, 0], ylabel='Rating')

        fig.delaxes(axs[1][1])
        fig.tight_layout()
        plt.show()
