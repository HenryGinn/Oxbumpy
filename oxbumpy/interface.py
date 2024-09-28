from oxbumpy import load_data, read_json, get_df, display


# data = load_data(2022, "torpids")
data = read_json("torpids_2022.json")
divs = read_json("torpids_2022_divs.json")
df = get_df(data)
display_obj = display(df, divs)
