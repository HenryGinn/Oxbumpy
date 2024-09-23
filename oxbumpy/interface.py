from oxbumpy import load_data, read_data, get_df, display


# data = load_data(2022, "torpids")
data = read_data("torpids_2022.json")
df = get_df(data)
display_obj = display(df)
