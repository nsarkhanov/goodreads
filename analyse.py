import preprocess


anay_goup = df.groupby("original_publish_year")[
    'minmax_norm_ratings'].mean().round(decimals=2)
anay_goup.to_frame()

# #                                         The Best Book Author


def get_book_author(name, df):
    f = df[df.loc[:, 'author'] == name]
    m = f['minmax_norm_ratings'].max()
    return m


###
get_book_author('Cassandra Clare', df)
