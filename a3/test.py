verts = ['v0', 'v1', 'v2', 'v3', 'v4',' v5', 'v6', 'v7', 'v7',' v8', 'v9']


cycle0 = verts[3:] + verts[:3]
cycle0.append(verts[3])

print(cycle0)


for x in range(len(verts) - 1, -1, -1):
    print(x)