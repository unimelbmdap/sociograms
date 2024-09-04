import pandas as pd

nodes = pd.read_excel('Sociograms.xlsx', sheet_name="Nodes")
edges = pd.read_excel('Sociograms.xlsx', sheet_name="Edges")
quotes = pd.read_excel('Sociograms.xlsx', sheet_name="Quotes")
person = pd.read_excel('Sociograms.xlsx', sheet_name="Persons")

# set level by distance from 'Me'
# nodes
nodes['label'] = nodes['name']
levels_map = {'Person': 1, 'Platform' : 2, 'Recipients': 3, 'Video': 4,'Image': 4, }
nodes['level'] = nodes['type'].map(levels_map)

color_map = {
    'Image': '#8dd3c7',
    'Person': '#fb8072',
    'Platform': '#8da0cb',
    'Recipients': '#ffffb3',
    'Video': '#8dd3c7'}
nodes['color'] = nodes['type'].map(color_map)
nodes.set_index('name', inplace=True)
nodes['name'] = nodes['label']

nodecols = ['name','type','label','level','color']
quotecols = ['Node', 'Quote', 'File']

nodes[nodecols].sort_values(by='label').to_json("nodes.json",indent=2, mode='w',orient='index')

# deduplicate edges and save as json
edgecols = ['source', 'target']
#edges.drop_duplicates(subset=edgecols, keep="first",inplace=True,ignore_index=True)
print(edges.columns)
edges[edgecols].sort_values(by='source').to_json("edges.json",indent=2, mode='w',orient='index')

# structure edges to be level 1 (me) -> level 2 (platform) -> level 3 (who shared with) -> level 4 (what shared)
#  and now adjusted to allow level 1 -> level 2 -> level 4 as well
# deducing that Me sharing to Instagram with Close friends and Me sharing to Instagram what Everyday photos
#    (without an edge that says Me shares to Instagram with Close Friends what Everyday photos)
#     so assume level 2 to level 4 will be through the 'Platform' node wich is another column



# save as csv for exploration
nodeTypes = pd.Series(nodes['level'].values,index=nodes['name']).to_dict()
edges['srcLvel'] = edges['source'].map(nodeTypes)
edges['tarLvel'] = edges['target'].map(nodeTypes)
edgecols=['id','source','srcLvel','relationship','target','tarLvel']
edges[edgecols].sort_values(['id','srcLvel','tarLvel']).to_csv("edges.csv",index=False)


sociograms = edges['id'].unique()
edges['diff'] = edges.apply(lambda row: int(row['tarLvel'])-int(row['srcLvel']),axis=1)
edgecols=['id','source','srcLvel','relationship','target','tarLvel','diff','platform']
print(sociograms)
print(edgecols)

# its not pythonic but its helping me think through the logic
for s in sociograms:
    for ix,e in edges[edges['id']==s].iterrows():
        if (int(e['diff'])>1):
            newEdge = [s,e['platform'],levels_map['Platform'],'with',e['target'],e['tarLvel'],1,e['platform']]
            if (e.tarLvel==4):
                newEdgedf = pd.DataFrame(columns=edgecols,data=[newEdge])
                edges = pd.concat([edges[edgecols],newEdgedf[edgecols]],ignore_index=True)
            else:
                print('hang on whats this then: not level 4 but jumped two levels')


edges[edgecols].sort_values(['id','srcLvel','tarLvel']).to_csv("edges.csv",index=False)

edgecols=['id','source','relationship','target']
edges.drop_duplicates(subset=edgecols, keep="first",inplace=True,ignore_index=True)
edges[edgecols].sort_values(by='source').to_json("edges.json",indent=2, mode='w',orient='index')
